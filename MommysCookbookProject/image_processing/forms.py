from django import forms


class RecipeImageEditForm(forms.Form):
    BRIGHTNESS_CHOICES = (
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
    )

    CONTRAST_CHOICES = (
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
    )

    brightness = forms.ChoiceField(choices=BRIGHTNESS_CHOICES, widget=forms.RadioSelect)
    contrast = forms.ChoiceField(choices=CONTRAST_CHOICES, widget=forms.RadioSelect)
    solarization = forms.BooleanField(required=False)
    greyscale = forms.BooleanField(required=False)
