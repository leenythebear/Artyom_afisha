from django.http import HttpResponse
from django.templatetags.static import static
from django.template import loader
from .models import Place


def get_main(request):
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
            "detailsUrl": static('places/moscow_legends.json')
            }
        }
        features.append(feature)

    places = {
        'type': 'FeatureCollection',
        'features': features
    }
    print(places)
    template = loader.get_template('index.html')
    context = {'places': places}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
