
from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index, name='index'),
    path('login/',login_page,name='login'),
    path('register/', register, name='register' ),
    path('logout/', logout_page, name='logout'),
    ##path('teacher/', teacher_page , name='teacher' ),
    ##path('student/', student_page , name='student'),
    ##path('subject/', subject_page , name='subject'),
    ##path('about/', about_page ,name='about'),


]