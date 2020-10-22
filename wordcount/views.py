from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    txtdoc=request.GET['counttext']
    words=txtdoc.split()
    worddic={}
    for word in words:
        if word in worddic:
            worddic[wordd]+=1
        else:
            worddic[word]=1


    return render(request,'count.html',{"txtdoc":txtdoc,"noofwords":len(words),"Worddic":worddic})
def aboutus(request):
    return render (request,'aboutus.html')
