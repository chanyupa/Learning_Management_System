# Generated by Django 5.0.2 on 2024-04-25 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0005_monthly_income_table_weekly_income_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthly_income_table',
            old_name='monthlylyfess',
            new_name='monthlyfess',
        ),
    ]
