from django import forms

from MommysCookbookProject.recipe.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # hidden input owner in template
        exclude = ['slug', 'owner', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the recipe title'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter a brief description of the recipe'
            }),
            'ingredients': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter the list of ingredients'
            }),
            'instructions': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter the cooking instructions'
            }),
            'prep_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter preparation time'
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter cooking time'
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter number of servings'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
        }

