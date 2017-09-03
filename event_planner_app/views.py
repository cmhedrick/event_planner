from django.views import generic
from django.views.generic.base import TemplateView

from event_planner_app import models, forms


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


class ClientListAllView(TemplateView):
    template_name = "client_list_view.html"

    def get_context_data(self, **kwargs):
        context = super(ClientListAllView, self).get_context_data(**kwargs)
        employees = models.Client.objects.all()
        context['clients'] = employees
        return context


class AddClientView(generic.FormView):
    template_name = 'add_client.html'
    form_class = forms.AddClientForm

    def get_context_data(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        context = super(AddClientView, self).get_context_data(*args, **kwargs)
        context['kwargs'] = self.kwargs
        context['request'] = self.request
        return context

    def get_form_kwargs(self):
        kwargs = super(AddClientView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AddClientView, self).form_valid(form)

    def get_success_url(self):
        return '/'


class AddEventView(generic.FormView):
    template_name = 'add_event.html'
    form_class = forms.AddEventForm

    def get_context_data(self, *args, **kwargs):
        context = super(AddEventView, self).get_context_data(*args, **kwargs)
        context['kwargs'] = self.kwargs
        context['request'] = self.request
        return context

    def get_form_kwargs(self):
        kwargs = super(AddEventView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AddEventView, self).form_valid(form)

    def get_success_url(self):
        return '/'
