from django.shortcuts import render, redirect
from .models import Post, Like
from .forms import PostForm, CommentForm
from rej_log.models import User_details

# Create your views here.
def post_com_upload(request):
    post_obj = Post.objects.all()
    
    
    profile = User_details.objects.get(user=request.user) 
    post_form = PostForm()
    com_form = CommentForm()
    
    
    if 'submit_post_form' in request.POST:
        print(request.POST)
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = profile
            instance.save()
            post_form = PostForm()
    
    if 'submit_com_form' in request.POST:
        com_form = CommentForm(request.POST)    
        if com_form.is_valid():
            instance = com_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            com_form = CommentForm()
    
    
    context = {
        'post_obj': post_obj,
        'profile': profile,
        'post_form': post_form,
        'com_form': com_form,
    }
    
    return render(request, 'posts/post_upload.html', context)

def like_unlike(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = User_details.objects.get(user=user)
        
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
            
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
                
            post_obj.save()
            like.save()
    return redirect('posts:post-com-upload')