from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.

# 刘学
from django.views import View

from app.models import BBS, User


class BBS_del_view(View):
    def get(sel,request,bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.delete()
        return redirect('/bbs_list/1')

class BBS_add_view(View):
    def post(self, request):
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        bbs = BBS(title=title,content=content,user_id=1)
        bbs.save()
        return redirect('/bbs_list/1')


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
        bbs.add_time = datetime.now()
        bbs.save()
        return redirect('/bbs_list/1')


class BBS_list_view(View):
    def get(self,request,page):
        if not page:
            page = 1
        bbs_list = BBS.objects.order_by('-add_time')
        after_range_num = 3  # 当前页前显示5页
        befor_range_num = 2  # 当前页后显示4页
        page = int(page)
        try:  # 如果请求的页码少于1或者类型错误，则跳转到第1页
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        paginator = Paginator(bbs_list, 5)

        bbs_list = paginator.page(page)
        for bbs in bbs_list:
            bbs.user = bbs.getUser()
        if page >= after_range_num:
            page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
        else:
            page_range = paginator.page_range[0:int(page) + befor_range_num]

        return render(request,'bbs_list.html',locals())


class BBS_search_view(View):
    def get(self,request,page):
        key = request.GET.get('key','')
        bbs_list = BBS.objects.filter(title__icontains=key).order_by('-add_time')
        after_range_num = 3  # 当前页前显示5页
        befor_range_num = 2  # 当前页后显示4页
        page = int(page)
        try:  # 如果请求的页码少于1或者类型错误，则跳转到第1页
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        paginator = Paginator(bbs_list, 5)

        bbs_list = paginator.page(page)
        for bbs in bbs_list:
            bbs.user = bbs.getUser()
        if page >= after_range_num:
            page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
        else:
            page_range = paginator.page_range[0:int(page) + befor_range_num]
        return render(request,'bbs_search.html',locals())


class BBS_detail_view(View):
    def get(self,request,bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.user = bbs.getUser()
        return render(request,'bbs_detail.html',{'bbs':bbs})


class BBS_index_view(View):
    def get(self,request):
        return redirect('/bbs_list/1')