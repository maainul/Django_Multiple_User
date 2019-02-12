from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..models import User
from ..forms import FinanceDepartmentSignUpForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect



class FinanceDepartmentSignUpView(CreateView):
    model = User
    form_class = FinanceDepartmentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'fin_department'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('fin_department:fin_department_home')


def fin_department_home(request):
    return render(request, 'useraccount/fin_department/fin_department_home.html')
