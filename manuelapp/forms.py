from django import forms
from django.core import validators


def check_value_m(value):
    if value[0].lower() != 'm':
        raise forms.ValidationError('Your name does not start with M')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_value_m],)
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write something here'}))
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)],
                                 error_messages={'max_length': 'Gotcha Bot!'},)

    def clean(self):
        all_data_clean = super().clean()
        email = all_data_clean['email']
        verify_email = all_data_clean['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Sorry, your email does not match')




