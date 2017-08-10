from django.views.generic.base import TemplateView

from event_planner_app import models


class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        return context


class EmployeeListAllView(TemplateView):
    template_name = "employee_list_view.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeListAllView, self).get_context_data(**kwargs)
        employees = models.Employee.objects.all()
        context['employees'] = employees
        return context
