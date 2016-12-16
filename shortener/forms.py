from django import forms

from .validators import validate_url, validate_dot_com

class SubmitURLForm(forms.Form):
    url = forms.CharField(label="Submit URL", validators=[validate_url, validate_dot_com])

"""
    def clean(self):
        cleaned_data = super(SubmitURLForm, self).clean()
        url = cleaned_data.get('url')

    def clean_url(self):
        url = self.cleaned_data['url']
"""
