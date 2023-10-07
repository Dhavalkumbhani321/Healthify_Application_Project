from django import forms
from django.forms import ModelForm

from .models import *


class DoctorForm(ModelForm):
	class Meta:
		model = Doctor
		fields = ('user', 'image', 'first_name', 'second_name', 'title', 'd_o_b', 'gender', 'biography', 
			'phone_no', 'email', 'address_line1', 'address_line2', 'country', 'county', 'town', 'pricing', 
			'services', 'specialization', 'clinic', 'clinic_address', 'speciality')
  
  
class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = ('user', 'image', 'first_name', 'second_name', 'd_o_b', 'gender', 'blood_group', 'phone_no', 
			'email', 'street_lane', 'country', 'county', 'town')
  