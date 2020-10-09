from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action
from common.decorators import ajax_required


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            create_action(request.user, 'bookmarked image', new_item)
            messages.success(request, 'Image added successfully')

            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
        return render(request, 'images/image/create.html', {
            'section': 'images',
            'form': form,
        })


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    is_liked = request.user in image.users_like.all()
    return render(request, 'images/image/detail.html',  {
        'section': 'images',
        'image': image,
        'is_liked': is_liked,
    })


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 2)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        images = paginator.page(paginator.num_pages)
    context = {
        'section': 'images',
        'images': images,
    }
    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html', context)
    return render(request, 'images/image/list.html', context)
