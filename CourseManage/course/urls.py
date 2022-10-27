from django.urls import path, include
from .views import CourseList, AddCourse
from course import views

urlpatterns = [
    path("course-list/", views.CourseList.as_view()),
    path("course/", AddCourse),
]