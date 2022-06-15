from rest_framework import generics
from django.shortcuts import render
from .models import *
from .serializer import *


class createlist(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class readlist(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class updatelist(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class deletelist(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Create your views here.
# funtion based :-
# @csrf_exempt
# def ToDoAPI(request):
#     if request.method == 'GET':
#         ToDo = ToDo.objects.all()
#         ToDo_serializer = ToDoSerializer(ToDo, many=True)
#         return JsonResponse(ToDo_serializer.data, safe=False)
#     elif request.method == 'POST':
#         ToDo_data = JSONParser().parse(request)
#         ToDo_serializer = ToDoSerializer(data=ToDo_data)
#         if ToDo_serializer.is_valid:
#             ToDo_serializer.save()
#             return JsonResponse('added sucessfully', safe=False)
#         return JsonResponse('failed to add', safe=False)

#     elif request.method == 'PUT':
#         ToDo_data = JSONParser().parse(request)
#         ToDo = ToDo.objects.all(ToDoId=ToDo_data['ToDoId'])
#         ToDo_serializer = ToDoSerializer(ToDo, data=ToDo_data)
#         if ToDo_serializer.is_valid:
#             ToDo_serializer.save()
#             return JsonResponse('Updated sucessfully', safe=False)
#         return JsonResponse('failed to add', safe=False)

#     elif request.method == 'DELETE':
#         ToDo = ToDo.objects.all(ToDoId=id)
#         ToDo.delete()
#         return JsonResponse('DElete successfully', safe=False)
