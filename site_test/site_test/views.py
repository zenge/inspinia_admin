#coding:utf-8
#__author__ = 'cengchengpeng'
from django.shortcuts import redirect,render

from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return render(request, 'index.html')



