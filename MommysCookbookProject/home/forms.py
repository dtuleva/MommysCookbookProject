from django import forms

from MommysCookbookProject.home.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note_text',)
        widgets = {
            'note_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                })
        }