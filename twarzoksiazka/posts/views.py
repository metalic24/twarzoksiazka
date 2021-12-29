from django.shortcuts import render
from .models import Post
from .forms import PostForm
from rej_log.models import User_details

# Create your views here.
def post_com_upload(request):
    post_obj = Post.objects.all()
    
    post_form = PostForm(request.POST or None, request.FILES or None)
    profile = User_details.objects.get(user=request.user)
    
    if post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.author = profile
        instance.save()
        post_form = PostForm()
    
    
    context = {
        'post_obj': post_obj,
        'profile': profile,
        'post_form': post_form,
    }
    
    return render(request, 'posts/post_upload.html', context)