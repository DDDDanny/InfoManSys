# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 0:38
# @Author  : DannyDong
# @File    : urls.py
# @describe: 配置url地址


from django.urls import path
from . import views

app_name = '[infoSys]'

urlpatterns = [
    # 用户登录
    path('login/', views.login, name='login'),
    path('login_jud/', views.login_jud, name='login_jud'),
    path('logout/', views.logout, name='logout'),
    # 人员相关路由
    path('index/', views.index, name='index'),
    path('userInfo/', views.user_info_page, name='user_info_page'),
    path('userInfo_edit/<int:user_id>', views.user_info_edit, name='user_info_edit'),
    path('user_add/', views.user_info_add, name='user_info_add'),
    path('user_del/<int:user_id>', views.user_info_del, name='user_info_del'),
    # 项目相关路由
    path('proInfo/', views.project_info_page, name='pro_info_page'),
    path('proInfo_edit/<int:pro_id>', views.project_info_edit, name='pro_info_edit'),
    path('proInfo_add/', views.project_info_add, name='pro_info_add'),
    path('proInfo_del/<int:pro_id>', views.project_info_del, name='pro_info_del'),
    # 服务器相关路由
    path('serInfo/', views.ser_info_page, name='ser_info_page'),
    path('serInfo_edit/<int:ser_id>', views.ser_info_edit, name='ser_info_edit'),
    path('serInfo_add/', views.ser_info_add, name='ser_info_add'),
    path('serInfo_del/<int:ser_id>', views.ser_info_del, name='ser_info_del'),
    # 平台信息相关路由
    path('plaInfo/', views.pla_info_page, name='pla_info_page'),
    path('plaInfo_edit/<int:pla_id>', views.pla_info_edit, name='pla_info_edit'),
    path('plaInfo_add/', views.pla_info_add, name='pla_info_add'),
    path('plaInfo_del/<int:pla_id>', views.pla_info_del, name='pla_info_del'),
    # 版本信息相关路由
    path('verInfo/', views.ver_info_page, name='ver_info_page'),
    path('verInfo_edit/<int:ver_id>', views.ver_info_edit, name='ver_info_edit'),
    path('verInfo_add/', views.ver_info_add, name='ver_info_add'),
    path('verInfo_del/<int:ver_id>', views.ver_info_del, name='ver_info_del'),
]
