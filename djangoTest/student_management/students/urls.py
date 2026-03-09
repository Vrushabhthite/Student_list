from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.list_students, name='list_student'), 
    path('add/', views.add_student_data, name='add_student'),
   # path('list_student/', views.list_students, name='list_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('api/add-student',views.add_student_api),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    

]
