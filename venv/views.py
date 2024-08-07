from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404 

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Teacher , Student , Subject

## login required page is added before the view or page that is needed to
#  be logged in before open or reach it
@login_required(login_url='/login/')
def index(request):
    if request.method=="GET":
      teachersList=Teacher.objects.all()
      num_students= Student.objects.count()
      print(teachersList)
      try:
         
       visitTime = request.session('visitTime')  
       print('try',visitTime)
      except:       
       request.session('visitTime') =0
       visitTime = request.session('visitTime')

      visitTime +=1
      request.session('visitTime') =visitTime
      context={
         'visitTime':visitTime,
         'teachersList':teachersList,
         'num_students':num_students,
      }
      print('visitTime',visitTime)
      return render(request,'index.html')


 
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
          print(username,password)
          response =redirect('/index/')
          return render(response)
        else:
          print('Invalid credintial')
          return render(request,'login.html')    
         
    elif request.method=='GET':
       
     return render (request,'login.html')


def register(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        password2 = request.POST.get('password2')
        userData = {'username':username,'email': email, 'password1':password, 'password2':password2}
        if password!= password2:
           print('passwords do not match')
           return render (request,'register.html',{'error massage':'passwords do not match'})
        form = RegistrationForm(data=userData)
        print(form.errors)
        if form.is_valid():
           form.save()
           response = redirect('/login/')
           return response
        else:
           return render(request,'register.html',{'form':form})

        print(username,password,email,password2
              )
        print('from register')
   return render(request, 'register.html')   
  

def logout_page(request):
   logout(request)
   return redirect('/login')



def subject_detail(request,pk):
   subject = get_object_or_404(Teacher,pk=pk)
   return render('subject_detail.html',{'subject' : subject})
