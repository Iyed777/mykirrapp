from django import forms
from django.core.validators import URLValidator

class SubmitURLForm(forms.Form):
    url = forms.CharField(label="Submit URL")


    def clean(self):
        cleaned_data = super(SubmitURLForm, self).clean()
        url = cleaned_data.get('url')

    def clean_url(self):
        url = self.cleaned_data['url']

        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("invalid url")
        return url
