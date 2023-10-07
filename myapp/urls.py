from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('profile',views.profile,name='profile'),
    path('settings',views.settings,name='settings'),
    path('logout',views.logout,name='logout'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('appointment_list',views.appointment_list,name='appointment_list'),
    path('specialities',views.specialities,name='specialities'),
    path('doctor_list',views.doctor_list,name='doctor_list'),
    path('patient_list',views.patient_list,name='patient_list'),
    path('admin_reviews',views.admin_reviews,name='admin_reviews'),
    path('transactions_list',views.transactions_list,name='transactions_list'),
    path('lock_screen',views.lock_screen,name='lock_screen'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('patient_change_password',views.patient_change_password,name='patient_change_password'),
    path('doctor_register',views.doctor_register,name='doctor_register'),
    path('doctor_dashboard',views.doctor_dashboard,name='doctor_dashboard'),
    path('patient_dashboard',views.patient_dashboard,name='patient_dashboard'),
    path('my_patients',views.my_patients,name='my_patients'),
    path('appointments',views.appointments,name='appointments'),
    path('schedule_timings',views.schedule_timings,name='schedule_timings'),
    path('reviews',views.reviews,name='reviews'),
    path('profile_settings',views.profile_settings,name='profile_settings'),
    path('change_password',views.change_password,name='change_password'),
    path('favourites',views.favourites,name='favourites'),
    path('chat',views.chat,name='chat'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    path('booking',views.booking,name='booking'),
    path('patient_profile',views.patient_profile,name='patient_profile'),
    path('doctor_change_password',views.doctor_change_password,name='doctor_change_password'),
    path('doctor_profile_settings',views.doctor_profile_settings,name='doctor_profile_settings'),
    
    

    
]