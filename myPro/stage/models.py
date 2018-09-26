from django.db import models
from subject.models import SubjectModel
import datetime
from django.contrib import admin
# Create your models here.
class StageModel(models.Model):
    subjects=SubjectModel.objects.all()

    subject_name_id=[(subject.id,subject.name) for subject in subjects]
    subject_id=models.IntegerField(default=0,verbose_name='学科id',choices=subject_name_id)
    title=models.CharField(max_length=80,verbose_name='阶段标题',null=False)
    number=models.IntegerField(default=0,verbose_name='排序')
    days=models.IntegerField(default=0,verbose_name='学时')
    project=models.CharField(max_length=255,verbose_name='项目')
    teaching=models.CharField(max_length=255,verbose_name='教学方法')
    learning = models.CharField(max_length=255,verbose_name='学习方法')
    sharing = models.CharField(max_length=255,verbose_name='学生分享')
    remark = models.CharField(max_length=255,verbose_name='备注')
    status=models.CharField(max_length=255,verbose_name='状态')
    ceater=models.CharField(max_length=255,verbose_name='创建者')
    updater=models.CharField(max_length=255,verbose_name='更新者')
    update_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')
    class Meta:
        db_table = 'stage'

@admin.register(StageModel)
class StageAdminModel(admin.ModelAdmin):
    list_display=('title','number')