# Generated by Django 4.0.4 on 2022-05-24 08:23

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('student_num', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('student_type', models.CharField(choices=[('UNDERGRADUATE', 'Undergraduate'), ('GRADUATE', 'Graduate'), ('EXCHANGE', 'Exchange')], max_length=20)),
                ('graduated', models.BooleanField(default=False)),
                ('entrance_date', models.DateField()),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]