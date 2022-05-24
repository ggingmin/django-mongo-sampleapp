from djongo import models


class Student(models.Model):
    STUDENT_TYPE = (
        ("UNDERGRADUATE", "Undergraduate"),
        ("GRADUATE", "Graduate"),
        ("EXCHANGE", "Exchange")
    )

    _id = models.ObjectIdField()
    student_num = models.IntegerField()
    name = models.CharField(max_length=30)
    college = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    student_type = models.CharField(max_length=20, choices=STUDENT_TYPE)
    graduated = models.BooleanField(default=False)
    entrance_date = models.DateField()

    class Meta:
        db_table = "students"

    def __str__(self):
        return f"${self.student_num}, ${self.name}"

