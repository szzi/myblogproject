from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})


def new(request): #new.html 띄워주기
    return render(request,'new.html')

def create(request): #입력받은 내용을 데이터베이스에 집어넣기
    blog = Blog() # Blog 클래스로부터 blog 객체 생성
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # blog 객체의 내용을 데이터베이스에 저장해라.
    return redirect('/blog/'+ str(blog.id)) 