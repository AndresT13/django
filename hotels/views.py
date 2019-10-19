from django.shortcuts import render


hotels = [
    {
        'city': 'Bogota',
        'user': {
            'administrator': 'Jaime Torres',

        },
        'picture': 'http://s1.picswalls.com/wallpapers/2016/03/29/beautiful-nature-background_042320579_304.jpg'
    },
     {
        'city': 'Medellín',
        'user': {
            'administrator': 'Hernesto Melchor',

        },
        'picture': 'https://i.imgur.com/Zir9zCj.jpg'
    },
     {
        'city': 'Manizalez',
        'user': {
            'administrator': 'Jhon Doe',

        },
        'picture': 'https://images6.alphacoders.com/476/476288.jpg'
    }
]



def list_hotels(request):
    return render(request, 'feed.html', {'data': hotels})


# Create your views here.
