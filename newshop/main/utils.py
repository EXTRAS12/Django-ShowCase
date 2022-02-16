from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import OrderForm


class MixinForm(object):
    """Отправка заявки на почту"""
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                subject = "Новая заявка!"
                body = {
                    'name': form.cleaned_data['name'],
                    'phone': form.cleaned_data['phone'],
                    'area': form.cleaned_data['area'],
                    'city': form.cleaned_data['city'],
                    'adres': form.cleaned_data['adres'],
                    'prodname': form.cleaned_data['prodname'],
                }
                message = "\n".join(body.values())
                try:
                    send_mail(subject, message,
                              'info.moonshine@yandex.ru',
                              ['intfloatwork@yandex.ru'])
                except BadHeaderError:
                    return HttpResponse('Найден некорректный заголовок')
                return redirect("thanks")

