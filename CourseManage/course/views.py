from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import Course
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

def get_course(name):
    try:
        course = Course.objects.get(name=name)
        return course
    except:
        return Response({"message": "Course not exist!"}, status=status.HTTP_404_NOT_FOUND)


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
    all_course = Course.objects.all()
    for course in all_course:
        if data["name"] == course.name:
            return Response({"message": "Course already exist!"}, status=status.HTTP_400_BAD_REQUEST)
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


@api_view(["POST"])
def update(request, name):
    Course.objects.filter(name=name).update(name=request.data["name"], credit=request.data["credit"])
    return Response({"message": "Successful updated"}, status=status.HTTP_200_OK)
