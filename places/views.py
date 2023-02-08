from django.http import HttpResponse
from django.templatetags.static import static
from django.template import loader
from .models import Place


def get_index_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": static(place.details_url)
            }
        }
        features.append(feature)

    places = {
        'type': 'FeatureCollection',
        'features': features
    }
    template = loader.get_template('index.html')
    context = {'places': places}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
