from django.shortcuts import render, redirect
from apps.models import company, department, user
# Create your views here.


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
