from django.shortcuts import render
from django.db import models
from django.http import HttpResponseRedirect
from prospect.models import Agent, Listing
from django.core.paginator import Paginator


def index(request):
    return render(request, "prospect/index.html")


def marketing(request):
    return render(request, "prospect/marketing.html")


def clients(request):
    return render(request, "prospect/clients.html")


def agents(request):
    return render(request, "prospect/agents.html")


def saved(request):
    return render(request, "prospect/saved.html")


def seen(request):
    return render(request, "prospect/seen.html")


def prospecting(request):
    listing = Listing.objects.all().filter(seen=False)
    paginator = Paginator(listing, 1)
    page_number = request.GET.get('page')
    listing_obj = paginator.get_page(page_number)
    return render(request, "prospect/prospect.html", {
        'listings': listing_obj
    })
