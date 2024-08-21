

from django.core.management.base import BaseCommand
import pandas as pd
from cars.utils.reviews import summarize_reviews
from cars.utils.dowload import download_image

class Command(BaseCommand):
    help = 'Update vehicle data from reviews'

    def handle(self, *args, **kwargs):
        vehicles = [
            ('chevrolet', 'sail'),
            ('Volkswagen', 'Gol'),
            ('Toyota', 'Hilux')
        ]

        summary_df, all_reviews_df = summarize_reviews(vehicles)

        from cars.models import Car, Comment


        # Limpiar datos anteriores si es necesario
        Car.objects.all().delete()
        Comment.objects.all().delete()

        # Actualizar datos de coches
        for _, row in summary_df.iterrows():
            # Descargar imagen
            image_url = download_image(row['name'])
            
            # Crear o actualizar el objeto Car
            Car.objects.create(
                name=row['name'],
                average_rating=row['average_rating'],
                summary=row['summary'],
                image=image_url  # Agregar URL de imagen
            )

        # Actualizar comentarios
        for _, row in all_reviews_df.iterrows():
            Comment.objects.create(
                car=Car.objects.get(name=row['name']),
                text=row['comment'],
                rating=row['rating']
            )
        
        self.stdout.write(self.style.SUCCESS('Vehicle data updated successfully.'))
