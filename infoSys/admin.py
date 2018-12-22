from django.contrib import admin

from .models import User, ProjectInfo, SerInfo, Platform, Version


# 人员信息
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_nickname', 'user_phone')
    search_fields = ('user_name',)


# 项目信息
@admin.register(ProjectInfo)
class ProInfoAdmin(admin.ModelAdmin):
    list_display = ('pro_id', 'pro_name', 'pro_adds', 'pro_time', 'user')
    search_fields = ('pro_name',)


# 服务器信息
@admin.register(SerInfo)
class SerInfoAdmin(admin.ModelAdmin):
    list_display = ('ser_id', 'ser_name', 'ser_adds', 'ser_loginName', 'ser_loginPwd', 'ser_time', 'projectInfo')
    search_fields = ('ser_id',)


@admin.register(Platform)
# 平台信息
class PlatformAdmin(admin.ModelAdmin):
    list_display = (
        'pla_id', 'pla_name', 'pla_type', 'pla_adds', 'manage_adds',
        'forward_adds', 'appeui', 'pla_path', 'forward_path',
        'pla_time', 'remake', 'serInfo'
    )
    search_fields = ('pla_name',)


# 项目信息
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        'ver_id', 'ver_no', 'ver_upd', 'ver_time', 'ver_user', 'platform'
    )
    search_fields = ('platform',)
