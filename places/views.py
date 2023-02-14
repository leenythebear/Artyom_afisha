from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=place_id)
    serialized_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(serialized_place, json_dumps_params={"ensure_ascii": False, "indent": 2})


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
                 "detailsUrl": reverse("get_place", args=[place.id])
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
