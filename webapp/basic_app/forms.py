from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')




class UserProfileInfoForm(forms.ModelForm):
    #profile_pic = forms.FileInput(label='')
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        labels = { 'profile_pic': (''), }
        widgets = {
            'profile_pic': forms.FileInput(attrs={'capture': 'camera','accept':'image/*','style':'visibility:hidden;'},),

        }
