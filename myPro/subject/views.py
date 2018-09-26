from django.shortcuts import render ,redirect,render_to_response

from django.views import View
# Create your views here.
from .models import  SubjectModel
class SubjectList(View):
    def get(self ,request):
        subjects = SubjectModel.objects.all()
        return render(request ,'subject/home.html',{'subjects':subjects})
    def post(self ,request):
        return render(request ,'subject/home.html')

class DetailView(View):
    def get(self,request):
        subject_id=request.GET["subject_id"]
        subject=SubjectModel.objects.get(id=subject_id)
        return render_to_response("subject/detail.html",{"subject":subject})

class EditView(View):
    def get(self,request):
        subject_id=request.GET['subject_id']
        subject=SubjectModel.objects.get(id=subject_id)
        return render_to_response('subject/edit.html',{'subject':subject})
    def post(self,request):

        subject_id=request.POST['subject_id']

        name = request.POST['name']
        amount = request.POST['amount']
        days = request.POST['days']
        number = request.POST['number']
        assurance = request.POST['assurance']
        remark = request.POST['remark']
        subject=SubjectModel.objects.get(id=subject_id)

        if subject:
            subject.name = name
            subject.days = int(days)
            subject.amount = amount
            subject.number = int(number)
            subject.assurance = assurance
            subject.remark = remark

            subject.save()
        return redirect('/subject/')

class AddView(View):
    def get(self ,request):
        return render(request,'subject/add.html')
    def post(self ,request):
        name = request.POST['name']
        amount = request.POST['amount']
        days = request.POST['days']
        number = request.POST['number']
        assurance = request.POST['assurance']
        remark = request.POST['remark']

        subject = SubjectModel()
        subject.name = name
        subject.days = int(days)
        subject.amount = amount
        subject.number = int(number)
        subject.assurance = assurance
        subject.remark = remark
        subject.save()

        return redirect('/subject/')

class DeleteView(View):
    def get(self,request):
        subject_id=request.GET['subject_id']
        subject=SubjectModel.objects.get(id=subject_id)
        if subject:
            subject.delete()
        return redirect('/subject/')