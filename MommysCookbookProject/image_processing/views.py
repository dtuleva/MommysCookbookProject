from io import BytesIO

import numpy as np
from PIL import Image

from django.shortcuts import render, get_object_or_404, redirect


from MommysCookbookProject.image_processing.forms import RecipeImageEditForm
from MommysCookbookProject.recipe.models import Recipe



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

            img = Image.open(recipe.image.path)

            img_array = np.array(img)
            processed_array = image_process_numpy(img_array, params)

            processed_img = Image.fromarray(processed_array.astype('uint8'))

            processed_io = BytesIO()
            processed_img.save(processed_io, format='PNG')

            recipe.image.save('processed.png', processed_io, save=True)

            context["form"] = form

            return render(request, "image_processing/image_process.html", context=context)


    context["form"] = RecipeImageEditForm()
    return render(request, "image_processing/image_process.html", context=context)



def image_process_numpy(img_array, params):
    brightness_factor = params["brightness"]
    print(brightness_factor)
    if brightness_factor == 1:
        img_array = img_array // 2
    elif brightness_factor == 3:
        img_array = img_array * 2 # limit to 255



    print(img_array.shape)

    return img_array

