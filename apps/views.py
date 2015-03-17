from django.views import generic
from django.core.urlresolvers import reverse_lazy

from apps.notifications.forms import SubscribeForm
from apps.notifications.mailchimp_services import subscribe_email


class LandingPageView(generic.FormView):
    template_name = 'landing_page.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        subscribe_email(form.cleaned_data['email'])

        return super(LandingPageView, self).form_valid(form)
