from django import forms


class StudentForms(forms.Form):
    fname = forms.CharField(label="Your First Name", max_length=30)
    lname = forms.CharField(label="Your Last Name", max_length=30)
    eml = forms.EmailField(label="Your Email", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
