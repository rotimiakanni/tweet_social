from django.shortcuts import render, redirect
from .models import Tweet
from django.http import HttpResponse, Http404, JsonResponse
from .forms import TweetForm
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def home_view(request):
    current_site = get_current_site(request)
    print(current_site)
    return render(request, 'pages/home.html')

def tweet_list_view(request):
    qs = Tweet.objects.all()
    tweet_list = [{'id':x.id, 'content':x.content, 'counts':20} for x in qs]
    data = {
        'isUser':False,
        'response':tweet_list
    }
    return JsonResponse(data, status=200)

def create_tweet_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
    return render(request, 'components/form.html', context={"form": form})

def tweet_view(request, tweet_id, args, kwargs):
    data = {
        id:tweet_id
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        status = 200
    except:
        data['message'] = 'Content not found'
        status = 404
    data = {
        id:tweet.id,
        content:obj.content
    }
    return JsonResponse(data, status=status)