from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from books.models import Books

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Barrow
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


# Create your views here.
# @cache_page(CACHE_TTL)
def barrowed_index(request):

    barrow_list = Barrow.objects.all()
    query = request.GET.get('q')
    if query:
        book_list = barrow_list.filter(
            Q(title__icontains=query)|
            Q(author__icontains=query))

    paginator = Paginator(barrow_list, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    barrow = paginator.get_page(page_number)
    return render(request, 'myBooks/listing.html', {'barrows':barrow})


def return_barrow(request,id):
    book = Books.objects.get(id=id)
    if request.method == 'GET':
        Books.objects.filter(id=id).update(flag=False)
        book.refresh_from_db()
        books = Barrow.objects.get(id=id)
        books.delete()


    return redirect('/books/index/')
