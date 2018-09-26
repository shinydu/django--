from django.shortcuts import render,render_to_response,redirect
from django.views import View
from stage.models import StageModel
from subject.models import SubjectModel
from outline.models import OutlineModel
from program.models import ProgramModel

class ListView(View):
    def get(self,request):
        nameSubject=request.GET['subject_id']
        nameSubjectList=SubjectModel.objects.filter(id=nameSubject)[0]
        unameSubject=nameSubjectList.name
        nameStage=request.GET['stage_id']
        nameStageList=StageModel.objects.filter(id=nameStage)[0]
        unameStage=nameStageList.title
        nameOutline=request.GET['outline_id']
        nameOutlineList=OutlineModel.objects.filter(id=nameOutline)[0]
        unameOutline=nameOutlineList.title
        subject_id=request.GET['subject_id']
        stage_id=request.GET['stage_id']
        outline_id=request.GET['outline_id']
        program_list=ProgramModel.objects.filter(subject_id=subject_id,stage_id=stage_id,outline_id=outline_id)
        print('-----------------------------------')
        return render_to_response('program/list.html',{'program_list':program_list,'subjectName':unameSubject,'stageName':unameStage,'outlineName':unameOutline,'outlineList':nameOutlineList})

class DetailView(View):
    def get(self,request):
        program_id=request.GET['program_id']
        outline_id=request.GET['outline_id']
        stage_id=request.GET['stage_id']
        subject_id=request.GET['subject_id']
        program=ProgramModel.objects.get(id=program_id)
        outline=OutlineModel.objects.get(id=outline_id)
        stage = StageModel.objects.get(id=stage_id)
        subject = SubjectModel.objects.get(id=subject_id)
        return render_to_response('program/detail.html', {'program':program,'outline':outline,'stage': stage, 'subject': subject})

class DeleteView(View):
    def get(self,request):
        program_id=request.GET['program_id']
        program=ProgramModel.objects.get(id=program_id)
        outline_id=program.outline_id
        stage_id=program.stage_id
        subject_id=program.subject_id
        if program:
            program.delete()
        return redirect('/program/list/?subject_id={}&stage_id={}&outline_id={}'.format(subject_id,stage_id,outline_id))

class AddView(View):
    def get(self,request):
        subject=SubjectModel.objects.all()
        stage=StageModel.objects.all()
        outline=OutlineModel.objects.all()
        return render_to_response('program/add.html',{'subject':subject,'stage':stage,'outline':outline})
    def post(self,request):
        stage_id=request.POST['stage_id']
        outline_id=request.POST['outline_id']
        number=request.POST['number']
        sign=request.POST['sign']
        digest=request.POST['digest']
        prepare=request.POST['prepare']
        process=request.POST['process']
        attention=request.POST['attention']
        exercise=request.POST['exercise']
        share=request.POST['share']
        management=request.POST['management']
        remark=request.POST['remark']

        stage = StageModel.objects.get(id=stage_id)
        subject = SubjectModel.objects.get(id=stage.subject_id)
        subject_id = subject.id

        program=ProgramModel()
        program.subject_id=int(subject_id)
        program.stage_id=int(stage_id)
        program.outline_id=int(outline_id)
        program.number=int(number)
        program.sign=sign
        program.digest=digest
        program.prepare=prepare
        program.process=process
        program.attention=attention
        program.exercise=exercise
        program.share=share
        program.management=management
        program.remark=remark
        program.save()


        return redirect('/program/list/?subject_id={}&stage_id={}&outline_id={}'.format(subject_id,stage_id,outline_id))

class EditView(View):
    def get(self,request):
        program_id=request.GET['program_id']
        program=ProgramModel.objects.get(id=program_id)
        return render_to_response('program/edit.html',{'program':program})
    def post(self,request):
        program_id=request.POST['program_id']
        number = request.POST['number']
        sign = request.POST['sign']
        digest = request.POST['digest']
        prepare = request.POST['prepare']
        process = request.POST['process']
        attention = request.POST['attention']
        exercise = request.POST['exercise']
        share = request.POST['share']
        management = request.POST['management']
        remark = request.POST['remark']

        program=ProgramModel.objects.get(id=program_id)
        subject_id=program.subject_id
        stage_id=program.stage_id
        outline_id=program.outline_id

        if program:
            program.number = int(number)
            program.sign = sign
            program.digest = digest
            program.prepare = prepare
            program.process = process
            program.attention = attention
            program.exercise = exercise
            program.share = share
            program.management = management
            program.remark = remark
            program.save()

            return redirect('/program/list/?subject_id={}&stage_id={}&outline_id={}'.format(subject_id, stage_id, outline_id))














