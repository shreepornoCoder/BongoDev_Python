from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from . models import Student
from . serializers import Student_Serializer
from rest_framework.response import Response
from django.http import Http404

# Create your views here.
class Student_View(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

class Student_Create_View(generics.CreateAPIView):
    serializer_class = Student_Serializer

# class Student_Create_View(views.APIView):
#     def post(self, request):
#         serializer = Student_Serializer(data = self.request.data)
#         if serializer.is_valid():
#             serializer.save() 
#         return Response("Data Added")
    
class Student_Get_View(views.APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk=pk)
        serializer = Student_Serializer(student)

        return Response(serializer.data) 