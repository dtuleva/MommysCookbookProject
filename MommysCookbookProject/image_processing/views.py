from io import BytesIO

import numpy as np
from PIL import Image
from django.core import files

from django.shortcuts import render, get_object_or_404, redirect


from MommysCookbookProject.image_processing.forms import RecipeImageEditForm
from MommysCookbookProject.recipe.models import Recipe



# def image_process(request, recipe_slug):
#     recipe = get_object_or_404(Recipe, slug=recipe_slug)
#     context = {"recipe": recipe}
#     if request.method == 'POST':
#         form = RecipeImageEditForm(request.POST)
#
#         if form.is_valid():
#
#             params = {
#             "brightness": form.cleaned_data['brightness'],
#             "contrast": form.cleaned_data['contrast'],
#             "solarization": form.cleaned_data['solarization'],
#             "greyscale": form.cleaned_data['greyscale']
#             }
#
#             img = Image.open(recipe.image.path)
#
#             img_array = np.array(img)
#             processed_array = image_process_numpy(img_array, params)
#
#             processed_img = Image.fromarray(processed_array.astype('uint8'))
#
#             processed_io = BytesIO()
#             processed_img.save(processed_io, format='PNG')
#
#             recipe.image.save('processed.png', processed_io, save=True)
#
#             context["form"] = form
#
#             return render(request, "image_processing/image_process.html", context=context)
#
#
#     context["form"] = RecipeImageEditForm()
#     return render(request, "image_processing/image_process.html", context=context)




def image_process(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    context = {"recipe": recipe}
    if request.method == 'POST':
        form = RecipeImageEditForm(request.POST)

        if form.is_valid():

            params = {
            "brightness": form.cleaned_data['brightness'],
            "contrast": form.cleaned_data['contrast'],
            "solarization": form.cleaned_data['solarization'],
            "greyscale": form.cleaned_data['greyscale']
            }

            raw_image = recipe.image  # raw if raw


            #raw_image = Image.open(raw_image)
            with Image.open(raw_image) as img:

                raw_image_np = np.array(img)
                processed_array = image_process_numpy(raw_image_np, params)
                processed_image = Image.fromarray(processed_array.astype('uint8'))

                processed_io = BytesIO()
                processed_image.save(processed_io, 'PNG')
                processed_image_file = files.File(processed_io, name=f"processed_{recipe.pk}.png")

                recipe.image = processed_image_file

                recipe.save()

            context["form"] = form

            return render(request, "image_processing/image_process.html", context=context)


    context["form"] = RecipeImageEditForm()
    return render(request, "image_processing/image_process.html", context=context)



def image_process_numpy(img_array, params):
    brightness = params["brightness"]
    contrast = params["contrast"]
    solarization = ["solarization"]
    greyscale = ["greyscale"]

    def limit_range(pixel_value, min_value=0, max_value=255):
        if pixel_value < min_value:
            pixel_value = min_value
        elif pixel_value > max_value:
            pixel_value = max_value
        return pixel_value

    limit_range = np.vectorize(limit_range)
    def custom_map(px):
        if px < 0.15 * 255:
            return 0
        elif px < 0.3 * 255:
            return 0.15
        elif px < 0.7 * 255:
            return px
        elif px < 0.85 * 255:
            return 0.7
        return 1

    custom_map = np.vectorize(custom_map)

    if brightness == 1:
        img_array = img_array // 2
    elif brightness == 3:
        img_array = img_array * 2
        img_array = limit_range(img_array)

    if contrast == 1:
        img_array[img_array == 20] = 255
        img_array[img_array == 235] = 0
    elif contrast == 3:
        img_array[img_array == 20] = 0
        img_array[img_array == 235] = 255

    if greyscale:
        r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
        img_array = 0.299 * r + 0.587 * g + 0.114 * b

    if solarization:
        img_array = custom_map(img_array)

    #print(img_array.shape)

    return img_array

