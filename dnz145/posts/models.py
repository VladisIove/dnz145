import uuid
import os

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"dnz145-{uuid.uuid4()}.{ext}"
    return f'upload_file/{filename}'
    
class Topic(models.Model):
    class Meta:
        db_table = 'topics' 
        ordering = ('name',)
        verbose_name = 'назви тем'
        verbose_name_plural = 'назви тем'

    name = models.CharField(max_length=2000, help_text='Назва теми', verbose_name='Назва теми') 
    active = models.BooleanField(default=True, help_text='Чи активна ця тема на сайті', verbose_name='Активація')
    slug = models.SlugField(null=False, blank=False, unique=True, help_text='Чипати у виподку інформування', verbose_name='Слаг')

    def __str__(self,):
        return self.name


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        ordering = ('last_update',)
        verbose_name = 'Пости'
        verbose_name_plural = 'Пости'

    topic = models.ForeignKey(Topic, null=False, blank=False, related_name='posts', on_delete=models.CASCADE,
                                help_text='Тема посту', verbose_name='Оберіть тему посту к якій відносится пост')
    name = models.CharField(max_length=2000, null=True, blank=True, unique=False, 
                                    help_text='Впішить назву даного посту', verbose_name='Назва поста')
    text = RichTextUploadingField(verbose_name='Текс для посту', 
                        help_text='Відкерактуйте текст, так Ви бажаєте щоб він виглядав на сайті')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Част останнього редагування')
    slug = models.SlugField(null=False, blank=False, unique=True, help_text='Чипати у виподку інформування', verbose_name='Слаг')
    active = models.BooleanField(default=True,help_text='Чи активна цей пост на сайті', verbose_name='Активація')

    def __str__(self,):
        return self.name

class File(models.Model):
    class Meta:
        db_table = 'files'
        ordering = ('id',)
        verbose_name = 'Файли'
        verbose_name_plural = 'Файли'
    
    name = models.CharField(max_length=2000, null=True, blank=True, default='Файл',
                            help_text='Назва файла не обов\'язкова', verbose_name='Назва файла')
    file_link = models.FileField(upload_to=get_file_path, help_text='Оберіть потрібний файл для поста', verbose_name='Загрузити файл')
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE, related_name='files', 
                                help_text='До якого посту приєднати файл', verbose_name='Пост')
    active = models.BooleanField(default=True, help_text='Чи активна цей файл на сайті', verbose_name='Активація')

    def __str__(self):
        return self.name if self.name is not None else 'Фаил'


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file_link:
        if os.path.isfile(instance.file_link.path):
            os.remove(instance.file_link.path)

@receiver(models.signals.pre_save, sender=File)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = File.objects.get(pk=instance.pk).file_link
    except File.DoesNotExist:
        return False

    new_file = instance.file_link
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
