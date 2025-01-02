from django.contrib import admin
from django.urls import path
from Demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.Student_View.as_view(), name='students'),
    path('students/<int:pk>/', views.Student_Get_View.as_view()), 
    path('students/create/', views.Student_Create_View.as_view()), 
    path('students/update/<int:pk>/', views.Student_Update.as_view()), 
]
