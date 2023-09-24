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


def exam_edit(request):
    """考核试题编辑"""
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
        'state_list': state_list,
        'login_state': login_state,
        "logout_state": logout_state,
        'admin_operate_state': admin_operate_state,  # 管理员编辑状态
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        'name': name_display
    }
    return render(request, 'exam_edit.html', context)


def exam_objective_edit(request):
    """考核客观题部分"""
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
    if request.method == "GET":
        row_object = models.QuestionObj.objects.filter(id=1).first()
        context = {
            'state_list': state_list,
            'login_state': login_state,
            "logout_state": logout_state,
            'admin_operate_state': admin_operate_state,  # 管理员编辑状态
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
            'name': name_display,
            'row_object': row_object
        }
        return render(request, 'exam_obj_edit.html', context)
    Question_1 = request.POST.get("q1")
    ans_1 = request.POST.get("ans1")

    Question_2 = request.POST.get("q2")
    ans_2 = request.POST.get("ans2")

    Question_3 = request.POST.get("q3")
    ans_3 = request.POST.get("ans3")

    Question_4 = request.POST.get("q4")
    ans_4 = request.POST.get("ans4")

    Question_5 = request.POST.get("q5")
    ans_5 = request.POST.get("ans5")

    Question_6 = request.POST.get("q6")
    ans_6 = request.POST.get("ans6")
    Question_6_a = request.POST.get("q6A")
    Question_6_b = request.POST.get("q6B")
    Question_6_c = request.POST.get("q6C")
    Question_6_d = request.POST.get("q6D")

    Question_7 = request.POST.get("q7")
    ans_7 = request.POST.get("ans7")
    Question_7_a = request.POST.get("q7A")
    Question_7_b = request.POST.get("q7B")
    Question_7_c = request.POST.get("q7C")
    Question_7_d = request.POST.get("q7D")

    Question_8 = request.POST.get("q8")
    ans_8 = request.POST.get("ans8")
    Question_8_a = request.POST.get("q8A")
    Question_8_b = request.POST.get("q8B")
    Question_8_c = request.POST.get("q8C")
    Question_8_d = request.POST.get("q8D")

    Question_9 = request.POST.get("q9")
    ans_9 = request.POST.get("ans9")
    Question_9_a = request.POST.get("q9A")
    Question_9_b = request.POST.get("q9B")
    Question_9_c = request.POST.get("q9C")
    Question_9_d = request.POST.get("q9D")

    Question_10 = request.POST.get("q10")
    ans_10 = request.POST.get("ans10")
    Question_10_a = request.POST.get("q10A")
    Question_10_b = request.POST.get("q10B")
    Question_10_c = request.POST.get("q10C")
    Question_10_d = request.POST.get("q10D")

    models.QuestionObj.objects.filter(id=1).update(Question_1=Question_1,
                                                   ans_1=ans_1,
                                                   Question_2=Question_2,
                                                   ans_2=ans_2,
                                                   Question_3=Question_3,
                                                   ans_3=ans_3,
                                                   Question_4=Question_4,
                                                   ans_4=ans_4,
                                                   Question_5=Question_5,
                                                   ans_5=ans_5,
                                                   Question_6=Question_6,
                                                   ans_6=ans_6,
                                                   Question_6_A=Question_6_a,
                                                   Question_6_B=Question_6_b,
                                                   Question_6_C=Question_6_c,
                                                   Question_6_D=Question_6_d,
                                                   Question_7=Question_7,
                                                   ans_7=ans_7,
                                                   Question_7_A=Question_7_a,
                                                   Question_7_B=Question_7_b,
                                                   Question_7_C=Question_7_c,
                                                   Question_7_D=Question_7_d,
                                                   Question_8=Question_8,
                                                   ans_8=ans_8,
                                                   Question_8_A=Question_8_a,
                                                   Question_8_B=Question_8_b,
                                                   Question_8_C=Question_8_c,
                                                   Question_8_D=Question_8_d,
                                                   Question_9=Question_9,
                                                   ans_9=ans_9,
                                                   Question_9_A=Question_9_a,
                                                   Question_9_B=Question_9_b,
                                                   Question_9_C=Question_9_c,
                                                   Question_9_D=Question_9_d,
                                                   Question_10=Question_10,
                                                   ans_10=ans_10,
                                                   Question_10_A=Question_10_a,
                                                   Question_10_B=Question_10_b,
                                                   Question_10_C=Question_10_c,
                                                   Question_10_D=Question_10_d
                                                   )
    context = {
        'state_list': state_list,
        'login_state': login_state,
        "logout_state": logout_state,
        'admin_operate_state': admin_operate_state,  # 管理员编辑状态
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        'name': name_display,
    }
    return redirect("/exam/edit")


def exam_subjective_edit(request):
    """考核主观题部分"""
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
    if request.method == "GET":
        row_object = models.QuestionSub.objects.filter(id=1).first()
        context = {
            'state_list': state_list,
            'login_state': login_state,
            "logout_state": logout_state,
            'admin_operate_state': admin_operate_state,  # 管理员编辑状态
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
            'name': name_display,
            'row_object': row_object
        }
        return render(request, 'exam_sub_edit.html', context)
    Question_A = request.POST.get("qA")
    Question_B = request.POST.get("qB")

    models.QuestionSub.objects.filter(id=1).update(Question_A=Question_A,
                                                   Question_B=Question_B,
                                                   )
    context = {
        'state_list': state_list,
        'login_state': login_state,
        "logout_state": logout_state,
        'admin_operate_state': admin_operate_state,  # 管理员编辑状态
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        'name': name_display,
    }
    return redirect("/exam/edit")
