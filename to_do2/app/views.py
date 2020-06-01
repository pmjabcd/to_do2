from django.shortcuts import render, redirect
from .models import Post, Comment
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    index = Post.objects.all().order_by("due_date")
    return render (request, 'index.html', {'index' : index})


# 여기 골뱅이 추가해준 이유는, 로그인을 한 사람만 글을 쓸 수 있게 해주는 것을 의미
@login_required(login_url='/registration/login')
def new (reuqest): 
    if request.method == 'POST':
        # print (request.POST)
        new = Post.objects.create(
            title = request.POST ['title'],
            content = request.POST ['content'],
            due_date = request.POST ['due_date'],
            author = request.user
        )

        return redirect ('detail', new.pk)
    else:
        return render (request, 'new.html')


    # 위에서 request를 이렇게 해석하면 될 듯.
    # request를 받은 method가 'POST'라면
    # print (request.POST)는 아래와 같이 해
    # *** 우선 models.py에서 데이터 불러와서 / new니까 만들어줘야지 
    # ex) request를 받은 / 저장 받식의 / title은 -> 어디에 담고 ~~ 

    # post (저장) 만약 저장 방식이 맞으면, return redirect (detail 경로로 가줘 -> 그리고 새롭게 생긴 new.pk는 ''라고 이름을 담을게)
    # get (열기) 만약 저장 방식이 그냥 get이라면 new.html을 열어줘 

def detail(request,post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        Comment.objects.create(
            post = post,
            content = request.POST['contnet'],
            author = request.user
        )
        return redirect ('detail', new.pk)
    return render (request, 'detail.html', {'post':post})

# question) 여기서 detail.html은 왜 열어주는거징
# detail 화면은 우선 글들 있는 곳이니, 다 불러왔고 / 여기에 comment도 있으니 생성/
# 댓글을 Post 방식으로 저장하는거면 '그 글(pk)'에 댓글이 달리는거니 detail 불러오고
# ㅡ만약 저장이 아니라 그냥 댓글 불러오는거면.... html을 왜 ㅠㅠ?

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            due_date = request.POST['due_date']
        )
        return redirect ('detail', post_pk)
    return render(request, 'edit.html', {'post' : post})

# question) 여기서도 edit.html 템플릿을 왜 불러오는걸까

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('index')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = "이미 존재하는 이름입니다"
            return render(request, 'registration/signup.html', {'error' : error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = "아이디 또는 비밀번호가 틀렸습니다."
            return render(request, 'registration/login.html', {'error' : error})

        auth.login(request, found_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next','/'))
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def my_post_list(request):
    posts = Post.objects.all().order_by("due_date")
    return render(request, 'my_post_list.html', {'posts' : posts})