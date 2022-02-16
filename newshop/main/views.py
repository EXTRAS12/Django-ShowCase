from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import ContactForm, OrderForm
from .models import Category, Product
from .utils import MixinForm


class Home(ListView, MixinForm):
    """Главная страница"""
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all().select_related('category')
        form = OrderForm(request.POST or None)
        context = {
            'categories': categories,
            'products': products,
            'form': form
        }
        return render(request, 'base.html', context)


class CategoryByProducts(ListView, MixinForm):
    """Страница товара по категориям"""
    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        categories = Category.objects.all()
        products = Product.objects.filter(category__slug=self.kwargs['slug'])\
            .select_related('category')
        context = {
            'categories': categories,
            'products': products,
            'form': form,
        }
        return render(request, 'main/index.html', context)


class ProductDetailView(DetailView, MixinForm):
    """Страница конкретного товара"""
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


class Search(ListView, MixinForm):
    """Страница поиска"""
    form_class = OrderForm
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('s'))\
            .select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['form'] = OrderForm
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


def contacts(request):
    """Страница контакты"""
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
    """Страница спасибо"""
    return render(request, 'main/thanks.html')
