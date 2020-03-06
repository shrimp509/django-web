from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
import json

from django.http import HttpResponse
import random

from .models import Product


def delect_view(request):
    product = Product.objects.get(id=1)
    product.delete()
    return HttpResponse('刪除 id=1 的資料成功，請到 SQL shell 下指令\nsql> select * from product')


def modify_view(request):
    product = Product.objects.get(id=1)
    product.name = "我是後來才修改的產品"
    product.save()
    return HttpResponse('修改完成，到 Mongo Compass 確認資料')


def lookup_view(request):
    result = Product.objects.all()
    mlist = []
    for item in result:
        content = {"product name": item.name, "price": float(item.price)}
        mlist.append(content)

    return HttpResponse(mlist)

def insert_view(request):
    for i in range(5):
        product = Product()
        product.name = "測試" + str(random.randint(0, 5))
        product.price = random.randint(1, 500)
        product.save()

    return HttpResponse("批次新增資料完成")


def shop_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg',
        'products': list(Product.objects.all())
    }
    return render(request, 'shop/shop.html', context)


def product_view(request):
    context = {
        'bg_6': '/static/images/bg_6.jpg'
    }
    return render(request, 'shop/product-single.html', context)


def about_view(request):
	context = {
		'bg_6': '/static/images/bg_6.jpg',
		'bg_2': '/static/images/bg_2.jpg',
		'bg_4': '/static/images/bg_4.jpg',
		'person_1': '/static/images/person_1.jpg',
		'person_2': '/static/images/person_2.jpg',
		'person_3': '/static/images/person_3.jpg',
	}
	return render(request, 'shop/about.html', context)


def cart_view(request):
	context = {
		'bg_6': '/static/images/bg_6.jpg',
		'product_3': '/static/images/product-3.jpg',
		'product_4': '/static/images/product-4.jpg',
	}
	return render(request, 'shop/cart.html', context)


def checkout_view(request):
	context = {
		'bg_6': '/static/images/bg_6.jpg',

	}
	return render(request, 'shop/checkout.html', context)


'''
def post_create_view(request):
	form = PostForm(request.POST or None)
	print("form valid: ", form.is_valid, ", request: ", request)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, 'shop/post_create.html', context)


@csrf_exempt
def test_json_response_view(request: WSGIRequest):
	print('-----------------------------------')
	if request.method == 'GET':
		print("get GET request: ", request)
		return JsonResponse({'first': 'content', 'second': 'test'})
	elif request.method == 'POST':
		# get json data
		data = json.loads(request.body)
		print("get POST request data: ", data)

		# save to db
		Post.objects.create(title=data['title'], content=data['content'])

		# check posts in db
		print('all posts in db: ', Post.objects.all())

		return JsonResponse({'status': 'ok, I got you.'})
	else:
		print("get unknown request: ", request)
		return JsonResponse({'status': 'no, I don\'t know it.'})


def hello(request):
	return render(request, 'shop/index.html', {
			"first_var": "Hello Man",
			"second_var": 87.8787,
			"third_list": ["歡迎", "你好", "我是 RS", "來比對我阿"]
		})
'''
