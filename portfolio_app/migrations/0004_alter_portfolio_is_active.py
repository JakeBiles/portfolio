# Generated by Django 4.2 on 2024-03-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_project_portfolio_student_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
