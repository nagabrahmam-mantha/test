from .models import Employee
from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponseRedirect, HttpResponse


def view_ordosaldo(request):
    emp = Employee.objects.all()
    for i in emp:
        print("DOB:: ", i.birthdate)
    context = {}

    if request.method == "POST":
        post = request.POST.copy()
        post['first_name'] = request.POST.get('fn', None)
        post['last_name'] = request.POST.get('ln', None)
        post['birthdate'] = request.POST.get('dob', None)

        request.POST = post

        form_instance = Employee.objects.get(first_name=post['first_name'])
        # form = Employee(first_name=fn, last_name=ln)
        form = EmployeeForm(request.POST, instance=form_instance)
        print(form_instance)
        print(request.POST)
        print(form)

        if form.is_valid():
            print("Saved")
            form.save()
            return HttpResponse(status=204)

    else:
        form = EmployeeForm()


    context = {"emp": emp, "form": form}

    return render(request, "employee_view.html", context)
