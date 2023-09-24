from django.db import models


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)


class Department(models.Model):
    """成员职能分配表"""
    # 标题数据
    title = models.CharField(verbose_name="标题", max_length=32)

    # 定制字符串输出
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """成员基本信息表"""
    # 姓名数据
    name = models.CharField(verbose_name="姓名", max_length=16)
    # 用户名数据
    username = models.CharField(verbose_name="用户名", max_length=32)
    # 密码数据
    password = models.CharField(verbose_name="密码", max_length=64)
    # 性别数据
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    # 加入时间数据
    create_time = models.DateField(verbose_name="加入时间")

    # 关联职能分配（删除置空）
    depart = models.ForeignKey(verbose_name="职能",
                               to="Department",
                               to_field="id",
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)


class SuperAdmin(models.Model):
    # 用户名数据
    username = models.CharField(verbose_name="用户名", max_length=32)
    # 密码数据
    password = models.CharField(verbose_name="密码", max_length=64)


class QuestionObj(models.Model):
    Question_1 = models.CharField(verbose_name="第一题", max_length=512, default="题目测试")

    Question_2 = models.CharField(verbose_name="第二题", max_length=512, default="题目测试")

    Question_3 = models.CharField(verbose_name="第三题", max_length=512, default="题目测试")

    Question_4 = models.CharField(verbose_name="第四题", max_length=512, default="题目测试")

    Question_5 = models.CharField(verbose_name="第五题", max_length=512, default="题目测试")

    Question_6 = models.CharField(verbose_name="第六题", max_length=512, default="题目测试")
    Question_6_A = models.CharField(verbose_name="第六题A选项", max_length=256, default="选项测试")
    Question_6_B = models.CharField(verbose_name="第六题B选项", max_length=256, default="选项测试")
    Question_6_C = models.CharField(verbose_name="第六题C选项", max_length=256, default="选项测试")
    Question_6_D = models.CharField(verbose_name="第六题D选项", max_length=256, default="选项测试")

    Question_7 = models.CharField(verbose_name="第七题", max_length=512, default="题目测试")
    Question_7_A = models.CharField(verbose_name="第七题A选项", max_length=256, default="选项测试")
    Question_7_B = models.CharField(verbose_name="第七题B选项", max_length=256, default="选项测试")
    Question_7_C = models.CharField(verbose_name="第七题C选项", max_length=256, default="选项测试")
    Question_7_D = models.CharField(verbose_name="第七题D选项", max_length=256, default="选项测试")

    Question_8 = models.CharField(verbose_name="第八题", max_length=512, default="题目测试")
    Question_8_A = models.CharField(verbose_name="第八题A选项", max_length=256, default="选项测试")
    Question_8_B = models.CharField(verbose_name="第八题B选项", max_length=256, default="选项测试")
    Question_8_C = models.CharField(verbose_name="第八题C选项", max_length=256, default="选项测试")
    Question_8_D = models.CharField(verbose_name="第八题D选项", max_length=256, default="选项测试")

    Question_9 = models.CharField(verbose_name="第九题", max_length=512, default="题目测试")
    Question_9_A = models.CharField(verbose_name="第九题A选项", max_length=256, default="选项测试")
    Question_9_B = models.CharField(verbose_name="第九题B选项", max_length=256, default="选项测试")
    Question_9_C = models.CharField(verbose_name="第九题C选项", max_length=256, default="选项测试")
    Question_9_D = models.CharField(verbose_name="第九题D选项", max_length=256, default="选项测试")

    Question_10 = models.CharField(verbose_name="第十题", max_length=512, default="题目测试")
    Question_10_A = models.CharField(verbose_name="第十题A选项", max_length=256, default="选项测试")
    Question_10_B = models.CharField(verbose_name="第十题B选项", max_length=256, default="选项测试")
    Question_10_C = models.CharField(verbose_name="第十题C选项", max_length=256, default="选项测试")
    Question_10_D = models.CharField(verbose_name="第十题D选项", max_length=512, default="选项测试")

    ans_1 = models.CharField(verbose_name="第一题答案", max_length=32)
    ans_2 = models.CharField(verbose_name="第二题答案", max_length=32)
    ans_3 = models.CharField(verbose_name="第三题答案", max_length=32)
    ans_4 = models.CharField(verbose_name="第四题答案", max_length=32)
    ans_5 = models.CharField(verbose_name="第五题答案", max_length=32)
    ans_6 = models.CharField(verbose_name="第六题答案", max_length=32)
    ans_7 = models.CharField(verbose_name="第七题答案", max_length=32)
    ans_8 = models.CharField(verbose_name="第八题答案", max_length=32)
    ans_9 = models.CharField(verbose_name="第九题答案", max_length=32)
    ans_10 = models.CharField(verbose_name="第十题答案", max_length=32)


class QuestionSub(models.Model):
    Question_A = models.CharField(verbose_name="第十一题", max_length=512)

    Question_B = models.CharField(verbose_name="第十二题", max_length=512)


class ExamResult(models.Model):
    # 用户名数据
    username = models.CharField(verbose_name="用户名", max_length=32)

    Result_1 = models.CharField(verbose_name="第一题", max_length=32)

    Result_2 = models.CharField(verbose_name="第二题", max_length=32)

    Result_3 = models.CharField(verbose_name="第三题", max_length=32)

    Result_4 = models.CharField(verbose_name="第四题", max_length=32)

    Result_5 = models.CharField(verbose_name="第五题", max_length=32)

    Result_6 = models.CharField(verbose_name="第六题", max_length=32)

    Result_7 = models.CharField(verbose_name="第七题", max_length=32)

    Result_8 = models.CharField(verbose_name="第八题", max_length=32)

    Result_9 = models.CharField(verbose_name="第九题", max_length=32)

    Result_10 = models.CharField(verbose_name="第十题", max_length=32)

    Result_A = models.CharField(verbose_name="第十一题", max_length=1024)

    Result_B = models.CharField(verbose_name="第十二题", max_length=1024)

    Score_obj_all = models.CharField(verbose_name="客观题总分", max_length=32)
    Score_sub_all = models.CharField(verbose_name="主观题总分", max_length=32)


class TestStates(models.Model):
    """成员考核状态"""
    # 姓名数据
    name = models.CharField(verbose_name="姓名", max_length=16)
    # 用户名数据
    username = models.CharField(verbose_name="用户名", max_length=32)
    # 密码数据
    password = models.CharField(verbose_name="密码", max_length=64)
    # 性别数据
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    # 班级数据
    class_num = models.IntegerField(verbose_name="班级")
    # 主观题成绩
    result_sub = models.IntegerField(verbose_name="主观题成绩")
    # 客观题成绩
    result_obj = models.IntegerField(verbose_name="客观题成绩")
    # 考核结果
    result_choices = (
        (1, "未参加考核"),
        (2, "考核未通过"),
        (3, "考核通过"),
    )
    result_state = models.SmallIntegerField(verbose_name="考核结果",
                                            choices=result_choices,
                                            default=1
                                            )
