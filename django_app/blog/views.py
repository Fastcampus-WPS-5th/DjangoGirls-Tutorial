from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    # posts변수에 ORM을 이용해서 전체 Post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.all()

    # posts변수에 ORM을 사용해서 전달할 쿼리셋이
    # Post의 published_date가 timezone.now()보다
    # 작은 값을 가질때만 해당하도록 필터를 사용한다
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    )
    context = {
        'title': 'PostList from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)
