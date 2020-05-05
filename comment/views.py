from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from comment.models import Comment
from myBlog.models import Article
from comment.form import CommentForm


# 文章评论
@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = request.POST["body"]
            print(content)
            ai = article.id
            ui = request.user.id
            Comment.objects.create(body=content, article_id=ai, CommentUser_id=ui)
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")


@login_required(login_url='/userprofile/login/')
def delete_comment(request, comment_id, article_id):
    target_comment = Comment.objects.filter(id=comment_id)
    article = Article.objects.filter(id=article_id)
    target_comment.delete()
    return redirect(article[0])
