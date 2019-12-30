from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL")
    return value

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self.clean)
    #     print(cleaned_data)
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    
    def clean_url(self):
        url = self.cleaned_data['url']
        
        # url_validator = URLValidator()
        # try:
        #     url_validator(url)
        # except:
        #     raise forms.ValidationError("Invalid URL provided")
        return url