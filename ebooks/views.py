from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ebook


# Create your views here.

def index(request):
    book_list = Ebook.objects.all()
    return render(request, 'ebooks/index.html', {'book_list': book_list})

def book_details(request, book_id):
    """

    :param request:
    :param book_id:
    :return: Book Details View
    """
    book_info = get_object_or_404(Ebook, pk=book_id)
    return render(request, 'ebooks/details.html', {'book_info': book_info})

