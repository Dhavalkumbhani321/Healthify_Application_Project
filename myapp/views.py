from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


def index(request):
    return render(request,'index.html')
    
    
    


def base(request):
    return render(request,'base.html')


def profile(request):
	return render(request, 'profile.html')

def settings(request):
    return render(request,'settings.html')


def logout(request):
    del request.session['email']
    return redirect('register')


def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def appointment_list(request):
    return render(request,'appointment_list.html')



def specialities(request):
    return render(request,'specialities.html')



def check_doctor(user):
	group = user.groups.get()
	return group.name=='doctors_group'


def check_settings(user):
	profile = Doctor.objects.filter(user=user.id)
	return profile.count()>=1



@login_required(login_url='/login/')
@user_passes_test(check_doctor, login_url='/login/')
@user_passes_test(check_settings, login_url='/doctors/profile-settings/')
def doctor_dashboard(request):
	profile = Doctor.objects.get(user=request.user.id)
	appointments = Appointment.objects.filter(doctor=profile.id)
	upcoming_appointments = appointments.filter(booking_date__gte=dt.date.today())
	today_appointments = appointments.filter(status='ACCEPTTED', booking_date__date=dt.date.today())
	my_patients = []
	for appointment in appointments:
		if appointment.patient not in my_patients:
			my_patients += [appointment.patient]
	return render(request, 'doctors/doctor-dashboard.html', {"profile": profile, "appointments": appointments,
		"upcoming_appointments": upcoming_appointments, "today_appointments": today_appointments, 
		"total_patients": len(my_patients)})		
    
   

def my_patients(request):
    return render(request,'my_patients.html')

def patient_dashboard(request):
    return render(request,'patient_dashboard.html')


def doctor_list(request):
    return render(request,'doctor_list.html')



def patient_list(request):
    return render(request,'patient_list.html')


def admin_reviews(request):
    return render(request,'admin_reviews.html')


def transactions_list(request):
    return render(request,'transactions_list.html')





def lock_screen(request):
    return render(request,'lock_screen.html')

def login(request):
    try:
        user = Dctor_register.objects.get(email=request.session['email'])
        return render(request,'admin_dashboard.html',{'user':user})
    except:
        if request.method == 'POST':
            try:
                user = Doctor_register.objects.get(email=request.POST['email'])
                if request.POST['password'] == user.password:
                    request.session['email'] = user.email

                    return render(request,'admin_dashboard.html',{'user':user})
                return render(request,'login.html',{'msg':'Incorrect Password'})
            except:
                return render(request,'register.html',{'msg':'Account does not exist please register first!!'})
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                Doctor_register.objects.get(email=request.POST['email'])
                return render(request,'login.html',{'msg':'Account alreadt exist please login'})
            except:
               Dctor_register.objects.objects.create(
                    fname = request.POST['name'],
                    email = request.POST['email'],
                    password = request.POST['password']
                )

            return render(request,'login.html',{'msg':'Account created go and login'})
            
        return render(request,'register.html',{'msg':'Both pass are not same'})


    return render(request,'register.html')


def forgot_password(request):
    if request.method=="POST":
        email=request.POST.get('email')
        otp=otpGen()
        token=tokenGen()
        # try:
        user=User.objects.get(email=email)
        if user is not None:
            temp_user=Temp_User.objects.create(email=email, otp=otp, token=token)
            return render(request, 'login-with-otp.html', {'token':token})
        return redirect('/')
        # except Exception as E:
        return redirect('/')
    return render(request, 'forgot_password.html')
    


def patient_change_password(request):
	patient = Patient.objects.get(user=request.user.id)
	if request.is_ajax():
		usr = request.user
		if usr.check_password(request.POST['old_password']):
			if request.POST['new_password'] == request.POST['confirm_password']:
				if not request.POST['new_password'] == request.POST['old_password']:
					usr.set_password(request.POST['new_password'])
					usr.save()
					logout(request)
					redirect = '../../login/'
					return JsonResponse({"success": "Password Updated.", "redirect": redirect}, status=200)
				else:
					return JsonResponse({"error": "The Password Has not Changed"}, status=200)
			else:
				return JsonResponse({"error": "Confirm and New Password don't Match"}, status=200)
		else:
			return JsonResponse({"error": "Incorrect password"}, status=200)
	else:
		return render(request, 'patients_change_password.html', {'profile': patient})



def doctor_register(request):
    if request.method=="POST":
        try:
            User.object.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
		
        except: 
            if request.POST['password']== request.POST['cpassword']:
	            User.objects.create(
			
					fname=request.POST['fname'],
					email=request.POST['email'],
					password=request.POST['password'],)
            msg='User signup Successfully'
            return render(request,'login.html',{'msg':msg})
        else:
            msg ="password and confirm password are not match"	
            return render(request,'register.html',{'msg':msg})
    else:
            return render(request,'register.html')	



def get_user(self):
		usr = self.user
		group = usr.groups.get()
		if group.name=='patients_group':
			patient = Patient.objects.get(user=usr.id)
			return patient
		elif group.name=='doctors_group':
			doctor = Doctor.objects.get(user=usr.id)
			return doctor
		else:
			return user


def get_group(self):
    usr = self.user
    group = usr.groups.get()
    return group.name


def appointments(request):
    return render(request,'appointments.html')


def schedule_timings(request):
    return render(request,'schedule_timings.html')


def reviews(request):
	doctor = Doctor.objects.get(user=request.user.id)
	reviews = Review.objects.filter(appointment__doctor=doctor.id)
	return render(request, 'reviews.html', {'profile': doctor, 'reviews': reviews})


def profile_settings(request):
#data = {'user': request.user.id, 'first_name': request.user.first_name, 'email': request.user.email}
	if request.method == 'POST':
		if int(request.POST['user']) == request.user.id:
			try:
				a = Patient.objects.get(user=request.user.id)
				f = PatientForm(request.POST, request.FILES, instance=a)
				f.save()
				return HttpResponseRedirect('../../patients/')
			except Exception:
				form = PatientForm(request.POST, request.FILES)
				if form.is_valid():
					form.save()
					user=request.user
					user.last_name = request.POST['second_name']
					user.first_name = request.POST['first_name']
					user.email = request.POST['email']
					user.save()
					return HttpResponseRedirect('../../patients/')
				else:
					return HttpResponse(form.errors)
					# return render(request, 'appointments/profile-settings.html', {'form': form})
		else:
			return HttpResponse("form.errors")
	else:
		profile = None
		form = None
		try:
			profile = Patient.objects.get(user=request.user.id)
			form = PatientForm(instance=profile)
		except Exception:
			profile = request.user
			form = PatientForm()
		return render(request, 'profile_settings.html', {"profile": profile, "form": form})


def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if user.usertype=="customer":
        if request.method=="POST":
            if user.password==request.POST['old_password']:
                if request.POST['new_password']==request.POST['cnew_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    return redirect('logout')
                else:
                    msg="New password and confirm new password does not marched"
                    return render(request,'change_password.html',{'msg':msg})
            else:
                    msg="Old password is incorrect"
                    return render(request,'change_password.html',{'msg':msg})
        else:
                return render(request,'change_password.html')
    else:
        if request.method=="POST":
            if user.password==request.POST['old_password']:
                if request.POST['new_password']==request.POST['cnew_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    return redirect('logout')
                else:
                    msg="New password and confirm New password does not match"
                    return render(request,'artist_change_password.html',{'msg':msg})
            else:
                msg="Old passowrd is incorrect"
                return render(request,'artist_change_password.html',{'msg': msg})
        else:
            return render(request,'change_password.html')
                    
    



def favourites(request):
    return render(request,'favourites.html')

def chat(request):
    return render(request,'chat.html')


def doctor_profile(request):
    doctor = Doctor.objects.get(id=doctor)
    edu = Education.objects.filter(doctor=doctor) 
    exp = Experience.objects.filter(doctor=doctor)
    awd = Award.objects.filter(doctor=doctor)
    mbr = Membership.objects.filter(doctor=doctor)
    reg = Registration.objects.filter(doctor=doctor)
    reviews = Review.objects.filter(appointment__doctor=doctor)
    schedule = DoctorSchedule.objects.filter(doctor=doctor)
    profile = get_profile(request.user)
    return render(request, 'doctor_profile.html', {"doctor": doctor, "education": edu, 
		"experience": exp, "award": awd, "membership": mbr, "registration": reg, "profile": profile, 
		"reviews": reviews, "schedule": schedule})


def booking(request):
    return render(request,'booking.html')

def patient_profile(request):
    doctor = Doctor.objects.get(user=request.user.id)
    patient = Patient.objects.get(id=patient_id)
    appointments = Appointment.objects.filter(patient=patient_id, doctor=doctor.id)
    prescriptions = Prescription.objects.filter(patient=patient_id) 
    records = MedicalRecord.objects.filter(patient=patient_id) 
    invoices = Invoice.objects.filter(patient=patient_id, doctor=doctor.id)
    return render(request, 'patient-profile.html', {'profile': doctor, 'patient': patient, 
		'last_appointments': appointments, 'prescriptions': prescriptions, 'records': records, 
		'invoices': invoices})

    



def doctor_change_password(request):
    doctor = Doctor.objects.get(user=request.user.id)
    if request.is_ajax():
        usr = request.user
        if usr.check_password(request.POST['old_pswd']):
            if request.POST['new_pswd'] == request.POST['cfm_pswd']:
                if not request.POST['new_pswd'] == request.POST['old_pswd']:
                    usr.set_password(request.POST['new_pswd'])
                    usr.save()
                    logout(request)
                    redirect = '../../login/'
                    return JsonResponse({"success": "Social Sites Updated.", "redirect": redirect}, status=200)
                else:
                    return JsonResponse({"error": "The Password Has not Changed"}, status=200)
            else:
                    return JsonResponse({"error": "Confirm and New Password don't Match"}, status=200)
        else:
            return JsonResponse({"error": "Incorrect password"}, status=200)
    else:
            return render(request, 'doctor_change_password.html', {'profile': doctor})
    



def doctor_profile_settings(request):
    if request.method == 'POST':
        if int(request.POST['user']) == request.user.id:
            try:
                a = Doctor.objects.get(user=request.user.id)
                f = DoctorForm(request.POST, request.FILES, instance=a)
                f.save()
                user=request.user
                user.last_name = request.POST['second_name']
                user.first_name = request.POST['first_name']
                user.email = request.POST['email']
                user.save()
                return HttpResponseRedirect('../profile/settings-page2/')
            except Exception:
                form = DoctorForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    user=request.user
                    user.last_name = request.POST['second_name']
                    user.first_name = request.POST['first_name']
                    user.email = request.POST['email']
                    user.save()
                    return HttpResponseRedirect('../profile/settings-page2/')
                else:
                    return HttpResponse(form.errors)
                # return render(request, 'appointments/profile-settings.html', {'form': form})
            else:
                    return HttpResponse("form.errors")
        else:
            profile = None
            form = None
            try:
                profile = Doctor.objects.get(user=request.user.id)
                form = DoctorForm(instance=profile)
            except Exception:
                form = DoctorForm()
                specialities = Speciality.objects.all()
                return render(request, 'doctor_profile_settings.html', {'specialities': specialities, 
			'profile': profile, 'form': form})
    



