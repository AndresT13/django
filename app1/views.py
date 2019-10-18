from django.http import HttpResponse
import json


def testUno(request):
    return HttpResponse('Pagina 2')

def test3(request):
    numbers = [ int(i) for i in request.GET ['numbers'].split(',')]
    sorted_ints = sorted(numbers)


    data = {
        'status': 'OK',
        'numbers': sorted_ints,
        'message': 'Request successfully'
    }

    return HttpResponse (
        json.dumps(data, indent=4),
        content_type = 'application/json'
    )