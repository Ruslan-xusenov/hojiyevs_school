from django.contrib import messages
from django.forms import Form
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import logout
from online_site_app import models
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from .models import News
from online_site_app import forms

def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')

def news_list(request):
    news = News.objects.all()
    query = request.GET.get('q')
    if query:
        from django.db.models import Q
        news = news.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'news_list.html', {'news_list': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'main/news_detail.html', {'news': news})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            messages.success(request, 'Xabaringiz yuborildi!')
            return redirect('contact')
        else:
            print("XATOLAR:", form.errors)
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def location(request):
    return render(request, 'main/location.html')