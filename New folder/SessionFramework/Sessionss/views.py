from django.shortcuts import render
from django.http import HttpResponse
# from datetime import datetime, timedelta
# from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def setsession(request):
   # all the set data will be added in same session
   request.session['name'] = 'Abhay'
   request.session['lname'] = 'Kanwasi'
   request.session.set_expiry(10) # session expires in 600 seconds
   #request.session.set_expiry(0) # session expires when browser close
   return render(request, 'setsession.html')

def getsession(request):
    if 'name' in request.session:
        # name = request.session['name'] # give the key to know the value
        name = request.session.get('name') # can give default
        lname = request.session.get('lname')
        request.session.modified = True # add the time that we give for session timeout (it means if our session timeout time is 10sec and in that 10sec our session get some changes(even refresh ) it will give 10 more seconds for session timeout)
    else:
        return HttpResponse("Your session has expired !")
    # methods
    # keys = request.session.keys()
    # values = request.session.values()
    # items = request.session.items()
    # age = request.session.setdefault('age', '23')
    # session_cookie_age = request.session.get_session_cookie_age()
    # expiry_age = request.session.get_expiry_age()
    # expiry_date = request.session.get_expiry_date()
    # check_on_browser_close = request.session.get_expire_at_browser_close()

    return render(request, 'getsession.html', {'name':name, 'lname':lname})

def delsession(request):
    # # for deleting a data in session
    # if 'name' in request.session:
    #     del request.session['name']
    #     del request.session['lname']

    # for deleting the session
    request.session.flush()

    # if we now try to get data it will not give us error because we defined many default values and because of that when we try to set value they create a session and doesn't give us error.

    # flush help us to clear data from browser but still expires data save in db for that we use clear
    request.session.clear_expired()
    return render(request, 'delsession.html')


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'settestcookie.html')

def checktestcookie(request):
    test = request.session.test_cookie_worked()
    return render(request, 'checktestcookie.html', {'test':test})

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'deltestcookie.html')