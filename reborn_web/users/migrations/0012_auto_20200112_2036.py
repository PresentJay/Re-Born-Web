# Generated by Django 3.0.1 on 2020-01-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200112_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=32, null=True, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.IntegerField(null=True, verbose_name='학번'),
        ),
    ]
