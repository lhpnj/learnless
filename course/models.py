from django.db import models
from django.utils import timezone

class Subject(models.Model):
    title = models.CharField('科目标题', max_length=100)
    description = models.CharField('科目描述',max_length=500)
    add_date = models.DateTimeField('创建日期',default = timezone.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '科目'
        verbose_name_plural = '科目'


class Course(models.Model):
    title = models.CharField('课程标题',max_length=100)
    description = models.CharField('课程介绍',max_length=200, null=True)
    grade = models.CharField('课程级别', max_length=20)
    content = models.CharField('课程内容',max_length=500, null=True, blank=True)
    image = models.ImageField('课程图片',upload_to='img', null=True, blank=True)
    video = models.URLField('视频链接',max_length=200, null=True, blank=True)
    add_date = models.DateTimeField('创建日期',default = timezone.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now = True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="所属科目",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'