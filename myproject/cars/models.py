from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()  # Suponiendo que la imagen es una URL
    average_rating = models.FloatField()
    summary = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return {self.car.name}
