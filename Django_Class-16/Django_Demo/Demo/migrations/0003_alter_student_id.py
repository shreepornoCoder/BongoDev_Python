# Generated by Django 5.0.6 on 2025-01-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0002_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]