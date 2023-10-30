from django.shortcuts import render, redirect

# Create your views here.

def chat_page(request, *args, **kwargs):
    try:
        if not request.user.is_authenticated:
            return redirect('login-user')
        return render(request, 'chatpage.html',context={})
    except Exception as e:
        raise e