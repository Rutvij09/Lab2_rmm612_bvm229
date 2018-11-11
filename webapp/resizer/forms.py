from django import forms

class ImageUpload(forms.Form):
    image_field = forms.FileField(
        label='Click to browse computer',
        help_text='Only jpeg and png allowed: ')
