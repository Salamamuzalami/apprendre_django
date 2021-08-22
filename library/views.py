from django.shortcuts import render

from . models import Book


def book_view(request):
    books=  Book.objects.all()
    context={"books":books}
    return render(request,"library/home.html",context)

