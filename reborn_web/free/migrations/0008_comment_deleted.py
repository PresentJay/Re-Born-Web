# Generated by Django 3.0.2 on 2020-01-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0007_auto_20200130_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='삭제여부'),
        ),
    ]
