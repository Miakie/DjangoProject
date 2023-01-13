import random

from django.shortcuts import render, HttpResponse, redirect
from django.utils.safestring import mark_safe

from djangoProject import settings
from electron.models import UserInfo
from electron import  models
import os
import subprocess


def index(request):
    return redirect("/user/list/")
def login(request):
    if request.method=='GET':
        return render(request,"login.html")
    name=request.POST.get("name")
    pwd=request.POST.get("password")
    print(name,pwd)
    return redirect("/user/list/")


def user_list(request):
    if request.method=="GET":
        queryset=models.FileInfo.objects.all()
        return render(request,"user_list.html",{'query_set':queryset})
    title=request.POST.get("title")
    f=models.FileInfo.objects.create(name=title)
    file_object=request.FILES.get("file")
    id=f.id
    s=open(str(id)+'.py',mode='wb')
    for chunk in file_object.chunks():
         s.write(chunk)
    s.close()

    # out = err = ""
    # # run_cmd='D:\\Practices\\djangoProject\\venv\\Scripts\\python 1.py'
    # # run_cmd='python3 1.py'
    # cominfo = subprocess.Popen(run_cmd, shell=True,
    #                            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
    #                            stderr=subprocess.PIPE, universal_newlines=True)
    # # 等子进程编译程序结束，并获取信息
    # out, err = cominfo.communicate()
    return redirect("/user/list/")


def file_delete(request):
    """删除用户"""
    nid=request.GET.get("nid")
    models.FileInfo.objects.filter(id=nid).delete()
    models.ResultInfo.objects.filter(result_id=nid).delete()
    return redirect("/user/list/")



def result_list(request):

    queryset=models.ResultInfo.objects.all()
    return render(request,'result_list.html',{'query_set':queryset})

def submit_list(request):
    if request.method=="GET":
        queryset=models.FileInfo.objects.all()
        return render(request,'submit.html',{'query_set':queryset})
    import subprocess
    id=request.POST.get("id_select")
    params=request.POST.get("params")

    out = err = ""
    temp=random.randint(1,10000000)
    os.system('touch'+' '+str(temp)+'.txt')
    os.system('echo'+' '+params+' >'+str(temp)+'.txt')
    run_cmd='python3 '+str(id)+'.py'+' <'+str(temp)+'.txt'

    # # run_cmd='python3 1.py'
    cominfo = subprocess.Popen(run_cmd, shell=True,
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, universal_newlines=True)
    # 等子进程编译程序结束，并获取信息
    out, err = cominfo.communicate()
    os.system('rm'+' '+' '+str(temp)+'.txt')
    models.ResultInfo.objects.create(result_id=id,inval=params,ouval=out,err=err)
    return redirect('/result/list/')

def file_edit(request):

    id=request.GET.get('nid')
    cont=open(str(id)+'.py').readlines()
    res=""
    for i in cont:
        res+=i+'<br>'
    res=mark_safe(res)
    return render(request, "show.html", {"content":res})