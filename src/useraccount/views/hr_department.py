from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import HRDepartmentSignUpForm
from ..models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from ..decorators import hr_department_required



class HRDepartmentSignUpView(CreateView):
    model = User
    form_class = HRDepartmentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hr_department'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('hr_department:hr_department_home')

def hr_department_home(request):
    return render(request, 'useraccount/hr_department/hr_department_home.html')
