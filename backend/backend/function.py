import json
import jwt
from . import error
from .settings import SECRET_KEY
from django.http.response import JsonResponse


# 检查用户是否已登录的装饰器
def check_login(fn):
    def wrap(request, *args, **kwargs):
        # 检查用户是否已登录(即存在token)
        try:
            str.encode(request.headers.get('token'), 'utf-8')
        except Exception as e:
            print('login error!', e)
            code, message = error.authorization_fail()
            return JsonResponse({
                'message': message,
            }, status=code)
        return fn(request, *args, **kwargs)
    return wrap


def check_method(method):
    def check_method_decorator(fn):
        def wrap(request, *args, **kwargs):
            if request.method != method:
                return JsonResponse({
                    'message': '无法访问此网页',
                }, status=404)
            return fn(request, *args, **kwargs)
        return wrap
    return check_method_decorator


def generate_token(js_code, provider, id):
    token = jwt.encode({
        'js_code': js_code,
        'provider': provider,
        'user_id': id
    }, SECRET_KEY,algorithm='HS256')
    return bytes.decode(token, 'utf-8')


def get_username_by_token(request):
    try:
        token = str.encode(request.headers.get('token'), 'utf-8')
        token_json_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        username = token_json_data.get('user_id')
    except jwt.DecodeError:
        username = None
    except Exception as e:
        print(e)
        username = None

    return username


def get_post_json(request):
    json_data = {}
    if request.content_type == 'application/json':
        temp_json_data = json.loads(request.body)
        if temp_json_data:
            json_data = temp_json_data
    elif request.content_type == 'multipart/form-data':
        temp_json_data = request.POST
        if temp_json_data:
            json_data = temp_json_data
    else:
        temp_json_data = json.loads(request.body)
        if temp_json_data:
            json_data = temp_json_data

    return json_data
