from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField('Profile Image', upload_to='Image/Admin', 
	max_length=500, default='dummy.png')
	first_name = models.CharField('First Name', max_length=50)
	second_name =  models.CharField('Second Name', max_length=50)
	d_o_b = models.DateField('Date of Birth')
	phone_no = models.CharField('Phone Number', max_length=50)
	email = models.EmailField('Email', max_length=250)
	address_line = models.CharField('Address Line', max_length=200, blank=True)
	country = models.CharField('Country', max_length=100, blank=True)
	county = models.CharField('County', max_length=100, blank=True)
	town = models.CharField('Town', max_length=100, blank=True)

    


# user, image, first_name, second_name, d_o_b, phone_no, email, address_line, country, county, town

	def __str__(self):
		return self.first_name+" "+self.second_name

class Dctor_register(models.Model):
    fname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

def __str__(self):
        return self.fname
    
    
    
class Patient_register(models.Model):
    fname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

def __str__(self):
        return self.fname
    



class Doctor(models.Model):
	"""docstring for Doctor"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField('Profile Image', upload_to='Image/Doctors', 
		max_length=500, default='dummy.png')
	first_name = models.CharField('First Name', max_length=50)
	second_name =  models.CharField('Second Name', max_length=50)
	title = models.CharField('Title', max_length=200, default='Dr.')
	phone_no = models.CharField('Phone Number', max_length=50)
	email = models.EmailField('Email', max_length=250)
	gender = models.CharField('Gender', max_length=10)
	d_o_b = models.DateField('Date of Birth', blank=True)
	biography = models.CharField('Biography', max_length=1000, blank=True)
	address_line1 = models.CharField('Address Line 1', max_length=200, blank=True)
	address_line2 = models.CharField('Address Line 2', max_length=200, blank=True)
	country = models.CharField('Country', max_length=100, blank=True)
	county = models.CharField('County', max_length=100, blank=True)
	town = models.CharField('Town', max_length=100, blank=True)
	pricing =  models.FloatField('Amount', default=0.00)
	services = models.CharField('Services', max_length=1000, blank=True)
	specialization = models.CharField('Specialization', max_length=1000, blank=True)
	clinic = models.CharField('Clinic', max_length=100, blank=True)
	clinic_address = models.CharField('Clinic Address', max_length=100, blank=True)
	''' user, image, first_name, second_name, title, phone_no, email, gender, d_o_b, biography,
	address_line1, address_line2, country, county, town, pricing, services, specialization, clinic, 
	clinic_address, speciality'''
	def full_name(self):
		return self.title + " " + self.first_name + " " + self.second_name






class Registration(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	year = models.DateField('Year')		
	registration = models.CharField('Registration', max_length=50)
 
 
 
class Patient(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField('Profile Image', upload_to='Image/Patient/Profile/', 
		max_length=500, default='dummy.png')
	first_name = models.CharField('First Name', max_length=50)
	second_name = models.CharField('Second Name', max_length=50)
	d_o_b = models.DateField('Date Of Birth')
	gender = models.CharField('Gender', max_length=10)
	email = models.CharField('Email', max_length=50)
	phone_no = models.CharField('Phone Number', max_length=20)
	blood_group = models.CharField('Blood Group', max_length=5)
	country = models.CharField('Country', max_length=50)
	county = models.CharField('County', max_length=50)
	town = models.CharField('Town', max_length=50)
	street_lane = models.CharField('Street/Lane', max_length=50)
	
	def __str__(self):
		return self.first_name +' '+self.second_name 




class Appointment(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	purpose = models.CharField('Purpose', max_length=50)
	category = models.CharField('Type', max_length=50)
	amount = models.FloatField('Amount', default=0.00)
	status = models.CharField('Status', max_length=50)
	date = models.DateTimeField('Appointment Date', auto_now_add=True)
	booking_date = models.DateTimeField('Booking Date')
	follow_up_date = models.DateTimeField('Follow Up', null=True)
	# doctor, patient, purpose, category, amount, status, booking_date, follow_up_date

	def __str__(self):
		return self.apt_purpose





class Temp_User(models.Model):
    username=models.CharField(max_length=100, blank=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=40, blank=True)
    otp=models.IntegerField()
    token=models.CharField(max_length=65)
    time=models.TimeField(auto_now_add=True)
    
    
    
    
class Review(models.Model):
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, blank=True)
	date = models.DateTimeField('Review Date', auto_now_add=True)
	rate = models.IntegerField('Rate')
	recommend = models.BooleanField('Recommend', default=False)
	text = models.CharField('Review Title', max_length=150, blank=True)
	# appointment, date, rate, recommend, text
 
 
 
 
 
 
 
 
 
class Education(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	degree = models.CharField('Degree', max_length=50)
	institute = models.CharField('College/Institute', max_length=50)
	y_o_c = models.DateField('Year of Completion')
 
 
 
 
 
class Experience(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	hospital_name = models.CharField('Hospital Name', max_length=50)
	start = models.DateField('From')
	finish = models.DateField('To', blank=True)
	designation = models.CharField('Designation', max_length=50)
	# doctor, hospital_name, start, finish, designation


class Award(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	award = models.CharField('Award', max_length=50)
	year  = models.DateField('Year')
	# doctor, award, year


class Membership(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	membership = models.CharField('Membership', max_length=50)
	# doctor, membership


class Registration(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	year = models.DateField('Year')		
	registration = models.CharField('Registration', max_length=50)
	# doctor, year, registration