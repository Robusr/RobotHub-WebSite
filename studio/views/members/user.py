from django.shortcuts import render, redirect
from studio import models
from studio.utils.pagination import Pagination
from studio.utils.form import UserAdd, UserReset
from django.utils.safestring import mark_safe

# 页面显示状态
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


def user_list(request):
    """成员列表"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_user"] = "active"
    page_state["title"] = "工作室成员列表"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    # 搜索成员
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["id__contains"] = search_data
    # 数据库中获取成员列表
    queryset = models.UserInfo.objects.filter(**data_dict)

    # 数据分页
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    # 成员登录状态
    info_dict = request.session.get("info")
    admin_operate_state = "none"
    super_admin_operate_state = "none"
    login_state = ""
    logout_state = "none"
    name_display = ""
    if info_dict:
        login_state = "none"
        logout_state = ""
        name_display = ""
        admin_object = models.Admin.objects.filter(**info_dict).first()
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        name_user_object = models.UserInfo.objects.filter(username=info_dict.get('username')).first()
        if name_user_object:
            name_data = models.UserInfo.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].name
        name_test_object = models.TestStates.objects.filter(username=info_dict.get('username')).first()
        if name_test_object:
            name_data = models.TestStates.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].name
        name_admin_object = models.Admin.objects.filter(username=info_dict.get('username')).first()
        if name_admin_object:
            name_data = models.Admin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username

        if admin_object:
            # 组件显示状态
            admin_state = ""
            # 组件输出HTML
            admin_operate_state = mark_safe(admin_state)
        if super_admin_object:
            # 组件显示状态
            admin_state = ""
            # 组件输出HTML
            admin_operate_state = mark_safe(admin_state)
            super_admin_operate_state = mark_safe(admin_state)

    context = {
        'search_data': search_data,
        'state_list': state_list,
        'queryset': page_queryset,  # 分页后的数据
        'page_string': page_string,  # 生成页码
        'admin_operate_state': admin_operate_state,  # 管理员编辑状态
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        'login_state': login_state,
        'logout_state': logout_state,
        'name': name_display
    }

    return render(request, 'user_list.html', context)


def user_add(request):
    """添加成员"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_user"] = "active"
    page_state["title"] = "添加成员"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    # 成员登录状态
    info_dict = request.session.get("info")
    login_state = ""
    logout_state = "none"
    super_admin_operate_state = "none"
    name_display = ""
    if info_dict:
        login_state = "none"
        logout_state = ""
        name_display = ""
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        name_user_object = models.UserInfo.objects.filter(username=info_dict.get('username')).first()
        if name_user_object:
            name_data = models.UserInfo.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].name
        name_test_object = models.TestStates.objects.filter(username=info_dict.get('username')).first()
        if name_test_object:
            name_data = models.TestStates.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].name
        name_admin_object = models.Admin.objects.filter(username=info_dict.get('username')).first()
        if name_admin_object:
            name_data = models.Admin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        if super_admin_object:
            # 组件显示状态
            admin_state = ""
            # 组件输出HTML
            admin_operate_state = mark_safe(admin_state)
            super_admin_operate_state = mark_safe(admin_state)

    if request.method == "GET":
        form = UserAdd()
        context = {
            'state_list': state_list,
            "form": form,
            "title": "添加成员",
            'login_state': login_state,
            'logout_state': logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }
        return render(request, 'change.html', context)
    # 通过POST提交数据并进行校验
    form = UserAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    context = {
        'state_list': state_list,
        "form": form,
        "title": "添加成员",
        'login_state': login_state,
        'logout_state': logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }
    # 校验失败显示错误信息
    return render(request, 'change.html', context)


def user_edit(request, nid):
    """编辑成员"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_user"] = "active"
    page_state["title"] = "编辑成员信息"
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
        name_user_object = models.UserInfo.objects.filter(username=info_dict.get('username')).first()
        super_admin_object = models.SuperAdmin.objects.filter(**info_dict).first()
        if name_user_object:
            name_data = models.UserInfo.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].name
        name_test_object = models.TestStates.objects.filter(username=info_dict.get('username')).first()
        if name_test_object:
            name_data = models.TestStates.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].name
        name_admin_object = models.Admin.objects.filter(username=info_dict.get('username')).first()
        if name_admin_object:
            name_data = models.Admin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        name_super_admin_object = models.SuperAdmin.objects.filter(username=info_dict.get('username')).first()
        if name_super_admin_object:
            name_data = models.SuperAdmin.objects.filter(username=info_dict.get('username'))
            name_display = name_data[0].username
        if super_admin_object:
            # 组件显示状态
            admin_state = ""
            # 组件输出HTML
            admin_operate_state = mark_safe(admin_state)
            super_admin_operate_state = mark_safe(admin_state)

    # 根据ID在数据库中获取当前数据
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {"msg": "数据不存在"})
    if request.method == "GET":
        form = UserReset(instance=row_object)
        context = {
            'state_list': state_list,
            "form": form,
            "title": "编辑成员",
            'login_state': login_state,
            'logout_state': logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }
        return render(request, 'change.html', context)
    # 通过POST提交数据并进行校验
    form = UserReset(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list')

    context = {
        'state_list': state_list,
        "form": form,
        "title": "编辑成员",
        'login_state': login_state,
        'logout_state': logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }
    # 校验失败显示错误信息
    return render(request, 'change.html', context)


def user_delete(request, nid):
    """删除成员"""
    models.UserInfo.objects.filter(id=nid).first().delete()
    return redirect('/user/list')
