from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,UserPictureCount

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs ={'class':"form-control",}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
        'username' : forms.TextInput(attrs ={'class':"form-control", 'placeholder' : 'first name'}),
        'email' : forms.EmailInput(attrs ={'class':"form-control", 'placeholder' : 'example@gmail.com'}),



        }




class UserProfileInfoForm(forms.ModelForm):
    #profile_pic = forms.FileInput(label='')
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        labels = { 'profile_pic': (''), }
        widgets = {
            'profile_pic': forms.FileInput(attrs={'capture': 'camera','accept':'image/*','style':'visibility:hidden;'},),

        }

class UserPictureCountForm(forms.ModelForm):
    #profile_pic = forms.FileInput(label='')
    class Meta():
        model = UserPictureCount
        fields = ('picture_count',)
