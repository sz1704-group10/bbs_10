from django.shortcuts import render

# Create your views here.

# 刘学
from django.views import View


class BBS_del_view(View):
    pass

# 刘学
class BBS_add_view(View):
    def get(self, request):
        return render(request, 'bbs_add.html', {})

# 卫星
class BBS_edit_view(View):
    def get(self,request):
        return render(request,'bbs_edit.html',{})

# 熊文强
class BBS_list_view(View):
    def get(self,request):
        return render(request,'bbs_list.html',{})

# 熊文强
class BBS_search_view(View):
    def get(self,request):
        return render(request,'bbs_search.html',{})


class BBS_detail_view(View):
    def get(self,request):
        return render(request,'bbs_detail.html',{})