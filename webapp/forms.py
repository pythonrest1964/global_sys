from django import  forms

class RegistrationForm(forms.Form):
    # firstname = forms.CharField(max_length=100)
    # lastname = forms.CharField(max_length=100)
    # username = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # mobile = forms.IntegerField()
    # email = forms.EmailField(max_length=100)
    firstname=forms.CharField(
        label='Enter UserName',
        widget=forms.TextInput(
            attrs={
                'placeholder':'FirstName',
                'class':'form-control'
            }
        )
    )
    lastname=forms.CharField(
        label='Enter LastName',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter LastName',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label='Enter UserName',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter Username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'enter password',
                'class':'form-control'
            }
        )
    )
    mobile=forms.CharField(
        label='enter mobile number',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'enter mobile number',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label='enter your email',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'enter email',
                'class':'form-control'
            }
        )
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label='enter your username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='enter your password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'enter password',
                'class':'form-control'
            }
        )
    )
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                'class':'form-control',
            }
        )
    )
    rating = forms.CharField(
        label='Enter your rating',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'your rating',
                'class': 'form-control',
            }
        )
    )
    feedback = forms.CharField(
        label='Enter your feedback',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'enter your feedback',
                'class': 'form-control',
            }
        )
    )
from multiselectfield import MultiSelectFormField
class ContactForm(forms.Form):
    name=forms.CharField(
        label='enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    mobile=forms.IntegerField(
        label='enter your mobileno',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    email=forms.EmailField(
        label='enter our email',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'enter email',
                'class':'form-control'
            }
        )
    )
    COURSES_CHOICES = (
        ('Python', 'PYTHON'),
        ('Django', 'DJANGO'),
        ('Ui', 'UI'),
        ('RestApi', 'RESTAPI')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES,label='select your course',
                                   )

    TRAINER_CHOICES = (
        ('Sai', 'SAI'),
        ('Nani', 'NANI'),
        ('Satya', 'SATYA')
    )
    trainers = MultiSelectFormField(choices=TRAINER_CHOICES,label='select required trainers')

    BRANCHES_CHOICES = (
        ('Hyd', 'HYDERABAD'),
        ('Pune', 'PUNE'),
        ('Bang', 'BANGALORE')
    )
    branches = MultiSelectFormField(choices=BRANCHES_CHOICES,label='select required branch')

    date=forms.DateField(
        widget=forms.SelectDateWidget(),
        label='Enter the date:'
    )
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=GENDER_CHOICES,label='select your gender'
    )