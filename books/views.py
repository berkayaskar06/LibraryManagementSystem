from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Books
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from barrow.models import Barrow


# Create your views here.
def books_index(request):

    book_list = Books.objects.all()
    query = request.GET.get('q')
    if query:
        book_list = book_list.filter(
            Q(title__icontains=query)|
            Q(author__icontains=query))

    paginator = Paginator(book_list, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'Books/index.html', {'books': books})




def books_update(request,id):
    books = get_object_or_404(Books,id=id)
    form = PostForm(request.POST or None, instance=books)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kitap Başarılı Bir Güncellendi Oluşturuldu.')
        return HttpResponseRedirect(books.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request,'Books/form.html',context)

def books_delete(request,id):
    books = get_object_or_404(Books,id=id)
    books.delete()
    return redirect('index')
def books_create(request):
    form = PostForm()
    context = form = {
        'form':form,
    }

    #title = request.POST.get('title')
    #author = request.POST.get('author')
   # Books.objects.create(title=title,author=author)
    if request.method == 'POST':
        #formdan gelen bilgileri kaydet
        form = PostForm(request.POST)
        if form.is_valid():
            book= form.save()
            messages.success(request,'Kitap Başarılı Bir Şekilde Oluşturuldu.')
            return HttpResponseRedirect(book.get_absolute_url())
    else:
    #formu kullanıcıya göster
        form = PostForm
    context = {
        'form':form,
               }


    return render(request,'Books/form.html',context)


def books_details(request,id):
    books = Books.objects.get(id=id)
    title = books.title
    id = books.id
    author = books.author
    publish = books.publish
    flag = books.flag
    rating = books.rating
    if request.method=='GET':
        flag = True
        barrow=Barrow.objects.create(id=id, title=title, author=author, publish=publish, flag=flag, rating=rating)
        barrow.save()
        messages.success(request,'This Books is Barrowed.You can see in My Books Section')

    return render(request,'Books/detail.html',{'books':books})







