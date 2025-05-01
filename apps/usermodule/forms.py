from django import forms
from .models import Student, Student2, Photo

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
