from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import NATO_Member, Country, News, InfoNATO, Story
from .forms import CountryForm, NewsForm, NATOInfoForm, StoryForm, DeleteStoryForm, EditStoryForm

def index(request):
    return render(request, 'index.html')

def story(request):
    stories = Story.objects.all()
    return render(request, 'story.html', {'stories': stories})

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'story_list.html', {'stories': stories})

def members_list(request):
    members = NATO_Member.objects.all()
    return render(request, 'members/members_list.html', {'members': members})

def country_info(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, 'country_info.html', {'country': country})

def all_countries(request):
    countries = Country.objects.all()
    return render(request, 'all_countries.html', {'countries': countries})

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, pk):
    news_item = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})

def info_nato_list(request):
    info_nato_list = InfoNATO.objects.all()
    return render(request, 'info_nato_list.html', {'info_nato_list': info_nato_list})

def info_nato_detail(request, info_nato_id):
    info_nato = InfoNATO.objects.get(pk=info_nato_id)
    return render(request, 'info_nato_detail.html', {'info_nato': info_nato})

def add_country_view(request):
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {'form': form})

def edit_country_view(request, country_id):
    country = NATO_Member.objects.get(id=country_id)
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'edit_country.html', {'form': form})

def delete_country_view(request, country_id):
    country = get_object_or_404(NATO_Member, id=country_id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            country.delete()
            messages.success(request, 'Country successfully deleted.')
            return redirect('members_list')
        else:
            form = CountryForm(request.POST, request.FILES, instance=country)
            if form.is_valid():
                form.save()
                return redirect('all_countries')
    else:
        form = CountryForm(instance=country)
    return render(request, 'delete_country.html', {'form': form, 'country': country})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

def edit_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news_item)
    return render(request, 'edit_news.html', {'form': form})

def delete_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_item.delete()
        return redirect('news_list')
    return render(request, 'delete_news.html', {'news_item': news_item})

def add_nato_info(request):
    if request.method == 'POST':
        form = NATOInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('info_nato_list')
    else:
        form = NATOInfoForm()
    return render(request, 'add_nato_info.html', {'form': form})

def edit_nato_info(request, info_id):
    info_nato = get_object_or_404(InfoNATO, id=info_id)
    if request.method == 'POST':
        form = NATOInfoForm(request.POST, request.FILES, instance=info_nato)
        if form.is_valid():
            form.save()
            return redirect('info_nato_list')
    else:
        form = NATOInfoForm(instance=info_nato)
    return render(request, 'edit_nato_info.html', {'form': form})

def delete_nato_info(request, info_id):
    info_nato = get_object_or_404(InfoNATO, id=info_id)
    if request.method == 'POST':
        info_nato.delete()
        return redirect('info_nato_list')
    return render(request, 'delete_nato_info.html', {'info_nato': info_nato})


def add_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story_list')
    else:
        form = StoryForm()
    
    return render(request, 'add_story.html', {'form': form})


def delete_story(request):
    if request.method == 'POST':
        form = DeleteStoryForm(request.POST)
        if form.is_valid():
            story_id = form.cleaned_data['story_id']
            Story.objects.filter(pk=story_id).delete()
            return redirect('story_list')
    return redirect('story_list')


def edit_story(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.method == 'POST':
        form = EditStoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('story_list')
    else:
        form = EditStoryForm(instance=story)
    
    return render(request, 'edit_story.html', {'form': form})


