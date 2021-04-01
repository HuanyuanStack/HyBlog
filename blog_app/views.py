from django.shortcuts import render

from django.http import HttpResponse
from .models import User, Address

import datetime


def index(request):
    address_list = Address.objects.all()
    for address in address_list:
        address.user.create_date = address.user.create_date.strftime("%Y/%m/%d")
        address.user.update_date = address.user.update_date.strftime("%Y/%m/%d")
    return render(request, 'blog_app/index.html', {
        'address_list': address_list
    })


def go_add_user(request):
    return render(request, 'blog_app/detail.html')


def add_user(request):
    nickname = request.POST['nickname']
    country = request.POST['country']
    address = request.POST['address']

    try:
        user = User()
        user.nickname_text = nickname
        user.update_date = datetime.datetime.now()
        user.save()

        addr = Address()
        addr.country_text = country
        addr.address_text = address
        addr.user = user
        addr.save()
    except KeyError:
        return render(request, 'blog_app/detail.html', {
            'error_message': "保存数据错误！！"
        })
    else:
        address_list = Address.objects.all()
        for address in address_list:
            address.user.create_date = address.user.create_date.strftime("%Y/%m/%d")
            address.user.update_date = address.user.update_date.strftime("%Y/%m/%d")
        return render(request, 'blog_app/index.html', {
            'address_list': address_list
        })
