from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_fin_department:
            return redirect('fin_department:fin_department_home')
        else:
            return redirect('hr_department:hr_department_home')
    return render(request, 'useraccount/home.html')


