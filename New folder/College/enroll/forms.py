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

    # name = forms.CharField(widget=forms.TextInput())

    # password = forms.CharField(widget=forms.PasswordInput()) # in this field text will shown as password.

    # hidden = forms.CharField(widget=forms.HiddenInput()) # this will hide this field

    # text_area = forms.CharField(widget=forms.Textarea()) # this will provide text area

    # checkbox = forms.CharField(widget=forms.CheckboxInput()) # give a check box

    file_input = forms.CharField(widget=forms.FileInput()) # Choose a file option

    #######################################################################################

    # css_class = forms.CharField(widget = forms.TextInput(attrs={'class' : 'inputcss', 'id' : 'uniqueid'}))

    #######################################################################################

    # 

    

