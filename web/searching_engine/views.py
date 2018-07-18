from django.shortcuts import render
from .crawler import Crawler
from .models import Indexes
from . import indexer


def index(request):
    return render(request, 'index.html')


def search(request):
    word = request.POST['input_field']

    splited = word.split()
    if len(splited) == 1:
        list_of_results = indexer.find_word(word)
    else:
        list_of_results = indexer.find_word(splited[0])

    if len(list_of_results) == 0:
        return render(request, 'index.html', {'results': None})


    if len(splited) == 1:
        return render(request, 'index.html', {'results': list_of_results})

    results = []
    for res in list_of_results:
        if res[2].find(splited[1]) != -1:
            results.append(res)



    return render(request, 'index.html', {'results': results})


def index_url(request):
    url = request.POST.get('input_field')
    if url is not None:
        str_url = str(url)
        if str_url.find('http') != 0:
            url = "http://" + str(url)

        Crawler(url).crawl()

    return render(request, 'indexURL.html')


def knownURL(request):
    ids = []
    # docs = Pages.objects.all()
    # for doc in docs:
    #     ids.append(int(doc.id))
    #
    # if not request.method == "POST" or request.POST.get('id') == '':
    #     return render(request, 'knownURL.html', {'docs': docs})
    #
    # if int(request.POST.get('id')) in ids:
    #     id_ = request.POST.get('id')
    # Pages.objects.get(id=id_).delete()
    # docs = Pages.objects.all()

    return render(request, 'knownURL.html', {"docs": docs})


def indexWords(request):
    ids = []
    pags = Indexes.objects.all()
    for index in pags:
        ids.append(int(index.id))

    if not request.method == "POST" or request.POST.get('id') == '':
        return render(request, 'indexWords.html', {'pags': pags[:300]})

    if int(request.POST.get('id')) in ids:
        id_ = request.POST.get('id')
    Indexes.objects.get(id=id_).delete()
    pags = Indexes.objects.all()

    pags = Indexes.objects.all()
    return render(request, 'indexWords.html', {"pags": pags[:300]})
