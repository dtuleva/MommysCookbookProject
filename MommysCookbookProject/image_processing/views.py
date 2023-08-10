from io import BytesIO

import numpy as np
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from MommysCookbookProject.recipe.models import Recipe


def image_process(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    context = {"recipe": recipe}
    if request.method == 'POST':
        if recipe.image:
            # Open the image using Pillow
            img = Image.open(recipe.image_raw.path)

            # Convert the image to a NumPy array and apply the operation
            img_array = np.array(img)
            processed_array = img_array // 2  # Adjust this operation as needed

            # Create a new Pillow Image from the processed array
            processed_img = Image.fromarray(processed_array.astype('uint8'))

            # Save the processed image to a BytesIO object
            processed_io = BytesIO()
            processed_img.save(processed_io, format='PNG')

            # Save the processed image back to the database
            recipe.image.save('processed.png', processed_io, save=True)

            return render(request, "image_processing/image_process.html", context=context)

    # If not a POST request or if no image processing is needed,
    # return the template with the recipe as context
    return render(request, "image_processing/image_process.html", context=context)
