from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

#首页
def index(request):
    if request.method=='GET':
        return render(request,'index.html')

#关于我们
def about(request):
    return render(request,'about.html')

#常见问题界面
def faqs(request):
    # return HttpResponse('123')
    return render(request,'faqs.html')

#Web图标界面
def icons(request):
    return render(request,'icons.html')

#排版
def typography(request):
    return render(request,'typography.html')

#联系我们
def contact(request):
    return render(request,'contact.html')