# Generated by Django 5.0.2 on 2024-04-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0004_school_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly_Income_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=255)),
                ('admissionfees', models.IntegerField()),
                ('monthlylyfess', models.IntegerField()),
                ('computerfees', models.IntegerField()),
                ('examfees', models.IntegerField()),
                ('scholarshipawardedto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_Income_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=255)),
                ('admissionfees', models.IntegerField()),
                ('weeklyfess', models.IntegerField()),
                ('computerfees', models.IntegerField()),
                ('examfees', models.IntegerField()),
                ('scholarshipawardedto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Yearly_Income_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=255)),
                ('admissionfees', models.IntegerField()),
                ('yearlyfess', models.IntegerField()),
                ('computerfees', models.IntegerField()),
                ('examfees', models.IntegerField()),
                ('scholarshipawardedto', models.IntegerField()),
            ],
        ),
    ]
