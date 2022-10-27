from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import Course
from rest_framework.decorators import api_view
from rest_framework import status

def get_course(name):
    try:
        return Course.objects.get(name=name)
    except:
        raise Http404
@api_view(["GET"])
def get_all_course(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get(request, name):
    course = get_course(name)
    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def post(request):
    data = request.data
    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete(request, name):
    course = get_course(name)
    course.delete()
    return Response({"message": "delete successfully"}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update(request, name):
    course = get_course(name)
    course.name = request.data["name"]
    course.credit = request.data["credit"]
    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)
