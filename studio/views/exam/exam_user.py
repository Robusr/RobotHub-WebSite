from django.shortcuts import render, redirect
from studio import models
from django.utils.safestring import mark_safe
from studio.utils.score import Score

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


def exam(request):
    """考核总页面"""
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
    return render(request, 'exam.html', context)


def exam_objective(request):
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
        queryset = models.QuestionObj.objects.all()
        context = {
            'state_list': state_list,
            'login_state': login_state,
            "logout_state": logout_state,
            'admin_operate_state': admin_operate_state,  # 管理员编辑状态
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
            'name': name_display,
            'queryset': queryset
        }
        return render(request, 'exam_obj.html', context)

    Result_1 = request.POST.get("q1")
    Result_2 = request.POST.get("q2")
    Result_3 = request.POST.get("q3")
    Result_4 = request.POST.get("q4")
    Result_5 = request.POST.get("q5")
    Result_6 = request.POST.get("q6")
    Result_7 = request.POST.get("q7")
    Result_8 = request.POST.get("q8")
    Result_9 = request.POST.get("q9")
    Result_10 = request.POST.get("q10")

    username = info_dict.get("username")

    models.ExamResult.objects.create(
        username=username,
        Result_1=Result_1,
        Result_2=Result_2,
        Result_3=Result_3,
        Result_4=Result_4,
        Result_5=Result_5,
        Result_6=Result_6,
        Result_7=Result_7,
        Result_8=Result_8,
        Result_9=Result_9,
        Result_10=Result_10,
    )
    return redirect("/exam/objective/score")


def exam_subjective(request):
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
        queryset = models.QuestionSub.objects.all()
        context = {
            'state_list': state_list,
            'login_state': login_state,
            "logout_state": logout_state,
            'admin_operate_state': admin_operate_state,  # 管理员编辑状态
            'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
            'name': name_display,
            'queryset': queryset
        }
        return render(request, 'exam_sub.html', context)
    Result_A = request.POST.get("qA")
    Result_B = request.POST.get("qB")

    username = info_dict.get("username")

    models.ExamResult.objects.filter(username=username).update(
        Result_A=Result_A,
        Result_B=Result_B
    )
    return redirect("/exam/subjective/score")


def exam_objective_score(request):
    """考核客观题得分部分"""
    # 全局变量
    global name_display, score

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "固原一中机器人创新工作室"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    queryset = models.QuestionSub.objects.all()

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

        score_object = Score(request)
        score = score_object.score_obj_all()
        models.TestStates.objects.filter(username=info_dict.get('username')).update(result_obj=str(score))
    context = {
        'state_list': state_list,
        'login_state': login_state,
        "logout_state": logout_state,
        'admin_operate_state': admin_operate_state,  # 管理员编辑状态
        'super_admin_operate_state': super_admin_operate_state,  # 超级管理员编辑状态
        'name': name_display,
        'queryset': queryset,
        'score': score
    }
    return render(request, 'score_obj.html', context)


def exam_subjective_score(request):
    """考核主观题得分部分"""
    # 全局变量
    global name_display, score

    # 页面显示状态
    for key in page_state:
        page_state[key] = "#"
    page_state["title"] = "固原一中机器人创新工作室"
    state_list = []
    for value in page_state.values():
        state_list.append(value)

    queryset = models.QuestionSub.objects.all()

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
        'name': name_display,
        'queryset': queryset,
    }
    return render(request, 'score_sub.html', context)
