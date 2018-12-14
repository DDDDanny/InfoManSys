from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from . import models

def login(request):
    return render(request, 'infoSys/login.html')

def login_jud(request):
    # 从前端获取用户名和密码
    user_login_name = request.POST.get('username', '')
    user_login_pwd = request.POST.get('pwd', '')
    user_info = models.User.objects.all()
    # 判断用户名与密码为空的情况
    if user_login_name == '' or user_login_pwd == '':
        messages.error(request, '用户名或密码不能为空！')
        return redirect('infoSys:login')
    else:
        # 判断用户名和密码是否正确
        for user in user_info:
            if user_login_name == user.user_nickname and user_login_pwd == user.user_pwd:
                return redirect('infoSys:index')
    messages.error(request, '用户名或密码输入错误！请重新输入！')  # 不能用大写！
    return redirect('infoSys:login')

def index(request):
    return render(request, 'infoSys/index.html')

# 浏览用户信息
def user_info_page(request):
    user_info = models.User.objects.all()
    return render(request, 'infoSys/user_info_page.html', {'user_info': user_info})

def user_info_edit(request, user_id):
    if str(user_id) == '0':
        return render(request, 'infoSys/user_info_add.html')  # 如果id为0，则是新添加
    user_info = models.User.objects.get(pk=user_id)
    return render(request, 'infoSys/user_info_add.html', {'user_info': user_info})

# 添加用户信息（&编辑用户信息）
def user_info_add(request):
    # 前端获取信息
    user_name = request.POST.get('username', 'name')
    user_nickname = request.POST.get('nickname', 'nickname')
    user_phone = request.POST.get('phone', '123')
    user_pwd = request.POST.get('pwd', 'admin')
    user_id = request.POST.get('id', 0)

    if str(user_id) == '0':
        # 添加数据
        models.User.objects.create(
            user_name=user_name,
            user_nickname=user_nickname,
            user_phone=user_phone,
            user_pwd=user_pwd,
        )
        # 重定向
        return redirect('infoSys:user_info_page')

    # 编辑人员信息（方法一）
    # user_info = models.User.objects.get(pk=user_id)
    # user_info.user_name = user_name
    # user_info.user_nickname = user_nickname
    # user_info.user_phone = user_phone
    # user_info.user_pwd = user_pwd
    # user_info.save()

    # 编辑人员信息（方法二）
    models.User.objects.filter(pk=user_id).update(
        user_name=user_name,
        user_nickname=user_nickname,
        user_phone=user_phone,
        user_pwd=user_pwd,
    )
    return redirect('infoSys:user_info_page')

# 删除用户信息
def user_info_del(request, user_id):
    if str(user_id) != '0':
        models.User.objects.filter(user_id=user_id).delete()  # 删除数据
        return redirect('infoSys:user_info_page')
    return HttpResponse('Error!')

# 查看项目信息
def project_info_page(request):
    pro_info = models.ProjectInfo.objects.all()
    return render(request, 'infoSys/pro_info_page.html', {'pro_info': pro_info})

# 编辑项目信息向导
def project_info_edit(request, pro_id):
    user_info = models.User.objects.all()
    print(pro_id)
    if str(pro_id) == '0':
        return render(request, 'infoSys/pro_info_add.html', {'user_info': user_info})
    pro_info = models.ProjectInfo.objects.get(pk=pro_id)
    return render(request, 'infoSys/pro_info_add.html', {'pro_info': pro_info})

# 添加项目信息&编辑项目信息
def project_info_add(request):
    pro_name = request.POST.get('proname', 'proname')
    pro_adds = request.POST.get('proadds', 'proadds')
    username = request.POST.get('username')
    pro_id = request.POST.get('id', 0)

    if str(pro_id) == '0':
        models.ProjectInfo.objects.create(
            pro_name=pro_name,
            pro_adds=pro_adds,
            user=models.User.objects.get(user_id=username)  # 实例化对象
        )
        return redirect('infoSys:pro_info_page')

    models.ProjectInfo.objects.filter(pk=pro_id).update(
        pro_name=pro_name,
        pro_adds=pro_adds,
    )
    return redirect('infoSys:pro_info_page')

# 删除项目信息
def project_info_del(request, pro_id):
    if str(pro_id) != '0':
        models.ProjectInfo.objects.filter(pro_id=pro_id).delete()
        return redirect('infoSys:pro_info_page')
    return HttpResponse('Error!')

# 浏览服务器信息
def ser_info_page(request):
    ser_info = models.SerInfo.objects.all()
    return render(request, 'infoSys/ser_info_page.html', {'ser_info': ser_info})

# 编辑服务器信息向导
def ser_info_edit(request, ser_id):
    pro_info = models.ProjectInfo.objects.all()  # 获取下拉菜单信息（服务器所属项目）
    if str(ser_id) == '0':
        return render(request, 'infoSys/ser_info_add.html', {'pro_info': pro_info})
    ser_info = models.SerInfo.objects.get(pk=ser_id)
    return render(request, 'infoSys/ser_info_add.html', {'ser_info': ser_info, 'pro_info': pro_info})

# 添加服务器信息&编辑服务器信息
def ser_info_add(request):
    ser_name = request.POST.get('sername', 'sername')
    ser_adds = request.POST.get('seradds', 'seradds')
    loginname = request.POST.get('loginname', 'loginname')
    loginpwd = request.POST.get('loginpwd', 'loginpwd')
    proinfo = request.POST.get('proinfo')
    ser_id = request.POST.get('id', 0)

    if str(ser_id) == '0':
        models.SerInfo.objects.create(
            ser_name=ser_name,
            ser_adds=ser_adds,
            ser_loginName=loginname,
            ser_loginPwd=loginpwd,
            projectInfo=models.ProjectInfo.objects.get(pro_id=proinfo)
        )
        return redirect('infoSys:ser_info_page')

    models.SerInfo.objects.filter(pk=ser_id).update(
        ser_name=ser_name,
        ser_adds=ser_adds,
        ser_loginName=loginname,
        ser_loginPwd=loginpwd,
        projectInfo=models.ProjectInfo.objects.get(pro_id=proinfo)
    )
    return redirect('infoSys:ser_info_page')

# 删除服务器信息
def ser_info_del(request, ser_id):
    if str(ser_id) != '0':
        models.SerInfo.objects.filter(pk=ser_id).delete()
        return redirect('infoSys:ser_info_page')
    return HttpResponse('Error!')

# 浏览平台信息
def pla_info_page(request):
    pla_info = models.Platform.objects.all()
    return render(request, 'infoSys/pla_info_page.html', {'pla_info': pla_info})

# 编辑平台信息向导
def pla_info_edit(request, pla_id):
    ser_info = models.SerInfo.objects.all()  # 获取下拉菜单信息（平台所属项目）
    if str(pla_id) == '0':
        return render(request, 'infoSys/pla_info_add.html', {'ser_info': ser_info})
    pal_info = models.Platform.objects.get(pk=pla_id)
    return render(request, 'infoSys/pla_info_add.html', {'ser_info': ser_info, 'pla_info': pal_info})

# 添加平台信息&编辑平台信息
def pla_info_add(request):
    pla_name = request.POST.get('planame', 'planame')
    pla_type = request.POST.get('platype', '1')
    pla_adds = request.POST.get('plaadds', 'adds')
    manage_adds = request.POST.get('manageadds', 'adds')
    forward_adds = request.POST.get('forwardadds', 'forwardadds')
    appeui = request.POST.get('appeui', 'appeui')
    pla_path = request.POST.get('plapath', 'plapath')
    forward_path = request.POST.get('forwardpath', 'forwardpath')
    remake = request.POST.get('remake')
    serinfo = request.POST.get('serinfo')
    pla_id = request.POST.get('id', 0)

    if str(pla_id) == '0':
        models.Platform.objects.create(
            pla_name=pla_name,
            pla_type=pla_type,
            pla_adds=pla_adds,
            manage_adds=manage_adds,
            forward_adds=forward_adds,
            appeui=appeui,
            pla_path=pla_path,
            forward_path=forward_path,
            remake=remake,
            serInfo=models.SerInfo.objects.get(ser_id=serinfo)
        )
        return redirect('infoSys:pla_info_page')
    models.Platform.objects.filter(pk=pla_id).update(
        pla_name=pla_name,
        pla_type=pla_type,
        pla_adds=pla_adds,
        manage_adds=manage_adds,
        forward_adds=forward_adds,
        appeui=appeui,
        pla_path=pla_path,
        forward_path=forward_path,
        remake=remake,
        serInfo=models.SerInfo.objects.get(ser_id=serinfo)
    )
    return redirect('infoSys:pla_info_page')

# 删除平台信息
def pla_info_del(request, pla_id):
    if str(pla_id) != '0':
        models.Platform.objects.filter(pk=pla_id).delete()
        return redirect('infoSys:pla_info_page')
    return HttpResponse('Error!')

# 浏览版本信息
def ver_info_page(request):
    ver_info = models.Version.objects.all()
    return render(request, 'infoSys/ver_info_page.html', {'ver_info': ver_info})

# 编辑版本信息向导
def ver_info_edit(request, ver_id):
    pla_info = models.Platform.objects.all()
    if str(ver_id) == '0':
        return render(request, 'infoSys/ver_info_add.html', {'pla_info': pla_info})
    ver_info = models.Version.objects.get(pk=ver_id)
    return render(request, 'infoSys/ver_info_add.html', {'pla_info': pla_info, 'ver_info': ver_info})

# 添加版本信息&编辑版本信息
def ver_info_add(request):
    ver_no = request.POST.get('verno', 'ver')
    ver_upd = request.POST.get('verupd', 'upd')
    ver_user = request.POST.get('veruser', 'user')
    plainfo = request.POST.get('plainfo')
    ver_id = request.POST.get('id', 0)

    if str(ver_id) == '0':
        models.Version.objects.create(
            ver_no=ver_no,
            ver_upd=ver_upd,
            ver_user=ver_user,
            platform=models.Platform.objects.get(pla_id=plainfo)
        )
        return redirect('infoSys:ver_info_page')
    models.Version.objects.filter(pk=ver_id).update(
        ver_no=ver_no,
        ver_upd=ver_upd,
        ver_user=ver_user,
        platform=models.Platform.objects.get(pla_id=plainfo)
    )
    return redirect('infoSys:ver_info_page')

# 删除版本信息
def ver_info_del(request, ver_id):
    if str(ver_id) != '0':
        models.Version.objects.filter(pk=ver_id).delete()
        return redirect('infoSys:ver_info_page')
    return HttpResponse('Error')
