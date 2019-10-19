from django.db import models


class Card(models.Model):
    card_image = models.CharField(max_length=200)
    card_heading = models.CharField(max_length=30)
    card_subtitle = models.CharField(max_length=40)
    card_paragraph = models.TextField()
    
    def __str__(self):
        return self.card_heading
