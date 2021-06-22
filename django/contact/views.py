from django.core.mail import mail_admins
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            mail_admins(
                'New contact form response',
                render_to_string('emails/response.txt', {
                    'response': form.cleaned_data,
                }),
                fail_silently=False,
                html_message=render_to_string('emails/response.html', {
                    'response': form.instance,
                })
            )
            return HttpResponseRedirect(reverse('contact-thanks'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
