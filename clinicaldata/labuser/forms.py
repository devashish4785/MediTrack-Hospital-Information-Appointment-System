from django import forms
from django.forms import Textarea

from labuser.models import patient,patientclinicaldata
from django.core import validators
#from django.core.exceptions import ValidationError



class patient_form(forms.ModelForm) :
    class Meta:
        model=patient
        fields="__all__"
        widgets={'address':Textarea()}
        """Gender=[('Male','MALE'),('Female','FEMALE')]
        firstname=forms.CharField()
        lastname=forms.CharField()
        age=forms.IntegerField(validators=[validators.MaxValueValidator(150),validators.MinValueValidator(0)])
        gender=forms.CharField(widget=forms.Select(choices=Gender))
        address=forms.CharField(widget=forms.Textarea)
        phone=forms.IntegerField()
        email=forms.EmailField(required=False,label='Enter email address.')"""

        def clean(self):
            super(patient_form,self).clean()
            p=self.cleaned_data['phone']
            print(len(str(p)))
            if len(str(p))!=10:

                print(len(str(p)))
                raise forms.ValidationError('Phone number should have 10 digits.')
            return self.cleaned_data
class clinicdataform(forms.ModelForm):
    class Meta:
        model=patientclinicaldata
        fields='__all__'
