from django.shortcuts import render,render_to_response,redirect
from django.views import View
from stage.models import StageModel
from subject.models import SubjectModel
from outline.models import OutlineModel

# Create your views here.
class OutlineListView(View):
    def get(self,request):
        nameSubject=request.GET['subject_id']
        nameSubjectList=SubjectModel.objects.filter(id=nameSubject)[0]
        unameSubject=nameSubjectList.name
        nameStage=request.GET['stage_id']
        nameStageList=StageModel.objects.filter(id=nameStage)[0]
        unameStage=nameStageList.title
        subject_id=request.GET['subject_id']
        stage_id=request.GET['stage_id']
        outline_list=OutlineModel.objects.filter(subject_id=subject_id,stage_id=stage_id)
        return render_to_response('outline/outline_list.html',{'outline_list':outline_list,'subjectName':unameSubject,'stageName':unameStage})

class DetailView(View):
    def get(self,request):
        outline_id=request.GET['outline_id']
        stage_id=request.GET['stage_id']
        subject_id=request.GET['subject_id']
        outline=OutlineModel.objects.get(id=outline_id)
        stage = StageModel.objects.get(id=stage_id)
        subject = SubjectModel.objects.get(id=subject_id)
        return render_to_response('outline/detail.html', {'outline':outline,'stage': stage, 'subject': subject})

class DeleteView(View):
    def get(self,request):
        outline_id=request.GET['outline_id']
        outline=OutlineModel.objects.get(id=outline_id)
        stage_id=outline.stage_id
        subject_id=outline.subject_id
        if outline:
            outline.delete()
        return redirect('/outline/list/?subject_id={}&stage_id={}'.format(subject_id,stage_id))

class AddView(View):
    def get(self,request):
        subject=SubjectModel.objects.all()
        stage=StageModel.objects.all()
        return render_to_response('outline/add.html',{'subject':subject,'stage':stage})
    def post(self,request):
        subject_id=request.POST['subject_id']
        stage_id=request.POST['stage_id']
        title=request.POST['title']
        days=request.POST['days']
        number=request.POST['number']
        advancing=request.POST['advancing']
        remark=request.POST['remark']

        outline=OutlineModel()
        outline.subject_id=subject_id
        outline.stage_id=stage_id
        outline.title=title
        outline.days=int(days)
        outline.number=int(number)
        outline.advancing=advancing
        outline.remark=remark
        outline.save()

        return redirect('/outline/list/?subject_id={}&stage_id={}'.format(subject_id,stage_id))

class EditView(View):
    def get(self,request):
        outline_id = request.GET['outline_id']
        outline = OutlineModel.objects.get(id=outline_id)
        return render_to_response('outline/edit.html', {'outline': outline})
    def post(self,request):
        outline_id=request.POST['outline_id']
        title=request.POST['title']
        days=request.POST['days']
        number=request.POST['number']
        advancing = request.POST['advancing']
        remark=request.POST['remark']

        outline=OutlineModel.objects.get(id=outline_id)
        subject_id=outline.subject_id
        stage_id=outline.stage_id

        if outline:
            outline.title=title
            outline.days=int(days)
            outline.number=int(number)
            outline.advancing = advancing
            outline.remark=remark
            outline.save()
        return redirect('/outline/list/?subject_id={}&stage_id={}'.format(subject_id,stage_id))