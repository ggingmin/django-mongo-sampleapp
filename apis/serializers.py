from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            "_id",
            "student_num",
            "name",
            "college",
            "major",
            "student_type",
            "graduated",
            "entrance_date"
        )
