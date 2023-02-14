from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loading_places'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', type=str)

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_information = response.json()
        title = place_information['title']
        short_description = place_information['short_description']
        long_description = place_information['long_description']
        lng = place_information['coordinates']['lng']
        lat = place_information['coordinates']['lat']
        images = place_information['imgs']

        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'short_description': short_description,
                'long_description': long_description,
                'latitude': lat,
                'longitude': lng,
            }
        )
        if created:
            self.download_images(images, place)

    def download_images(self, images, place):
        for number, image in enumerate(images):
            image_response = requests.get(image)
            image_response.raise_for_status()
            content_file = ContentFile(
                image_response.content,
                name=f'{place}{number}.jpg'
            )
            Image.objects.create(
                place=place,
                image=content_file,
                number=number
            )
