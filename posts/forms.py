from dataclasses import fields
from django import forms
from posts.models import PostModel

class SeesForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['sees']