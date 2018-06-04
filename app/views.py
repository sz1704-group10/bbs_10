from datetime import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# 刘学
from django.views import View

from app.forms import RegisterForm, LoginForm
from app.models import BBS, User


class BBS_del_view(View):
    def get(sel, request, bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.delete()
        return redirect('/bbs_list/1')


class BBS_add_view(View):
    def post(self, request):
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        bbs = BBS(title=title, content=content, user_id=1)
        bbs.save()

        return redirect('/bbs_list/1')


class BBS_edit_view(View):
    def get(self, request, bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        return render(request, 'bbs_edit.html', {'bbs': bbs})

    def post(self, request, bbs_id):
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.title = title
        bbs.content = content
        bbs.add_time = datetime.now()
        bbs.save()

        # if form.errors:
        #     return JsonResponse({'errors': form.errors)})
        return redirect('/bbs_list/1')


class BBS_list_view(View):
    def get(self, request, page):
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

        return render(request, 'bbs_list.html', locals())


class BBS_search_view(View):
    def get(self, request, page):
        key = request.GET.get('key', '')
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
        return render(request, 'bbs_search.html', locals())


class BBS_detail_view(View):
    def get(self, request, bbs_id):
        bbs = BBS.objects.filter(id=int(bbs_id)).first()
        bbs.user = bbs.getUser()
        return render(request, 'bbs_detail.html', {'bbs': bbs})


class BBS_index_view(View):
    def get(self, request):
        return redirect('/bbs_list/1')


class BBS_Register_view(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('/bbs_list/1')
        else:
            return render(request, 'register.html', {'form':form})


class BBS_Login_view(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = User.objects.filter(name=name).first()
            if not user:
                return JsonResponse({'code':'1001','msg':'用户不存在'})
            elif check_password(password,user.password):
                request.session['user'] = user.name
                return redirect('/bbs_list/1')
            else:
                return JsonResponse({'code': '1002', 'msg': '密码错误'})
        else:
            return JsonResponse({'code': '1002', 'msg': '用户名或密码错误'})


class BBS_Logout_view(View):
    def get(self,request):
        del request.session['user']
        return redirect('/login/')