from django.urls import path, include
from .views import get, get_all_course, post, delete, update

urlpatterns = [
    path("course/", get_all_course, name="courses"),
    path("course/add/", post, name="add-course"),
    path("course/<str:name>/", get, name="course"),
    path("course/delete/<str:name>/", delete, name="delete-course"),
    path("course/update/<str:name>/", update, name="update-course")
]