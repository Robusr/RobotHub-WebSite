from django.shortcuts import render, redirect
from studio import models
from studio.utils.pagination import Pagination
from studio.utils.form import AdminForm, AdminEditForm, AdminResetForm
from django.utils.safestring import mark_safe

page_state = {
    "index": "#",
    "news": "#",
    "learn": "#",
    "tools": "#",
    "member": "#",
    "member_user": "#",
    "member_depart": "#",
    "member_test": "#",
    "title": "固原一中机器人创新工作室"
}


def admin_list(request):
    """管理员列表"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "管理员列表"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    # 搜索成员
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["id__contains"] = search_data

    # 数据库中获取成员列表
    queryset = models.Admin.objects.filter(**data_dict)

    # 设置分页
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    # 成员登录状态
    info_dict = request.session.get("info")
    super_admin_operate_state = "none"
    login_state = ""
    logout_state = "none"
    if info_dict:
        login_state = "none"
        logout_state = ""
        name_display = ""
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        if super_admin_object:
            super_admin_operate_state = mark_safe("")

    context = {
        "state_list": state_list,
        "queryset": page_queryset,
        "page_string": page_string,
        "search_data": search_data,
        'login_state': login_state,
        "logout_state": logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """添加管理员"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "添加管理员"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    # 成员登录状态
    info_dict = request.session.get("info")
    super_admin_operate_state = "none"
    login_state = ""
    logout_state = "none"
    name_display = ""
    if info_dict:
        login_state = "none"
        logout_state = ""
        name_display = ""
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        if super_admin_object:
            super_admin_operate_state = mark_safe("")

    if request.method == "GET":
        form = AdminForm()
        context = {
            "form": form,
            "state_list": state_list,
            "title": "添加管理员",
            'login_state': login_state,
            "logout_state": logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }

        return render(request, 'change.html', context)

    form = AdminForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')

    context = {
        "form": form,
        "state_list": state_list,
        "title": "添加管理员",
        'login_state': login_state,
        "logout_state": logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }

    return render(request, 'change.html', context)


def admin_edit(request, nid):
    """编辑管理员"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "编辑管理员"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    # 成员登录状态
    info_dict = request.session.get("info")
    super_admin_operate_state = "none"
    login_state = ""
    logout_state = "none"
    name_display = ""
    if info_dict:
        login_state = "none"
        logout_state = ""
        name_display = ""
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        if super_admin_object:
            super_admin_operate_state = mark_safe("")

    # 根据ID在数据库中获取当前数据
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {"msg": "数据不存在"})

    if request.method == "GET":
        form = AdminEditForm(instance=row_object)
        context = {
            "form": form,
            "title": "管理员编辑",
            'login_state': login_state,
            "logout_state": logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }
        return render(request, 'change.html', context)

    # 通过POST提交数据并进行校验
    form = AdminEditForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')

    context = {
        'state_list': state_list,
        "form": form,
        'login_state': login_state,
        "logout_state": logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }

    # 校验失败显示错误信息
    return render(request, 'change.html', context)


def admin_delete(request, nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).first().delete()
    return redirect('/admin/list')


def admin_reset(request, nid):
    """重置密码"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "重置管理员密码"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

        # 成员登录状态
    info_dict = request.session.get("info")
    super_admin_operate_state = "none"
    login_state = ""
    logout_state = "none"
    name_display = ""
    if info_dict:
        login_state = "none"
        logout_state = ""
        name_display = ""
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        if super_admin_object:
            super_admin_operate_state = mark_safe("")

    # 根据ID在数据库中获取当前数据
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {"msg": "数据不存在"})
    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetForm()
        context = {
            'state_list': state_list,
            "form": form,
            "title": title,
            'login_state': login_state,
            "logout_state": logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }
        return render(request, 'change.html', context)

    # 通过POST提交数据并进行校验
    form = AdminResetForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')

    context = {
        'state_list': state_list,
        "form": form,
        "title": title,
        'login_state': login_state,
        "logout_state": logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }

    # 校验失败显示错误信息
    return render(request, 'change.html', context)
