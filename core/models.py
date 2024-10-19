from django.db import models
from django.utils import timezone

# Create your models here.


class Video(models.Model):
    title = models.CharField(
        max_length=100, unique=True, verbose_name="Título")
    description = models.TextField(verbose_name="descrição")
    thumbnail = models.ImageField(
        upload_to='thumbnails/', verbose_name="miniatura")
    video = models.FileField(upload_to='media/videos', verbose_name="vídeo")
    slug = models.SlugField(max_length=100, unique=True)
    published_at = models.DateTimeField(
        verbose_name="Publicado em", null=True, editable=False)
    is_published = models.BooleanField(
        default=False, verbose_name="Está publicado?")
    num_likes = models.IntegerField(
        default=0, verbose_name="Número de likes", editable=False)
    num_views = models.IntegerField(
        default=0, verbose_name="Número de views", editable=False)
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey(
        'auth.User', on_delete=models.PROTECT, verbose_name='autor', editable=False)

    class Meta:
        verbose_name = "Vídeo"
        verbose_name_plural = "Vídeos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")

    def __str__(self):
        return self.name
