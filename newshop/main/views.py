from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import ContactForm, OrderForm
from .models import Category, Product


class Home(ListView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        form = OrderForm(request.POST or None)
        context = {
            'categories': categories,
            'products': products,
            'form': form
        }
        return render(request, 'base.html', context)

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
        form = OrderForm()
        return render(request, "base.html", {'form': form})


class CategoryByProducts(ListView):

    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        categories = Category.objects.all()
        products = Product.objects.filter(category__slug=self.kwargs['slug'])
        context = {
            'categories': categories,
            'products': products,
            'form': form,
        }
        return render(request, 'main/index.html', context)

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
        form = OrderForm()
        return render(request, "main/index.html", {'form': form})


class ProductDetailView(DetailView):
    form_class = OrderForm
    model = Product
    template_name = 'main/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = OrderForm
        return context

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
        form = OrderForm()
        return render(request, "main/detail.html", {'form': form})


class Search(ListView):
    form_class = OrderForm
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'products'

    def get_queryset(self):  # новый
        return Product.objects.filter(name__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = OrderForm
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

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
        form = OrderForm()
        return render(request, "main/search.html", {'form': form})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Сообщение"
            body = {
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'extra-kent@mail.ru',
                          ['intfloatwork@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("home")

    form = ContactForm()
    return render(request, "main/contacts.html", {'form': form})


def thanks(request):
    return render(request, 'main/thanks.html')
