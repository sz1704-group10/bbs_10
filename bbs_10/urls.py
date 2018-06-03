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

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^$',views.BBS_list_view.as_view()),
    # 列表
    url(r'^bbs_list/$',views.BBS_list_view.as_view()),
    # 增
    url(r'^bbs_add/$',views.BBS_add_view.as_view()),
    # 删
    url(r'^bbs_del/$',views.BBS_del_view.as_view()),
    # 改
    url(r'^bbs_edit/$',views.BBS_edit_view.as_view()),
    # 搜索
    url(r'^bbs_search/$',views.BBS_search_view.as_view()),
    # 详情
    url(r'^bbs_detail/$', views.BBS_detail_view.as_view()),

]
