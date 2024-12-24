from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie, requires_csrf_token
from django.middleware.csrf import get_token
from .database_handler import (create_user, user_login, create_category, get_categories,
                                create_sub_category, get_sub_categories, create_application, get_application,
                                get_applications, download_application, get_user_data, get_completed_tasks,
                                get_remaining_tasks)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@ensure_csrf_cookie
def csrf(request):
    if request.method =='GET':
        return HttpResponse(json.dumps({'csrftoken': 'set succesfully'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)


@requires_csrf_token
def signup(request):
    if request.method == 'POST':
        # name = request.body['name']
        # print(request.body)
        user_data = request.POST.get('user_data', None)
        user_data = json.loads(user_data)
        profile_picture = request.POST.get('profile_pic', None)
        resp = create_user(user_data, profile_picture)

        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def login(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        email = user_data['email']
        password = user_data['password']
        admin = user_data['admin']
        resp = user_login(email, password, admin)
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def createCategory(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        category_name = request.POST['category_name']
        resp = create_category(category_name, email)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def createSubCategory(request):
    if request.method == 'POST':
        email = request.POST['email']
        category_name = request.POST['category_name']
        subcategory_name = request.POST['subcategory_name']
        resp = create_sub_category(subcategory_name, category_name, email)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)


@requires_csrf_token
def getCategories(request):
    if request.method == 'GET':
        resp = get_categories()
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def getSubCategories(request):
    if request.method == 'POST':
        category_data = json.loads(request.body)
        category_id = category_data['category_id']
        resp = get_sub_categories(category_id)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def createApplication(request):
    if request.method == 'POST':
        app_details = json.loads(request.POST.get('app_details', None))
        app_image = request.POST.get('app_image', None)
        resp = create_application(app_details, app_image)
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def getApplication(request):
    if request.method == 'GET':
        app_name = request.GET.get('app_name')
        app_id = request.GET.get('app_id')
        resp = get_application(app_name, app_id)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        app_name = data['app_data']['app_name']
        app_id = data['app_data']['app_id']
        email = data['user_data']['email']
        resp = get_application(app_name, app_id, email)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def getApplications(request):
    if request.method == 'GET':
        resp = get_applications()
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def downloadApplication(request):
    if request.method == 'POST':
        user_data = json.loads(request.POST['user_data'])
        app_data = json.loads(request.POST['app_data'])
        screenshot = request.POST['screenshot']
        resp = download_application(user_data['email'], app_data['app_id'], screenshot)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def getUserData(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        email = user_data['email']
        resp = get_user_data(email)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def getCompletedTasks(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        email = user_data['email']
        resp = get_completed_tasks(email)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)

@requires_csrf_token
def getRemainingTasks(request):
    if request.method =='POST':
        user_data = json.loads(request.body)
        email = user_data['email']
        resp = get_remaining_tasks(email)
        return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
    else:
        return HttpResponse(json.dumps({'message': 'Bad Request'}), content_type="application/json", status=400)
