from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from useraccount.models import User
from useraccount.models import Employee,User

class HRDepartmentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hr_department = True
        user.save()
        return user


    # def save(self,commit=True):
    #     user = super(HRDepartmentSignUpForm,self).save(commit=False)
    #     user.first_name = cleaned_data['first_name']
    #     user.last_name = cleaned_data['last_name']
    #     user.email = cleaned_data['email']
    #     user.is_hr_department = True
    #     user.save()
    #     return user


class FinanceDepartmentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_fin_department = True
        if commit:
            user.save()
        return user

    # def save(self,commit=True):
    #     user = super().save(commit=False)
    #     user.is_fin_department = True
    #     user.first_name = cleaned_data['first_name']
    #     user.last_name  = cleaned_data['last_name']
    #     user.email = cleaned_data['email']
    #     user.is_fin_department = True
    #     user.save()
    #     return user
    #     