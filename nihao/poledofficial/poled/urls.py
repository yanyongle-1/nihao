"""bigwang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path('en/message/', message, name="message"),  # 留言
    path('message/', message, name="message"),  # 留言
    path('en/search_date/', search_date, name="search_date"),  # 搜索
    path('search_date/', search_date, name="search_date"),
    path('en/download_list/', download_list, name="download_list"),
    path('download_list/', download_list, name="download_list"),  # 下载中心下载
    path('en/download_list_read/', download_list_read, name="download_list_read"),
    path('download_list_read/', download_list_read, name="download_list_read"),  # 下载中心阅读
    path('', index, name="home"),  # 主页
    path('option_detail/', option_detail, name="option_detail"),  # 设置
    path('en/option_detail/', option_detail, name="option_detail"),  # 设置
    path('produce_list/', produce_list, name="post_list"),  # 文章列表
    path('en/produce_list/', produce_list, name="produce_list"),  # 文章列表
    path('post_list/', post_list, name="post_list"),  # 文章列表
    path('en/post_list/', post_list, name="post_list"),
    path('producecard/', produce_card, name="produce_card"),  # 产品
    path('en/producecard/', produce_card, name="produce_card"),
    path('postarticle/', postarticle, name="postarticle"),  # 文章
    path('en/postarticle/', postarticle, name="postarticle"),
    path('en/feedback/', feedback, name="feedback"),
    path('feedback/', feedback, name="feedback"),
    path('en/', index, name="home"),  # 主页
    path('cn_post/', index, name="home"),  # post
]
