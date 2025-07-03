from django.http import HttpResponse
from django.http import JsonResponse
def d_test (request):
    # return HttpResponse('<h1>this is a message main :</h1>')
    return JsonResponse({'mahdi':'10'})