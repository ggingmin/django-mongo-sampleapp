from rest_framework import generics
from rest_framework.response import Response
from bson import ObjectId

from students.models import Student
from .serializers import StudentSerializer


class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StudentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        self.kwargs["pk"] = ObjectId(self.kwargs["pk"])
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
