from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost


def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all()
    #블로그 모든 글들 대상
    paginator = Paginator(blog_list, 3)
    #블로그 객체 세개를 한페이지로 자르기
    page = request.GET.get('page')
    #request된 페이지가 뭔지를 알아내고
    posts = paginator.get_page(page)
    #request된 페이지를 얻어온 뒤 return해준다 
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'details':details})

def new(request): #new.html띄워주는 함수
    return render(request, 'new.html')

#입력받은 내용 테이터 베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    #str : blog id 는 int기 때문에 url은 항상 str이라서 str으로 형변환후 더해줌 
    #render 과 redirect(안에 url을 받음)의 차이점 
# Create your views here.


def blogpost(request):
    # 1. 입력된 내용 처리 : POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.pub_date = timezone.now() # 나머지는 form.py에서 써줬지~
            post.save()
            return redirect('home')
    # 2. 빈 페이지 띄워주는 기능 : GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})