# Generated by Django 2.2.10 on 2020-02-29 13:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='科目标题')),
                ('description', models.CharField(max_length=500, verbose_name='科目描述')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
            ],
            options={
                'verbose_name': '科目',
                'verbose_name_plural': '科目',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='课程标题')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='课程介绍')),
                ('grade', models.CharField(max_length=20, verbose_name='课程级别')),
                ('content', models.CharField(max_length=500, null=True, verbose_name='课程内容')),
                ('image', models.ImageField(null=True, upload_to='img', verbose_name='课程图片')),
                ('video', models.URLField(null=True, verbose_name='视频链接')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Subject', verbose_name='所属科目')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
    ]
