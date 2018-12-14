from django.db import models

# 人员信息
class User(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    user_name = models.CharField(max_length=10, default='', blank=False, verbose_name='用户名')
    user_nickname = models.CharField(max_length=10, blank=False, verbose_name='登录名')
    user_phone = models.CharField(max_length=12, blank=False, verbose_name='电话')
    user_pwd = models.CharField(max_length=15, blank=False, verbose_name='密码')
    is_enable = models.BooleanField(default=True, verbose_name='是否有效')

    def __str__(self):
        return self.user_name

# 项目信息
class ProjectInfo(models.Model):
    pro_id = models.AutoField(primary_key=True, verbose_name='项目id')
    pro_name = models.CharField(max_length=20, blank=False, verbose_name='项目名称')
    pro_adds = models.CharField(max_length=20, blank=False, verbose_name='项目地址')
    pro_time = models.DateTimeField(auto_now_add=True, blank=False, verbose_name='创建时间')
    user = models.ForeignKey(
        'User', to_field='user_id', default=1, on_delete=models.CASCADE, verbose_name='创建人id')

    def __str__(self):
        return self.pro_name

# 服务器信息
class SerInfo(models.Model):
    ser_id = models.AutoField(primary_key=True, verbose_name='服务器id')
    ser_name = models.CharField(max_length=20, blank=False, verbose_name='服务器名称')
    ser_adds = models.CharField(max_length=20, blank=False, verbose_name='服务器地址')
    ser_loginName = models.CharField(max_length=50, verbose_name='服务器登陆名')
    ser_loginPwd = models.CharField(max_length=50, verbose_name='服务器密码')
    ser_time = models.DateTimeField(auto_now=True, blank=False, verbose_name='更新时间')
    projectInfo = models.ForeignKey(
        'ProjectInfo', to_field='pro_id', default=1, on_delete=models.CASCADE, verbose_name='服务器所属项目id'
    )

    def __str__(self):
        return self.ser_name

# 平台信息
class Platform(models.Model):
    pla_id = models.AutoField(primary_key=True, verbose_name='平台id')
    pla_name = models.CharField(max_length=20, blank=False, verbose_name='平台名称')
    pla_type = models.CharField(max_length=1, blank=False, verbose_name='平台类型')
    pla_adds = models.CharField(max_length=20, blank=False, verbose_name='平台地址')
    manage_adds = models.CharField(max_length=20, verbose_name='管理平台地址')
    forward_adds = models.CharField(max_length=20, verbose_name='前置机地址')
    appeui = models.CharField(max_length=20, verbose_name='AppEui')
    pla_path = models.CharField(max_length=200, verbose_name='主站安装路径')
    forward_path = models.CharField(max_length=200, verbose_name='前置机安装路径')
    pla_time = models.DateTimeField(auto_now=True, blank=False, verbose_name='更新时间')
    remake = models.CharField(max_length=500, verbose_name='备注')
    serInfo = models.ForeignKey(
        'SerInfo', to_field='ser_id', default=1, on_delete=models.CASCADE, verbose_name='平台所属服务器id')

    def __str__(self):
        return self.pla_name

# 版本信息
class Version(models.Model):
    ver_id = models.AutoField(primary_key=True, verbose_name='版本id')
    ver_no = models.CharField(max_length=10, blank=False, verbose_name='版本号')
    ver_upd = models.CharField(max_length=500, blank=False, verbose_name='修改内容')
    ver_time = models.DateTimeField(auto_now=True, blank=False, verbose_name='更新时间')
    ver_user = models.CharField(max_length=10, blank=False, verbose_name='版本创建人')
    platform = models.ForeignKey(
        'Platform', to_field='pla_id', default=1, on_delete=models.CASCADE, verbose_name='版本号所属平台id')

    def __str__(self):
        return self.ver_no
