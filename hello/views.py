from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
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

def index(request):
    params = {
        'title':'Hello',
        'message':'all friends.',
        'form':HelloForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)