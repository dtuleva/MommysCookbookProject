from django import forms

from MommysCookbookProject.home.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("note_text", "is_private")
        widgets = {
            "is_private": forms.RadioSelect(
                choices=[
                    (True, "Add private note"),
                    (False, "Post note on Mommy's Cookbook"),
                ]
            ),
            "note_text": forms.Textarea(
                attrs={
                    "placeholder": 'Add note to this recipe...',
                    "rows": 3
                })
        }