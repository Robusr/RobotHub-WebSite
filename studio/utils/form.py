from django import forms
from django.core.exceptions import ValidationError
from studio import models
from studio.utils.bootstrap import BootStrapModelForm
from studio.utils.encrypt import md5


class DepartForm(BootStrapModelForm):
    """定义职能管理的ModelsForm类"""

    class Meta:
        model = models.Department
        fields = ["title"]

    # 定义源码添加HTML样式

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"placeholder": field.label,
                                  "class": "form-control"
                                  }


class UserAdd(BootStrapModelForm):
    """定义添加成员的ModelsForm类"""
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.UserInfo
        fields = ["name",
                  "username",
                  "password",
                  "confirm_password",
                  "gender",
                  "create_time",
                  "depart"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        """钩子方法校验密码"""
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回保存至数据库的真实值
        return confirm


class UserReset(BootStrapModelForm):
    """定义编辑成员的ModelsForm类"""
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.UserInfo
        fields = ["name",
                  "username",
                  "password",
                  "confirm_password",
                  "gender",
                  "create_time",
                  "depart"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 在数据库中校验新旧密码是否一致
        exist = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError("不能与以前的密码相同")

        return md5_pwd


class TestStateAdd(BootStrapModelForm):
    """定义添加考核状态的ModelsForm类"""
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.TestStates
        fields = ["name",
                  "username",
                  "password",
                  "confirm_password",
                  "gender",
                  "class_num",
                  "result_sub",
                  "result_obj",
                  "result_state"
                  ]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        """钩子方法校验密码"""
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回保存至数据库的真实值
        return confirm


class TestStateReset(BootStrapModelForm):
    """定义编辑考核状态的ModelsForm类"""
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.TestStates
        fields = ["name",
                  "username",
                  "password",
                  "confirm_password",
                  "gender",
                  "class_num",
                  "result_sub",
                  "result_obj",
                  "result_state"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 在数据库中校验新旧密码是否一致
        exist = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError("不能与以前的密码相同")

        return md5_pwd


class AdminForm(BootStrapModelForm):
    """定义添加管理员的ModelsForm类"""
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        """钩子方法校验密码"""
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回保存至数据库的真实值
        return confirm


class AdminEditForm(BootStrapModelForm):
    """定义编辑管理员的ModelsForm类"""

    class Meta:
        model = models.Admin
        fields = ["username"]


class AdminResetForm(BootStrapModelForm):
    """定义重置管理员密码的ModelsForm类"""
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 在数据库中校验新旧密码是否一致
        exist = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError("不能与以前的密码相同")

        return md5_pwd

    def clean_confirm_password(self):
        """钩子方法校验密码"""
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回保存至数据库的真实值
        return confirm


class LoginForm(forms.Form):
    """定义成员登录的Form类"""
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "input100",
                                      "placeholder": "Username",
                                      "type": "text",
                                      "name": "username",
                                      "required": "True"
                                      })
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "input100",
                                          "placeholder": "Password",
                                          "type": "password",
                                          "name": "password",
                                          "required": "True"
                                          }),
    )

    def clean_password(self):
        """对密码进行MD5加密"""
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
