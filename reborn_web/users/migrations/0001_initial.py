# Generated by Django 3.0.1 on 2019-12-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='이메일')),
                ('hp', models.IntegerField(null=True, unique=True, verbose_name='핸드폰번호')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='이름')),
                ('student_id', models.IntegerField(null=True, unique=True, verbose_name='학번')),
                ('grade', models.CharField(choices=[('1', '1학년'), ('2', '2학년'), ('3', '3학년'), ('4', '4학년'), ('졸업', '졸업생')], max_length=18, null=True, verbose_name='학년')),
                ('level', models.CharField(choices=[('1', '1_EveryOne'), ('2', '2_Certified Member'), ('3', '3_Manager'), ('4', '4_Supervisor')], default=1, max_length=18, verbose_name='등급')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': '회원목록',
            },
        ),
    ]
