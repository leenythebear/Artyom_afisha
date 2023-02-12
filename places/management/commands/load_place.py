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
        description_short = place_information['description_short']
        description_long = place_information['description_long']
        lng = place_information['coordinates']['lng']
        lat = place_information['coordinates']['lat']
        images = place_information['imgs']

        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'description_short': description_short,
                'description_long': description_long,
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
