from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Blog, Comment

@login_required
def home_view(request):
    # Fetch blogs in descending order by creation date
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_app/home.html', {'blogs': blogs})

# Create a new blog
@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Blog.objects.create(author=request.user, title=title, content=content)
        return redirect('home')
    return render(request, 'blog_app/create_blog.html')

# Update a blog
@login_required
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return HttpResponseForbidden("You are not authorized to edit this blog.")
    
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_detail', blog_id=blog.id)
    return render(request, 'blog_app/update_blog.html', {'blog': blog})

# Delete a blog
@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return HttpResponseForbidden("You are not authorized to delete this blog.")
    
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blog_app/delete_blog.html', {'blog': blog})

# Increment view count
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    # Increment view count
    if not request.session.get(f'viewed_blog_{blog.id}', False):
        blog.views += 1
        blog.save()
        request.session[f'viewed_blog_{blog.id}'] = True  # Store in session to avoid multiple views in the same session
    
    comments = blog.comments.all()
    return render(request, 'blog_app/blog_detail.html', {'blog': blog, 'comments': comments})

# Like/unlike a blog
@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)  # Unlike
    else:
        blog.likes.add(request.user)  # Like
    return redirect('blog_detail', blog_id=blog.id)

# Update a comment
@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment.text = request.POST['text']
        comment.save()
        return redirect('blog_detail', blog_id=comment.blog.id)
    return render(request, 'blog_app/update_comment.html', {'comment': comment})

# Delete a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog_detail', blog_id=comment.blog.id)
    return render(request, 'blog_app/delete_comment.html', {'comment': comment})
