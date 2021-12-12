from django.http import HttpResponse
import random


def status_view(request):
    return HttpResponse("ok")


def random_color(request):
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    html = f'<html><body bgcolor={color}>Random color: {color}</body></html>'
    return HttpResponse(html)

# also can use this
# def random_color(request):
#     rand = lambda: random.randint(0, 255)
#     color = '#%02X%02X%02X' % (rand(), rand(), rand())
#     html = f"<html><body bgcolor={color}>Color: {color}</body></html>"
#     return HttpResponse(html)
