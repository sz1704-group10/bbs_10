"""bbs_10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from app import views
from bbs_10 import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^$',views.BBS_index_view.as_view()),
    # 列表
    url(r'^bbs_list/(?P<page>\d+)/$',views.BBS_list_view.as_view(),name='bbs_list'),
    # 增
    url(r'^bbs_add/$',views.BBS_add_view.as_view()),
    # 删
    url(r'^bbs_del/(?P<bbs_id>\d+)/$',views.BBS_del_view.as_view(),name='bbs_del'),
    # 改
    url(r'^bbs_edit/(?P<bbs_id>\d+)/$',views.BBS_edit_view.as_view(),name='bbs_edit'),
    # 搜索
    url(r'^bbs_search/(?P<page>\d+)/$',views.BBS_search_view.as_view(),name='bbs_search'),
    # 详情
    url(r'^bbs_detail/(?P<bbs_id>\d+)/$', views.BBS_detail_view.as_view(),name='bbs_detail'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 注册
    url(r'^register/$',views.BBS_Register_view.as_view(),name='register'),
    # 登录
    url(r'^login/$',views.BBS_Login_view.as_view(),name='login'),
    #退出
    url(r'^logout/$',views.BBS_Logout_view.as_view(),name='logout'),


]
