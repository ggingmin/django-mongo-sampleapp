from django.urls import path

from .views import StudentAPIView, StudentAPIDetailView

urlpatterns = [
    path("<int:pk>/", StudentAPIDetailView.as_view(), name="student_detail"),
    path("", StudentAPIView.as_view(), name="student_list"),
]