from django.shortcuts import render

from django.views import View
# Create your views here.
from .models import  UserModels

from django.contrib.auth import login
class RegisterView(View):
    def get(self ,request):
        return render(request, 'register.html')
    def post(self ,request):
        username = request.POST['username']
        password = request.POST['password']

        if len(username) == 0 or len(password) == 0:
            return render(request,'register.html',{'msg':'账户和密码不能为空'})
        if UserModels.objects.filter(username=username):
            return render(request, 'register.html',{'msg':'该用户已经注册'})
        user = UserModels()
        user.username = username
        user.password = password
        user.save()
        return render(request,'login.html')

class LoginView(View):
    def get(self ,request):
        return render(request ,'login.html')
    def post(self ,request):

        username = request.POST['username']
        password = request.POST['password']

        if UserModels.objects.filter(username=username,password=password):

            user = UserModels.objects.get(username=username)
            # 获取当前登录的对象
            login(request ,user)
            return render(request, 'subject/home.html')
        else :
            return render(request,'login.html',{'msg':'账号或者密码错误'})

        # return render(request ,'login.html')