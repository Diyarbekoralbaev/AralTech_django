from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutModel, ServicesModel, PortfolioModel, TeamModel, BlogModel, AwardsModel, CounterModel, \
    ContactModel


def home(request):
    about = AboutModel.objects.first()
    services = ServicesModel.objects.all()
    portfolio = PortfolioModel.objects.filter(status='PUBLISHED')
    team = TeamModel.objects.all()
    blog = BlogModel.objects.all()
    awards = AwardsModel.objects.all()
    counter = CounterModel.objects.first()
    context = {
        'about': about,
        'services': services,
        'portfolio': portfolio,
        'team': team,
        'blog': blog,
        'awards': awards,
        'counter': counter
    }
    return render(request, 'index.html', context)


def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactModel.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('home')
    else:
        return redirect('home')


def about(request):
    about = AboutModel.objects.first()
    context = {
        'about': about
    }
    return render(request, 'about.html', context)


def portfolio_detail(request, pk):
    portfolio = get_object_or_404(PortfolioModel, pk=pk, status='PUBLISHED')
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio-details.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog-single.html', context)


def custom_404(request):
    return render(request, '404.html', status=404)