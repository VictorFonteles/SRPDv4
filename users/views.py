from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Professor, Estudante
from . forms import EditTeacherForm, TeacherForm, StudentForm
from django.contrib.auth import authenticate, login, logout




def criarProfessor(request): 
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            context={'form': form}
            return HttpResponseRedirect('/users/login', context)
    else:
        form = TeacherForm()
        
    context={'form': form}
    
    return render(request, 'users/addTeacher.html', context)

#################################################

def loginTeacher(request):
    if request.method == "GET":
        return render(request, 'registration/login.html')
    else:
        email = request.POST.get['email'] 
        password = request.POST.get ['password'] 

        user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/teacher/home")
        
    else:
        return HttpResponseRedirect("/users/teacher/login") 



#################################################  




    

