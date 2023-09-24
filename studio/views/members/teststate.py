from django.shortcuts import render, redirect
from studio import models
from studio.utils.pagination import Pagination
from studio.utils.form import TestStateAdd, TestStateReset
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


def test_state(request):
    """考核状态"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_test"] = "active"
    page_state["title"] = "工作室成员考核状态"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    # 搜索考核状态
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["id__contains"] = search_data

    # 数据库中获取考核状态
    queryset = models.TestStates.objects.filter(**data_dict)

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

    return render(request, 'test_state.html', context)


def test_state_add(request):
    """添加考核状态"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_test"] = "active"
    page_state["title"] = "添加考核状态"
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
        form = TestStateAdd()
        context = {
            'state_list': state_list,
            "form": form,
            "title": "添加考核状态",
            'login_state': login_state,
            'logout_state': logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }
        return render(request, 'change.html', context)
    # 通过POST提交数据并进行校验
    form = TestStateAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/test/state')
    context = {
        'state_list': state_list,
        "form": form,
        "title": "添加考核状态",
        'login_state': login_state,
        'logout_state': logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }
    # 校验失败显示错误信息
    return render(request, 'change.html', context)


def test_state_edit(request, nid):
    """编辑考核状态"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_test"] = "active"
    page_state["title"] = "编辑考核状态"
    state_list = []
    for value in page_state.values():
        state_list.append(value)
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

    row_object = models.TestStates.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {"msg": "数据不存在"})
    if request.method == "GET":
        form = TestStateReset(instance=row_object)
        context = {
            'state_list': state_list,
            "form": form,
            "title": "编辑考核状态",
            'login_state': login_state,
            'logout_state': logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        }
        return render(request, 'change.html', context)
    # 通过POST提交数据并进行校验
    form = TestStateReset(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/test/state')
    context = {
        'state_list': state_list,
        "form": form,
        "title": "编辑考核状态",
        'login_state': login_state,
        'logout_state': logout_state,
        'name': name_display,
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
    }
    # 校验失败显示错误信息
    return render(request, 'change.html', context)


def test_state_delete(request, nid):
    """删除考核状态"""
    models.TestStates.objects.filter(id=nid).first().delete()
    return redirect('/test/state')


def test_state_mark(request, nid):
    """编辑考核状态"""
    # 全局变量
    global name_display, user_sub

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["member"] = "active"
    page_state["member_test"] = "active"
    page_state["title"] = "编辑考核状态"
    state_list = []
    for value in page_state.values():
        state_list.append(value)
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
    user_id = models.TestStates.objects.filter(id=nid)
    username = user_id[0].username
    user_name_display = user_id[0].name
    user_sub_state = models.ExamResult.objects.filter(username=username).first()
    if user_sub_state:
        user_sub = models.ExamResult.objects.filter(username=username)
        sub_data = user_sub[0].Result_A
        if not sub_data:
            context = {
                'state_list': state_list,
                "title": "编辑考核状态",
                'login_state': login_state,
                'logout_state': logout_state,
                'name': name_display,
                'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
                "msg": "数据不存在"
            }
            return render(request, 'error.html', context)
    if not user_sub_state:
        context = {
            'state_list': state_list,
            "title": "编辑考核状态",
            'login_state': login_state,
            'logout_state': logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
            "msg": "数据不存在"
        }
        return render(request, 'error.html', context)
    if request.method == "GET":
        user_result_A = user_sub[0].Result_A
        user_result_B = user_sub[0].Result_B
        context = {
            'state_list': state_list,
            "title": "编辑考核状态",
            'login_state': login_state,
            'logout_state': logout_state,
            'name': name_display,
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
            'user_result_A': user_result_A,
            'user_result_B': user_result_B,
            'user_name': user_name_display
        }
        return render(request, 'exam_sub_mark.html', context)
    # 通过POST提交数据并进行校验
    user_score = int(request.POST.get("qA")) + int(request.POST.get("qB"))
    print(user_score)
    models.TestStates.objects.filter(username=info_dict.get('username')).update(result_sub=str(user_score))
    return redirect('/test/state')
