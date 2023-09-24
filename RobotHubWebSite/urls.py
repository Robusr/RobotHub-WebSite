"""
URL configuration for RobotHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studio.views.members import depart, user, teststate
from studio.views import admin, account, founding
from studio.views.index import index
from studio.views.exam import exam_user, exam_admin

urlpatterns = [

    # 管理员操作
    # 职能分配页面
    path("depart/list/", depart.depart_list),
    # 添加职能页面
    path("depart/add/", depart.depart_add),
    # 删除职能页面
    path("depart/<int:nid>/delete/", depart.depart_delete),
    # 编辑职能页面
    path("depart/<int:nid>/edit/", depart.depart_edit),

    # 成员列表页面
    path("user/list/", user.user_list),
    # 添加成员页面
    path("user/add/", user.user_add),
    # 编辑成员页面
    path("user/<int:nid>/edit/", user.user_edit),
    # 删除成员页面
    path("user/<int:nid>/delete/", user.user_delete),

    # 考核状态页面
    path("test/state/", teststate.test_state),
    # 添加考核状态页面
    path("test/state/add/", teststate.test_state_add),
    # 编辑考核状态页面
    path("test/state/<int:nid>/edit/", teststate.test_state_edit),
    # 评估考核状态页面
    path("test/state/<int:nid>/mark/", teststate.test_state_mark),
    # 删除考核状态页面
    path("test/state/<int:nid>/delete/", teststate.test_state_delete),

    # 管理员管理页面
    path("admin/list/", admin.admin_list),
    # 添加管理员页面
    path("admin/add/", admin.admin_add),
    # 编辑管理员页面
    path("admin/<int:nid>/edit/", admin.admin_edit),
    # 删除管理员页面
    path("admin/<int:nid>/delete/", admin.admin_delete),
    # 管理员重置密码页面
    path("admin/<int:nid>/reset/", admin.admin_reset),

    # 登录页面
    path("login/", account.login),
    # 注销页面
    path("logout/", account.logout),

    # 首页
    path("index/", index.index_show),

    # 未完成页面
    path("founding/", founding.founding_show),

    # 考核编辑总页面
    path("exam/", exam_user.exam),
    # 考核客观题页面
    path("exam/objective/", exam_user.exam_objective),
    # 考核客观题成绩页面
    path("exam/objective/score", exam_user.exam_objective_score),
    # 考核主观题页面
    path("exam/subjective/", exam_user.exam_subjective),
    # 考核主观题成绩页面
    path("exam/subjective/score", exam_user.exam_subjective_score),

    # 考核编辑总页面
    path("exam/edit/", exam_admin.exam_edit),
    # 考核客观题编辑页面
    path("exam/objective/edit/", exam_admin.exam_objective_edit),
    # 考核主观题编辑页面
    path("exam/subjective/edit/", exam_admin.exam_subjective_edit),
]
