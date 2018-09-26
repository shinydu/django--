from django.db import models
from subject.models import SubjectModel
from stage.models import StageModel
from outline.models import OutlineModel
import datetime
from django.contrib import admin
# Create your models here.
class ProgramModel(models.Model):
    subjects=SubjectModel.objects.all()
    subject_name_id=[(subject.id,subject.name) for subject in subjects]
    subject_id=models.IntegerField(default=0,verbose_name='学科id',choices=subject_name_id)

    stages = StageModel.objects.all()
    stage_name_id = [(stage.id, stage.title) for stage in stages]
    stage_id = models.IntegerField(default=0, verbose_name='阶段id', choices=stage_name_id)

    outlines = OutlineModel.objects.all()
    outline_name_id = [(outline.id, outline.title) for outline in outlines]
    outline_id = models.IntegerField(default=0, verbose_name='大纲id', choices=outline_name_id)

    number = models.IntegerField(default=0, verbose_name='天序')
    sign=models.CharField(max_length=80,verbose_name='标志性内容',null=False)
    digest=models.CharField(max_length=255,verbose_name='内容摘要')
    prepare=models.CharField(max_length=255,verbose_name='准备工作')
    process = models.CharField(max_length=255,verbose_name='讲课流程')
    attention = models.CharField(max_length=255,verbose_name='注意事项')
    exercise = models.CharField(max_length=255, verbose_name='课后作业')
    share = models.CharField(max_length=255, verbose_name='学生分享')
    management = models.CharField(max_length=255, verbose_name='管理事项')
    remark = models.CharField(max_length=255,verbose_name='备注')
    class Meta:
        db_table = 'program'

@admin.register(ProgramModel)
class ProgramAdminModel(admin.ModelAdmin):
    list_display=('sign','number')