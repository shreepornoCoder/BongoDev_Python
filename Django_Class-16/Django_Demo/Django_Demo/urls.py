from django.contrib import admin
from django.urls import path
from Demo.views import Student_View, Student_Create_View, Student_Get_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', Student_View.as_view(), name='students'),
    path('students/<int:pk>/', Student_Get_View.as_view()), 
    path('students/create/', Student_Create_View.as_view()), 
]
