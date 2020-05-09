from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from comment.models import Comment
from .models import Article, Category, Banner, Tag, Link


# Create your views here.

def index(request):
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    banner = Banner.objects.filter(is_active=True)[0:4]  # 查询所有幻灯图数据，并进行切片
    shouyetui = Article.objects.filter(tui__id=1)[:3]
    rementui = Article.objects.filter(tui_id=2)[:6]
    articles = Article.objects.order_by('-id')[0:10]
    hot = Article.objects.order_by('views')[:10]
    allTag = Tag.objects.all()
    link = Link.objects.all()
    # 把查询出来的分类封装到上下文里
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'shouyetui': shouyetui,
        'rementui': rementui,
        'articles': articles,
        'hot': hot,
        'allTag': allTag,
        'link': link,
    }
    return render(request, 'index.html', context)  # 把上下文传到index.html页面


# 列表页
def list(request, lid):
    list = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名
    rementui = Article.objects.filter(tui__id=2)[:6]  # 右侧的热门推荐
    allcategory = Category.objects.all()  # 导航所有分类
    allTag = Tag.objects.all()  # 右侧所有文章标签
    hot = Article.objects.order_by('views')[:10]
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'list.html', locals())


# 内容页
def show(request, sid):
    comments = Comment.objects.filter(article=sid)
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    hot = Article.objects.order_by('views')[:10]
    allTag = Tag.objects.all()  # 右侧所有标签
    rementui = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章
    rementui = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    hot = Article.objects.order_by('views')[:10]
    page = request.GET.get('page')
    allTag = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(Q(title__icontains=ss) | Q(excerpt__icontains=ss))  # 获取到搜索关键词通过标题进行匹配
    rementui = Article.objects.filter(tui__id=2)[:6]
    hot = Article.objects.order_by('views')[:10]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    allTag = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())


def page_not_found(request, exception=404):
    return render(request, '404.html')
