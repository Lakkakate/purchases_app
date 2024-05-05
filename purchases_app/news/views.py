from django.shortcuts import render, redirect
from .models import Artecles
from .forms import ArteclesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.

def news_home(request):
    news = Artecles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artecles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Artecles
    template_name = 'news/create.html'
    form_class = ArteclesForm

class NewsDeleteView(DeleteView):
    model = Artecles
    success_url = '/news'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArteclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong form'
    form = ArteclesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)