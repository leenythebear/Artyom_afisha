from django.http import HttpResponse
from django.template import loader


def get_main(request):
    template = loader.get_template('main.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
