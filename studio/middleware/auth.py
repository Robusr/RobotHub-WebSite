from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 排除非认证页面
        if request.path_info == "/login/":
            return
        if request.path_info == "/index/":
            return
        if request.path_info == "/":
            return redirect('/index/')
        # 读取当前成员的session信息
        info_dict = request.session.get("info")
        if info_dict:
            return
        # 未登录返回登录页面
        return redirect('/login/')

    def process_response(self, request, response):
        return response
