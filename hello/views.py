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
            'result':None
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'あたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')' + '</b> さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'
        
        ch = request.POST['choice']

        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        if ('check' in request.POST):
            self.params['result'] = 'Checked!<br>' + '</br>selected:' + ch
        else:
            self.params['result'] = 'not checked ...<br>' + '</br>selected:' + ch
        return render(request, 'hello/index.html', self.params)