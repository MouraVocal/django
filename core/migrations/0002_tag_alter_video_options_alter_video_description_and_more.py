# Generated by Django 5.1.2 on 2024-10-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Vídeo', 'verbose_name_plural': 'Vídeos'},
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Está publicado?'),
        ),
        migrations.AlterField(
            model_name='video',
            name='num_likes',
            field=models.IntegerField(default=0, verbose_name='Número de likes'),
        ),
        migrations.AlterField(
            model_name='video',
            name='num_views',
            field=models.IntegerField(default=0, verbose_name='Número de views'),
        ),
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(verbose_name='Publicado em'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails/', verbose_name='miniatura'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='media/videos', verbose_name='vídeo'),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='core.tag'),
        ),
    ]