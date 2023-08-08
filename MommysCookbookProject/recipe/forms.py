from django import forms

from MommysCookbookProject.recipe.models import Recipe


class RecipeCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe

        exclude = ['slug', 'owner', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the recipe title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter a brief description of the recipe'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter the list of ingredients'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter the cooking instructions'
            }),
            'prep_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preparation time in MINUTES'
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cooking time in MINUTES'
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of servings'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
        }

