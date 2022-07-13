from django.shortcuts import render
import random


users = {}

# Create your views here.
def index(request):

    user_id = request.COOKIES.get('user_id')

    if user_id not in users:
        user_id = str(random.randrange(1000, 600000))
        users[user_id] = {
            'count': 1
        }
    else:
        users[user_id]['count'] += 1

    my_data = {
        'user_id': user_id,
        'view_count': users[user_id]['count']
    }

    response = render(request, 'index.html', my_data)
    response.set_cookie('user_id', user_id)

    return response
