from django.shortcuts import render
from collections import Counter
# Create your views here.

def index(request):
    context = {}
    if request.method == 'post' and request.FILES['file1']:
        list_words = list()
        file1 = request.FILES['file1']
        data = file1.read()
        print(data)
        for words in data:
            c = Counter(words.split())
            for k, v in c.items():
                if v >= 1 and len(list_words) < 3:
                    list_words.append(k)
        context['data'] = list_words

    return  render(request, "demo/index.html", context)