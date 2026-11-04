from django.db import models


class WeddingProfile(models.Model):

    bride_name = models.CharField(max_length=100)
    groom_name = models.CharField(max_length=100)

    bride_father = models.CharField(max_length=100)
    bride_mother = models.CharField(max_length=100)

    bride_address = models.TextField()

    groom_father = models.CharField(max_length=100)
    groom_mother = models.CharField(max_length=100)

    groom_address = models.TextField()

    wedding_date = models.DateField()
    wedding_time = models.TimeField()

    venue_name = models.CharField(max_length=200)
    venue_address = models.TextField()

    google_maps_url = models.URLField(blank=True)

    invitation_message = models.TextField(
        default="Together with our families, we cordially invite you to celebrate our wedding."
    )

    story_intro = models.TextField(blank=True)

    def __str__(self):
        return self.bride_name + " & " + self.groom_name


class GalleryImage(models.Model):

    image = models.ImageField(upload_to='gallery/')

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.caption or "Wedding Gallery Image"

    class Meta:
        ordering = ['order']