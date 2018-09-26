from django.db import models
from subject.models import SubjectModel
from stage.models import StageModel
from django.contrib import admin
import datetime
# Create your models here.
class OutlineModel(models.Model):
    subjects=SubjectModel.objects.all()
    subject_name_id=[(subject.id,subject.name)for subject in subjects]
    subject_id=models.IntegerField(default=0,verbose_name='学科id',choices=subject_name_id)
    stages=StageModel.objects.all()
    stage_name_id=[(stage.id,stage.title)for stage in stages]
    stage_id=models.IntegerField(default=0,verbose_name='阶段id',choices=stage_name_id)
    number=models.IntegerField(default=0,verbose_name='序列')
    title=models.CharField(max_length=255,verbose_name='大纲标题')
    days=models.IntegerField(default=0,verbose_name='学时')
    advancing = models.CharField(max_length=255, verbose_name='高级内容')
    remark = models.CharField(max_length=255, verbose_name='备注')
    status=models.IntegerField(default=0,verbose_name='状态')
    creater = models.CharField(max_length=255, verbose_name='创建者')
    create_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    updater = models.CharField(max_length=255, verbose_name='更新者')
    update_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')
    class Meta:
        db_table='outline'

@admin.register(OutlineModel)
class OutlineAdminModel(admin.ModelAdmin):
    list_display=('title','number')

