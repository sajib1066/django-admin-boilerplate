from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class AnalyticalPageView(TemplateView):
    template_name = 'dashboard/analytical.html'
