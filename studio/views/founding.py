from django.shortcuts import render, redirect
from studio import models
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


def founding_show(request):
    """首页"""
    # 全局变量
    global name_display

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "固原一中机器人创新工作室"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

        # 成员登录状态
    info_dict = request.session.get("info")
    admin_operate_state = "none"
    super_admin_operate_state = "none"
    login_state = ""
    logout_state = "none"
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
        'state_list': state_list,
        'login_state': login_state,
        "logout_state": logout_state,
        'admin_operate_state': admin_operate_state,  # 管理员编辑状态
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        'name': name_display
    }
    return render(request, 'founding.html', context)