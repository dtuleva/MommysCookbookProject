from django import forms

from MommysCookbookProject.conversion.models import Measurement, Ingredient


class ConversionForm(forms.Form):
    quantity = forms.FloatField(label='Quantity', min_value=0)
    source_unit = forms.ModelChoiceField(queryset=Measurement.objects.all(), label='Source Unit')
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), label='Ingredient', required=False)
    target_unit = forms.ModelChoiceField(queryset=Measurement.objects.all(), label='Target Unit')

    def clean(self):
        cleaned_data = super().clean()
        source_unit = cleaned_data.get('source_unit')
        target_unit = cleaned_data.get('target_unit')
        ingredient = cleaned_data.get('ingredient')

        if source_unit and target_unit and not ingredient:
            if source_unit.volume_unit and not target_unit.volume_unit:
                self.add_error('ingredient', 'Ingredient field is required for the selected source unit.')
            if not source_unit.volume_unit and target_unit.volume_unit:
                self.add_error('ingredient', 'Ingredient field is required for the selected target unit.')

        return cleaned_data