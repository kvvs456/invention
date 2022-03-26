# Generated by Django 3.2.11 on 2022-03-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exp', models.DecimalField(decimal_places=2, max_digits=4)),
                ('designation', models.CharField(max_length=25)),
            ],
        ),
    ]
