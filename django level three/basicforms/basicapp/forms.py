from django import forms
from django.core import validators


# Method 3: Making our own custom validators
def check_for_v(value):     # Checks for name starts with v
    if value[0].lower() != 'v':
        raise forms.ValidationError("Name needs to start with v")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    # Method 2 : Using Built in validation (Recommended)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


    # Method 1: Using clean method to validate form
    def clean_botcatcher(self):     # whatever field written after claen will be searched on above fields
        botcatcher = self.cleaned_data['botcatcher']       # we are catching whatever botcatcher is putting value in this hidden field
        if len(botcatcher) > 0:
            raise forms.ValidationError