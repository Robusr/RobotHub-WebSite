"""
自定义分页组件
Robusr告诉你：使用该组件，需要知道以下几点
举例
一、视图函数
def Example(request):
    # 1、根据具体情况筛选数据
    queryset = models.Example.objects.all()

    # 2、实例化分页对象
    page_object = Pagination(request, queryset)

    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    context = {
        'search_data': search_data,
        'state_list': state_list,
        'queryset': page_queryset,  # 分页后的数据
        'page_string': page_string  # 生成页码
    }

    # 3、返回至前端页面
    return render(request, 'example.html', context)

二、前端HTML页面
    {% for obj in queryset %}
        <tr>
            <td>{{ obj.xxx }}</td>
        </tr>
    {% endfor %}
    <ul class="pagination">
        {{ page_string }}
    </ul>
##################### Robusr 2023.9.8 #####################
"""
from django.utils.safestring import mark_safe
import copy


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据
        :param page_size: 每页显示多少条数据
        :param page_param: 获取URL中传递的分页参数，例如: /aaa/bbb/?page=12
        :param plus: 显示页码范围
        """
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算出当前页的前五页后五页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据未达到11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的数据大于11页
            # 当前页码小于5时
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页码大于5
                # 当前页码加5大于总页面
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        self.query_dict.setlist(self.page_param, [1])
        page_str_list = ['<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())]

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page + 1):
            if i == self.page:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = """
        <li>
            <form method="get" style="float: left;;margin-left: -1px;">
                <div class="input-group">
                    <input name="page"
                           type="text"
                           class="form-control"
                           placeholder="页码"
                           style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0px">
                    <button class="btn btn-default" type="submit" style="border-radius: 0px">跳转</button>
                </div>
            </form>
        </li>
        """

        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string
