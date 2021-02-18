from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'name': 'My Dog.',
        'user': 'Yésica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
    
]

def list_posts(request):
    """ List existing post """
    
    content = []
    for post in posts:
        content.append("""
        <p><strong> {name} </p></strong>
        <p><small> {user} </p></small>
        <figure> <img src={picture} /> </figure>

        """.format(**post)
        )
    
    return HttpResponse('<br>'.join(content)) 