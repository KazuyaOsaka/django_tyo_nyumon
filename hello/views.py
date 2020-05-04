from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

# Create your views here.

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'message':'your data',
            'form':HelloForm(),
            'result':None,
            'result2':None,
            'result3':None
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'あたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')' + '</b> さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'

        ch = request.POST['choice']

        ra = request.POST['radio']

        se = request.POST['select']

        ms = request.POST.getlist('multiple_select')
        result3 = '<ol><b>multiple_selected:</b>'
        for item in ms:
            result3 += '<li>' + item + '</li>'
        result3 += '</ol>'

        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        if ('check' in request.POST):
            self.params['result'] = 'Checked!'
        else:
            self.params['result'] = 'not checked ...'
        self.params['result2'] =  'selected:' + ch + '<br>radio:' + ra + '<br>select:' + se
        self.params['result3'] =  'multiple_select:' + result3
        return render(request, 'hello/index.html', self.params)