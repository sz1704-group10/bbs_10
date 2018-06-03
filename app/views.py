from django.shortcuts import render, redirect

# Create your views here.

# 刘学
from django.views import View

from app.models import BBS, User


class BBS_del_view(View):
    def get(sel,request,bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.delete()
        return redirect('/bbs_list/')

class BBS_add_view(View):
    def post(self, request):
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        bbs = BBS(title=title,content=content,user_id=1)
        bbs.save()
        return redirect('/bbs_list/')


class BBS_edit_view(View):
    def get(self,request,bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        return render(request,'bbs_edit.html',{'bbs':bbs})
    def post(self,request,bbs_id):
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.title = title
        bbs.content = content
        bbs.save()
        return redirect('/bbs_list/')


class BBS_list_view(View):
    def get(self,request):
        bbs_list = BBS.objects.order_by('-add_time')
        for bbs in bbs_list:
            bbs.user = bbs.getUser()
        return render(request,'bbs_list.html',{'bbs_list':bbs_list})


class BBS_search_view(View):
    def get(self,request):
        key = request.GET.get('key','')
        bbs_list = BBS.objects.filter(title__icontains=key).order_by('-add_time')
        for bbs in bbs_list:
            bbs.user = bbs.getUser()
        return render(request,'bbs_list.html',{'bbs_list':bbs_list})


class BBS_detail_view(View):
    def get(self,request):
        return render(request,'bbs_detail.html',{})