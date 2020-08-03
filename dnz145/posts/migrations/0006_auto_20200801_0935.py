# Generated by Django 3.0.8 on 2020-08-01 06:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200727_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('id',), 'verbose_name': 'Файли', 'verbose_name_plural': 'Файли'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('last_update',), 'verbose_name': 'Пости', 'verbose_name_plural': 'Пости'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('name',), 'verbose_name': 'назви тем', 'verbose_name_plural': 'назви тем'},
        ),
        migrations.AlterField(
            model_name='file',
            name='active',
            field=models.BooleanField(default=True, help_text='Чи активна цей файл на сайті', verbose_name='Активація'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_link',
            field=models.FileField(help_text='Оберіть потрібний файл для поста', upload_to=posts.models.get_file_path, verbose_name='Загрузити файл'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, default='Файл', help_text="Назва файла не обов'язкова", max_length=2000, null=True, verbose_name='Назва файла'),
        ),
        migrations.AlterField(
            model_name='file',
            name='post',
            field=models.ForeignKey(help_text='До якого посту приєднати файл', on_delete=django.db.models.deletion.CASCADE, related_name='files', to='posts.Post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True, help_text='Чи активна цей пост на сайті', verbose_name='Активація'),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Част останнього редагування'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, help_text='Впішить назву даного посту', max_length=2000, null=True, verbose_name='Назва поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Чипати у виподку інформування', unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='Відкерактуйте текст, так Ви бажаєте щоб він виглядав на сайті', verbose_name='Текс для посту'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(help_text='Тема посту', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.Topic', verbose_name='Оберіть тему посту к якій відносится пост'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='active',
            field=models.BooleanField(default=True, help_text='Чи активна ця тема на сайті', verbose_name='Активація'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(help_text='Назва теми', max_length=2000, verbose_name='Назва теми'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(help_text='Чипати у виподку інформування', unique=True, verbose_name='Слаг'),
        ),
    ]