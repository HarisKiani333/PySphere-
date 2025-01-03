from django.shortcuts import render
# Create your views here.
book_list = [
    {'author': 'Chinua Achebe', 'title': 'Things Fall Apart', 'genre': 'Fiction', 'year': '1958'},
    {'author': 'Hans Christian Andersen', 'title': 'Fairy tales', 'genre': 'Fiction', 'year': '1835'},
    {'author': 'Dante Alighieri', 'title': 'The Divine Comedy', 'genre': 'Fiction', 'year': '1315'},
]



def home(request):
    context = {
        'books' : book_list

    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'books' : book_list

    }
    return render(request,'blog/about.html',context)