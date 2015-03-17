from django.views import generic


class EmptyView(generic.TemplateView):
    template_name = 'landing_page.html'
