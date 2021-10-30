from django.shortcuts import render, redirect
from apps.models import company, department, user
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
import collections


from pyecharts import options as opts
from pyecharts.charts import Bar


def index(request):
    company_all = company.objects.all()
    department_all = department.objects.all()
    user_all = user.objects.all()

    context = {
        "company": company_all,
        "department": department_all,
        "user": user_all,
    }
    return render(request, "index.html", context=context)


def demo(request):
    dep = department.objects.all()
    u = user.objects.all()
    d = [i.dname for i in dep]
    t = [i.dep_id_id for i in u]
    # 利用collections包求出列表中每个数的次数
    # coll = collections.Counter(t).values()
    # print(coll)
    # 求出列表每个数的次数
    result = {}
    for t_shu in t:
        if result.get(t_shu) == None:
            result[t_shu] = 1
        else:
            result[t_shu] += 1
    # 字典值转换列表
    value_list = list(result.values())
    c = (
        Bar()
        .add_xaxis(d)
        .add_yaxis("人数", value_list)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return HttpResponse(c.render_embed())
    # return HttpResponse("ttttt")

def add(request):
    company_all = company.objects.all()
    department_all = department.objects.all()
    user_all = user.objects.all()

    context = {
        "company": company_all,
        "department": department_all,
        "user": user_all,
    }
    if request.method == 'GET':
        return render(request, "add.html", context=context)
    else:
        # 拿数据
        username = request.POST.get("username")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        department_id = request.POST.get("department")
        company_id = request.POST.get("company")
        d = department.objects.filter(id=department_id).first()
        c = company.objects.filter(id=company_id).first()
        # 添加数据
        user_g = user(username=username, number=number, gender=gender, dep_id=d, company_id=c)
        user_g.save()
        return redirect(index)
