from django.shortcuts import render, redirect
from studio.utils.form import LoginForm
from studio import models


def login(request):
    """成员登录"""
    if request.method == "GET":
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context)
    form = LoginForm(data=request.POST)
    context = {
        "form": form
    }
    if form.is_valid():
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
        test_object = models.TestStates.objects.filter(**form.cleaned_data).first()
        super_admin_object = models.SuperAdmin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            if not user_object:
                if not test_object:
                    if not super_admin_object:
                        form.add_error("password", "用户名或密码错误")
                        return render(request, 'login.html', context)
                    # 用户名密码正确
                    # 网站生成随机字符串，写入到成员的Cookie中，再写入到Session中
                    request.session["info"] = {
                        "id": super_admin_object.id,
                        "username": super_admin_object.username,
                    }
                    return redirect('/index')
                # 用户名密码正确
                # 网站生成随机字符串，写入到成员的Cookie中，再写入到Session中
                request.session["info"] = {
                    "id": test_object.id,
                    "username": test_object.username,
                }
                print(test_object.name)
                return redirect('/index')
            # 用户名密码正确
            # 网站生成随机字符串，写入到成员的Cookie中，再写入到Session中
            request.session["info"] = {
                "id": user_object.id,
                "username": user_object.username,
            }
            return redirect('/index')
        # 用户名密码正确
        # 网站生成随机字符串，写入到成员的Cookie中，再写入到Session中
        request.session["info"] = {
            "id": admin_object.id,
            "username": admin_object.username
        }
        return redirect('/index')
    return render(request, 'login.html', context)


def logout(request):
    """注销"""
    request.session.clear()
    return redirect("/index")
