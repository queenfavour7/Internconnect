from django import forms
from .models import Intern, department

class InternForm(forms.ModelForm):
    class Meta :
        model = Intern
        fields = ['department','name','phone_number','created_on','is_active']
        wingets = {
            'department':forms.Select(
                attrs= {
                    'class':'form-control'
                }
            ),
            'name':forms.TextInput(
                attrs={
                    'class':'Intern_name',
                    'placeholder':'your name please',
                    'title':'Intern_name',
                }
            ),
            'phone_number':forms.TextInput(
                attrs= {
                    'class':'Intern_phone_number',
                    'placeholder':'please insert your phone number for easy identification',
                    'title':'Intern_phone_number'
                }
            ),
           'created_on':forms.TimeField(
            attrs= {
                    'class':'form-control'
                }
            ),
            'is_active':forms.Select(
                attrs={
                    'class':'search'
                }
            ),
        }

class departmentForm(forms.ModelForm):
    class Meta:
        model = department
        field = ['course','description','slug']
        wingets = {
            'course':forms.TextInput(
                attrs={
                    'class':'department_title',
                    'placeholder':'your course of study please',
                    'title':'department_title'
                }
            ),
             'description':forms.TextInput(
                attrs={
                    'class':'department_title',
                    'placeholder':'your course of study please',
                    'title':'department_title'
                }
            ),
            'slug':forms.TextInput(
                attrs={
                    'class':'department_title'
                }
            ),
        }