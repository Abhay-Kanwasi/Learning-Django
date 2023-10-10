from django import forms

class StudentRegistration(forms.Form):

    # different fields

    # name = forms.CharField(initial="Your Name", help_text="You can only enter 30 character maximum")
    # email = forms.EmailField(initial="Your Email")
    # password1 = forms.CharField(initial="Your Password1")
    # password2 = forms.CharField(initial="Your Password2")

    # initial value

    # name = forms.CharField(initial="Your Name")
    # mobile = forms.IntegerField(initial="Your Mobile")
    # email = forms.EmailField(initial="Your Email")
    
    # hidden value

    # key = forms.CharField(widget=forms.HiddenInput())

    name = forms.CharField(label="Name", label_suffix=' ', initial="Your Name", required=False, disabled=True, help_text="Maximum 70 character can be entered")
    
