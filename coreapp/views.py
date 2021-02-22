from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import Http404
from .models import Article, TopFeatured, UserTag
from django.contrib.auth.models import User

from functools import reduce


def article_category(request, category):
    articles = Article.objects.filter(tag = category)
    context = {
        "articles":articles,
    }
    return render(request, "coreapp/category.html", context)


def home_view(request):
    top_featured_article = Article.objects.filter(tag = "topfeatured").first()
    latest_news = Article.objects.all().order_by('-pub_date')[:2]


    if request.user.is_authenticated:
        user_tags = UserTag.objects.filter(user = request.user)
        print("nn"*30, user_tags)
        total_article_queryset = Article.objects.filter(tag = "topfeatured")
        for tag in user_tags:
            total_article_queryset = total_article_queryset | Article.objects.filter(tag = tag)[:3]

        context = {
            "articles":total_article_queryset,
            "top_featured_article":top_featured_article,
            "latest_news":latest_news
        }
        return render(request, "coreapp/home.html", context)

    else:
        articles = Article.objects.all()
        context = {
            "articles":articles,
            "top_featured_article":top_featured_article,
            "latest_news":latest_news
        }
        return render(request, "coreapp/home.html", context)

def article_detail(request, id):
    article = Article.objects.get(id = id)
    context={
        "article":article
    }
    return render(request, "coreapp/article_detail.html", context)

def register_form_view(request):
    if request.user.is_authenticated:
        return redirect("coreapp:home_view")
    else:
        return render(request, "coreapp/register_form.html", {})

#TODO
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        preferences_list =  request.POST.getlist('preferences')

        if User.objects.filter(username = username).count()> 0:
            messages.error(request, f"username already existed, please try another username")
            return redirect("coreapp:register_form_view")

        elif User.objects.filter(email = email).count()> 0:
            messages.error(request, f"email already existed, please try another email")
            return redirect("coreapp:register_form_view")

        # try:
        user = User.objects.create_user(username, email, password)
        authenticated_user = authenticate(request, username=user.username, password=password)

        for tag in preferences_list:
            usertag = UserTag(user = user, name = tag)
            usertag.save()

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("coreapp:home_view")

        # except:
        #     messages.error(request, f"Some thing wrong happened")
        #     return redirect("coreapp:register_form_view")
    else:
        return redirect("coreapp:register_form_view")

    
def login_form_view(request):
    if request.user.is_authenticated:
        return redirect("coreapp:home_view")
    else:
        return render(request, "coreapp/login_form.html", {})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("coreapp:home_view")
        else:
            messages.error(request, f"Invalid credential, please provide correct credentials..")
            # Return an 'invalid login' error message.
            return redirect("coreapp:login_form_view")
    else:
        return redirect("coreapp:login_form_view")

@login_required
def logout_view(request):
    logout(request)
    return redirect("coreapp:login_form_view")