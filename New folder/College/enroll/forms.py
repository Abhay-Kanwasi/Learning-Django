from django import forms
from django.core import validators
from .models import Staff

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

    # file_input = forms.CharField(widget=forms.FileInput()) # Choose a file option

    #######################################################################################

    # css_class = forms.CharField(widget = forms.TextInput(attrs={'class' : 'inputcss', 'id' : 'uniqueid'}))

    #######################################################################################

    # data = forms.CharField(min_length=5, max_length=30, strip=False)

    # data = forms.CharField(empty_value='Sonam') # in case of empty value error message will not work

    # data = forms.CharField(error_messages={'required':'Please enter your name'})


    # roll_number = forms.IntegerField(min_value=5)
    # agree = forms.BooleanField(label="I agree", label_suffix=" ")

#############################################################################################

    # name = forms.CharField(max_length=5, required=False)
    # # roll_number = forms.CharField(widget=forms.IntegerField())
    # price = forms.DecimalField()
    # rate = forms.FloatField()
    # comment = forms.SlugField()
    # email = forms.EmailField()
    # website = forms.URLField()
    # password = forms.CharField(widget=forms.PasswordInput())
    # description  = forms.CharField(widget=forms.Textarea)
    # feedback = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(attrs={'class': 'somecss1 somecss2', 'id' : 'uniqeid'}))
    # notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols' : 50}))
    # agree = forms.BooleanField(label_suffix='', label="I agree with terms and conditions")

###############################################################################

# validate a specific field

    # name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname)<4:
    #         raise forms.ValidationError("Enter more than or equal 4")
    #     return valname
    
##############################################################################
    
# validate of complete form

    # name = forms.CharField()
    # email = forms.EmailField()
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 4:
    #         raise forms.ValidationError("Name should be more than or equal 4")
    #     valemail = self.cleaned_data['email']
    #     if len(valemail) < 10:
    #         raise forms.ValidationError("Email should be more than or equal 10")

##################################################################################
    # built-in validators

    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    # email = forms.EmailField()

######################################################################################

    # def starts_with_s(value):
    #     if value[0] != 's':
    #         raise forms.ValidationError('Name should starts with s')
    
    # name = forms.CharField(validators=[starts_with_s])
    # email = forms.EmailField()

########################################################################################

    # match two fields

    # name = forms.CharField(error_messages={'required':'Enter your name'})
    # email = forms.EmailField(error_messages={'required':'Enter your email'})
    # password = forms.CharField(widget=forms.PasswordInput)
    # rpassword = forms.CharField(label='Password (agian)', widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd = self.cleaned_data['password']
    #     valrpwd = self.cleaned_data['rpassword']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('Password doesn\'t match')

########################################################################################
    # Save data in form

    student_id = forms.IntegerField()
    student_name = forms.CharField()
    student_email = forms.EmailField()
    student_password = forms.CharField()
    comment = forms.CharField()

class FacultyRegistration(forms.Form):
    fid = forms.CharField(label="Faculty ID")
    name = forms.CharField(label="Faculty Name")
    email = forms.CharField(label="Faculty Email")
    subjects = forms.CharField(label="Faculty Subjects")
    slogan = forms.CharField(label="Faculty Slogan")
    

class StaffRegistrations(forms.ModelForm):
    staff_name = forms.TextInput()
    class Meta:
        model = Staff
        fields = ['staff_id', 'staff_name', 'staff_email', 'staff_subjects', 'staff_slogan']
        labels = {'staff_id':'Your ID','staff_name' : 'Your Name', 'staff_email':"Your Email", 'staff_subjects':"Your Subjects", 'staff_slogan':"Your Slogan"}
        error_messages = {'name':{'required':'Please! enter your name'}}
        widgets = {'staff_id':forms.PasswordInput, 'staff_name':forms.TextInput(attrs={'placeholder': 'Enter your name'}), 'staff_email':forms.TextInput(attrs={'placeholder': 'Enter your email'}), 'staff_slogan':forms.TextInput(attrs={'placeholder': 'Enter your slogan'}), 'staff_id':forms.TextInput(attrs={'placeholder': 'Enter your id'}), 'staff_subjects':forms.Textarea(attrs={'placeholder': 'Enter your subjects'})}