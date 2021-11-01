from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    phone = forms.CharField(label='Номер Вашего телефона', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    email = forms.EmailField(label='Ваша электронная почта', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите электронную почту'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5, 'placeholder': 'Задайте вопрос'}))


class OrderForm(forms.Form):
    name = forms.CharField(label='Ф. И. О',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}))
    phone = forms.CharField(label='Номер Вашего телефона:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}))
    area = forms.CharField(label='Область:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Московская'}))
    city = forms.CharField(label='Город:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Москва'}))
    adres = forms.CharField(label='Ваш адрес:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Улица, дом №, кв №'}))
    prodname = forms.CharField(label='Товар:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'value': '{{ item.name }}'}))
