from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            # Increase word count
            worddic[word] += 1
        else:
            # Add to dictionary
            worddic[word] = 1
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddic':worddic.items()})
