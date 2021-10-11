from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category


class Home(ListView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'categories': categories,
            'products': products,

        }
        return render(request, 'base.html', context)


class CategoryByProducts(ListView):
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Search(ListView):
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'products'

    def get_queryset(self):  # новый
        return Product.objects.filter(name__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
