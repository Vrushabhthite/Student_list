# from django.shortcuts import render, redirect
# from .forms import StudentForm
# from .models import Student


# def add_student_data(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list_student')
#     else:
#         form = StudentForm()
#     return render(request, 'add_student.html', {'form': form})


# def list_students(request):
#     students = Student.objects.all()
#     return render(request, 'list_student.html', {'students': students})


# def update_student(request, id):
#     student = Student.objects.get(id=id)
#     form = StudentForm(instance=student)

#     if request.method == "POST":
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('list_student')

#     return render(request, 'update_student.html', {"form": form})


# def delete_student(request, id):
#     student = Student.objects.get(id=id)
#     student.delete()
#     return redirect('list_student')


from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def add_student_data(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # IMPORTANT
        if form.is_valid():
            form.save()
            return redirect('list_student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


#@login_required(login_url='login')
def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_student.html', {'students': students})

@login_required(login_url='login')

def update_student(request, id):
    student = Student.objects.get(id=id)
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)  # IMPORTANT
        if form.is_valid():
            form.save()
            return redirect('list_student')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {"form": form})

@login_required(login_url='login')
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('list_student')


#API VIEW

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['POST'])
def add_student_api(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':"Student Added"})
    return Response(serializer.errors)



#Auth System

def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('list_student')
        else:
            return render(request,'login.html',{'error':'Invalid Login'})
        
    return render(request,'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')





