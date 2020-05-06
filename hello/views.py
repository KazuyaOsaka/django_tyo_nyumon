from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import  QuerySet
from .forms import HelloForm, FriendForm
from .models import Friend

# Create your views here.


# 2章の内容===============================

# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title':'Hello',
#             'message':'your data',
#             'form':HelloForm(),
#             'result':None,
#             'result2':None,
#             'result3':None
#         }

#     def get(self, request):
#         return render(request, 'hello/index.html', self.params)

#     def post(self, request):
#         msg = 'あたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')' + '</b> さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'

#         ch = request.POST['choice']

#         ra = request.POST['radio']

#         se = request.POST['select']

#         ms = request.POST.getlist('multiple_select')
#         result3 = '<ol><b>multiple_selected:</b>'
#         for item in ms:
#             result3 += '<li>' + item + '</li>'
#         result3 += '</ol>'

#         self.params['message'] = msg
#         self.params['form'] = HelloForm(request.POST)
#         if ('check' in request.POST):
#             self.params['result'] = 'Checked!'
#         else:
#             self.params['result'] = 'not checked ...'
#         self.params['result2'] =  'selected:' + ch + '<br>radio:' + ra + '<br>select:' + se
#         self.params['result3'] =  'multiple_select:' + result3
#         return render(request, 'hello/index.html', self.params)


# ここから3章の内容！===============================

# 3-15------------
# def index(request):
#     params = {
#         'title':'Hello',
#         'message':'all friends.',
#         'form':HelloForm(),
#         'data':[],
#     }
#     if (request.method == 'POST'):
#         num = request.POST['id']
#         item = Friend.objects.get(id=num)
#         params['data'] = [item]
#         params['form'] = HelloForm(request.POST)
#     else:
#         params['data'] = Friend.objects.all()
#     return render(request, 'hello/index.html', params)

# 3-22------------
# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' +str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result

# QuerySet.__str__ = __new_str__

# 3-16------------
# def index(request):
#     # data = Friend.objects.all()
#     # data = Friend.objects.all().values()
#     data = Friend.objects.all().values('id', 'name', 'age')
#     # # data = Friend.objects.all().values_list()
#     # num = Friend.objects.count()
#     # first = Friend.objects.first()
#     # last = Friend.objects.last()
#     # data = [num, first, last]
#     params = {
#         'title':'Hello',
#         'data':data,
#     }
#     return render(request, 'hello/index.html', params)


# 3-27------------
def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)



# def create(request):
#     params = {
#         'title':'Hello',
#         'form':HelloForm(),
#     }
#     if (request.method == 'POST'):
#         # まず変数に入力された値を突っ込む
#         name = request.POST['name']
#         mail = request.POST['mail']
#         gender = 'gender' in request.POST
#         age = request.POST['age']
#         birth = request.POST['birthday']
#         # 値を突っ込んだ変数をもとにレコード（インスタンス）を作る
#         friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth)
#         # インスタンスをsaveメソッドでDBに登録する
#         friend.save()
#         # ポストの場合はsaveしてページを変える
#         return redirect(to='/hello')
#     else:
#         return render(request, 'hello/create.html', params)

def create(request):
    if (request.method == 'POST'):
        # モデルのクラスのインスタンスを作る
        obj = Friend()
        # モデルのクラスのインスタンスとリクエストの中身をがっちゃんこしてモデルフォームクラスのインスタンスを作る
        friend = FriendForm(request.POST, instance=obj)
        # モデルフォームクラスのインスタンスをsaveする
        friend.save()
        return redirect(to='/hello')
    else:
        params = {
            'title':'Hello',
            'form':FriendForm(),
        }
        return render(request, 'hello/create.html', params)
