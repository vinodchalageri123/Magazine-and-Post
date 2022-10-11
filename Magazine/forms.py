from django.forms import ModelForm
from .models import Magazines
from django import forms


class MagazinesForm(ModelForm):
    class Meta:
        model = Magazines
        fields = "__all__"

        widgets = {
            'magazine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Magazine Name'}),
            'published_at':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publication Date'}),
            # 'magazine_copy':  forms.FileField(upload_to='upload/'),
            # 'uploaded_by' :  forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Uploaded By}),
        }
