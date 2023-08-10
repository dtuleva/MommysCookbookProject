from django.shortcuts import render, redirect
from pyperclip import copy

from MommysCookbookProject.conversion.forms import ConversionForm


def convert_measurement(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            source_unit = form.cleaned_data['source_unit']
            ingredient = form.cleaned_data['ingredient']
            target_unit = form.cleaned_data['target_unit']

            # Convert to grams first
            grams_quantity = quantity * source_unit.conversion_to_grams

            # Perform the conversion using the conversion rates
            converted_quantity = grams_quantity / target_unit.conversion_to_grams

            # Add ingredient density factor for volume measurements

            if source_unit.volume_unit and source_unit.volume_unit and not target_unit.volume_unit:
                converted_quantity = converted_quantity * (ingredient.grams_in_a_cup / 240)
            if target_unit.volume_unit and not source_unit.volume_unit:
                converted_quantity = converted_quantity / (ingredient.grams_in_a_cup / 240)

            if ingredient is None:
                ingredient = ""

            converted_quantity_to_string = f"{quantity:.{source_unit.precision}f}{source_unit.unit} {ingredient} =" \
                                           f" {converted_quantity:.{target_unit.precision}f}{target_unit}"

            context = {
                'form': form,
                'converted_quantity': converted_quantity,
                'converted_quantity_to_string': converted_quantity_to_string
            }
            return render(request, 'conversion/conversion.html', context)

    else:
        form = ConversionForm()

    context = {'form': form}
    return render(request, 'conversion/conversion.html', context)


def copy_conversion_result(request):
    if request.method == 'POST':
        print(request.POST)
        converted_quantity_to_string = request.POST.get('converted_quantity_to_string', '')
        copy(converted_quantity_to_string)
        context = {"converted_quantity_to_string": converted_quantity_to_string}
        return render(request, template_name="conversion/conversion_copy.html", context=context)
    return render(request, template_name="404.html")

