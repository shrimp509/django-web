from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
import json

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


@csrf_exempt
def test_json_response_view(request: WSGIRequest):
	print('-----------------------------------')
	if request.method == 'GET':
		print("get GET request: ", request)
		return JsonResponse({'first': 'content', 'second': 'test'})
	elif request.method == 'POST':
		# get data
		data = json.loads(request.body)
		print("get POST request data: ", data)

		# turn to Post Object
		post = Post(title=data['title'], content=data['content'])
		print("post: ", post)

		# save to db
		Post.objects.create(title=data['title'], content=data['content'])

		# check posts in db
		print('all posts in db: ', Post.objects.all())

		return JsonResponse({'status': 'ok, I got you.'})
	else:
		print("get unknown request: ", request)
		return JsonResponse({'status': 'no, I don\'t know it.'})


# Create your views here.
def hello(request):
	return render(request, 'blog/index.html', {
			"first_var": "Hello Man",
			"second_var": 87.8787,
			"third_list": ["歡迎", "你好", "我是 RS", "來比對我阿"]
		})
