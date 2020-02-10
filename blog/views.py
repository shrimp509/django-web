from django.shortcuts import render

from .forms import PostForm
from .models import Post

def post_create_view(request):
	form = PostForm(request.POST or None)
	print("form valid: ", form.is_valid, ", request: ", request)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, 'blog/post_create.html', context)


# Create your views here.
def hello(request):
	return render(request, 'blog/index.html', {
			"first_var": "Hello Man",
			"second_var": 87.8787,
			"third_list": ["歡迎", "你好", "我是 RS", "來比對我阿"]
		})
