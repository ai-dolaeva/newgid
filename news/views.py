from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.urls import reverse_lazy
from django.views.generic import CreateView
from news import utils

# Create your views here.
from news.models import RegisterUserForm, LoginUserForm

langArr = [{
    'en': {
        'log': ["log out", 'log in'],
        'delete': "delete the account",
        'menu': ["sort by", "category", "source"],
        'category': ["general", "entertainment", "business", "health",
                     "science", "sports","technology"],
        'source': ['Aeon', 'BBC', 'Bloomberg', 'CNN', 'Forbes', 'Futurism',
                   'Harvard Business Review', 'Inc', 'Independent',
                   'Investopedia', 'Nautilus', 'Quartz', 'Scientific American',
                   'Tech Crunch', 'The Spectator', 'The Times'],
        'sortby': {"relevancy", "popularity", "publishedAt"},
        },
    'ru':{
        'log': ["выйти", 'войти'],
        'delete': "удалить аккаунт",
        'menu': ["сортировка", "категория", "источник"],
        'category': ["общее", "развлечение", "бизнесс", "здоровье", "наука",
                      "спорт", "технология"],
        'source': ['BBC News', 'Colta.ru', 'Deutsche Welle', 'Habr',
                     'Lenta.ru', 'Meduza', 'N+1', 'Sports.ru',
                     'Аргументы и факты', 'Ведомости', 'Газета.ру', 'Дождь',
                     'Известия', 'Коммерсантъ', 'Радио Свобода', 'РБК',
                     'РИА Новости', 'Сноб'],
        'sortby': ["релеватность", "популярность", "публикация"],
        }
}]

def index(request): #httpRequest

    lang = 'ru'
    defultparam = {
        'sortby': 'publishedAt',
        'category': 'general',
        'date': str(date.today()),
        'lan': lang
    }

    texts = ''

    if (request.GET):
        if(request.GET['lan']):
            print('gthj')
            lang = request.GET['lan']
            texts = utils.get_news(request.GET)
        else:
            texts = utils.get_news(defultparam)
    else:
        print('debil')
        texts = utils.get_news(defultparam)

    lansym = 'ru'
    if (lang=='ru'):
        lansym = 'en'
    else:
        lansym = 'ru'

    context = {
        'link': "home",
        'title': 'НовоГид',
        'footer': "© 2021 НовоГид",
        'news': texts,
        'langArr': langArr[0][lang],
        'login': langArr[0][lang]['log'][1],
        'logout': langArr[0][lang]['log'][0],
        'del_acc': langArr[0][lang]['delete'],
        'lang': lansym,
        'sortby': langArr[0][lang]['menu'][0],
        'category': langArr[0][lang]['menu'][1],
        'source': langArr[0][lang]['menu'][2],
        'date': str(date.today()),
        'mindate': str(date.today() - timedelta(days=30))
    }

    return render(request,
                  'news/newsgid.html',
                  context=context)

def about(request): #httpRequest
    return render(request, 'news/about.html', {'title': 'О нас'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Cтраница не найдена</h1>')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'news/auth.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = "home"
        context['title'] = 'Регистрация'
        context['footer'] = "© 2021 НовоГид"
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = "home"
        context['title'] = 'Авторизация'
        context['footer'] = "© 2021 НовоГид"
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')

def delete_user(username):
    u = User.objects.get(username=username.user)
    u.delete()
    return redirect('home')

