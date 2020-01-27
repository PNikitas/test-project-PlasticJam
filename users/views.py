from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import *


def UsersView(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 50)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'users': users,
        'statistics': Statistic.objects.all(),
    }

    return render(request, 'users-page.html', context)


def UserView(request, pk):
    users = User.objects.filter(pk=pk).first()
    if users is not None:
        first_name = users.first_name
        last_name = users.last_name
        email = users.email
        gender = users.gender
        ip_address = users.ip_address

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'gender': gender,
        'ip_address': ip_address,
        'statistics': Statistic.objects.all(),
        'users_id': get_object_or_404(User, pk=pk),
    }

    return render(request, 'user-page.html', context)