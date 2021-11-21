from django.shortcuts import render
from django.contrib import admin , messages
from django.http.response import Http404, HttpResponseBadRequest , HttpResponseRedirect
from django.core.paginator import Paginator
from polls.forms import *
from polls.models import *
# import datetime

# Create your views here.

def Home (request):
    courses = Courses.objects.all()
    blogs = Blog.objects.all()
    student = Student_comment.objects.all()
    context = {'courses':courses , 'blog':blogs,'student':student,'home':'home'}
    return render(request , 'index.html',context)

def contact_ (request):
    Course = Courses.objects.filter(available = True)
    form = contactform(request.POST or None)

    if form.is_valid():
        form.save()
        messages.warning(request,'We will contact you soon')
        return HttpResponseRedirect('/Contact')

    context = {'form': form,'courses':Course,'contact':'contact'}

    return render(request, 'page-contact.html', context)

def Courses_ (request):
    Course = Courses.objects.filter(available = True)
    paginator = Paginator(Course, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for i , s , h in zip(Course.values_list('end_day',flat=True),Course.values_list('id',flat=True),Course.values_list('available',flat=True)) :
    #     if h :
    #         start = []
    #         stop = []
    #         for k , j in zip(str(str(i).split()[0]).split('-') ,str(str(datetime.datetime.now()).split()[0]).split('-') ):
    #             start.append(j)
    #             stop.append(k)
    #         if int(start[0]) >= int(stop[0]) and int(start[1]) >= int(stop[1]) and int(start[2]) >= int(stop[2]) :
    #             Courses.objects.filter(id = s).update(available = True)
    context = {'page_obj':page_obj,'course':'course'}
    return render(request , 'shop.html',context)

def Courses_single (request , id) :
    a = Courses.objects.all()
    Course = Courses.objects.filter(available = True)
    course = Courses.objects.filter( id = id )
    context = {'a':a,'course':course,'Course':Course}
    return render (request , 'shop-single.html' , context)

def Blogs_(request):
    Course = Courses.objects.filter(available = True)
    blogs_pop = Blog.objects.all().order_by('-click')
    Blogs = Blog.objects.all()
    paginator = Paginator(Blogs, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'Course':Course,'blogs_pop':blogs_pop,'blog_':'blog'}
    return render(request,'blog.html',context)

def single_blog (request , id):
    a = Blog.objects.get(id = id)
    a.click = a.click + 1
    a.save()
    blogs_pop = Blog.objects.all().order_by('-click')
    Course = Courses.objects.filter(available = True)
    blogs = Blog.objects.filter(id = id )
    context = {'blog':blogs,'Course':Course,'blogs_pop':blogs_pop}
    return render(request , 'blog-single.html',context)
