from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CarForm
from .models import Car
# from .models import Page
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def home_view(request):
    context = {
        'title': 'Welcome To Audi Market ',
    }
    return render(request, 'index.html', context)


def create_item(request):
    form = CarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj_form = form.save(commit=False)
        # print form.cleaned_date.get('title')
        obj_form.save()
        # message successfully created
        messages.success(request, 'Your page has been created ')
        return HttpResponseRedirect(obj_form.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'create_item.html', context)


def detail_item(request, slug=None):
    instance = get_object_or_404(Car, slug=slug)
    context = {
        'name': instance.car_name,
        'instance': instance
    }
    return render(request, 'detail_item.html', context)


def list_items(request):
    query_set_list = Car.objects.all().order_by('-create_date')
    paginator = Paginator(query_set_list, 5)
    page_num = 'page'
    page = request.GET.get(page_num)
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_set = paginator.page(paginator.num_pages)
    context = {
        'object_list': query_set,
        'title': 'Audi Models',
        'page_num': page_num,
    }
    return render(request, 'item_list.html', context)


@login_required
def update_item(request, slug=None):
    instance = get_object_or_404(Car, slug=slug)
    form = CarForm(request.POST or None,
                   request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # print form.cleaned_date.get('car_name')
        instance.save()
        # message successfully updated
        messages.success(request, 'Your page has been updated ')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'name':        instance.car_name,
        'model':        instance.car_model,
        'instance':     instance.content,
        'form':         form,
        'image':        instance.image,
        'slug':         instance.slug,
    }
    return render(request, 'update_item.html', context)


def delete_item(request, slug=None):
    instance = get_object_or_404(Car, slug=slug)
    instance.delete()
    messages.success(request, 'The page has been Deleted ')
    return redirect('items:item_list')
