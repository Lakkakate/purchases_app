from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Контроль оплат', 'Пароли личных кабинетов'],
        'obj': {
            'goods': 'Товарный калькулятор',
            'tax': 'Калькулятор НДС',
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
