# Generated by Django 3.0.8 on 2020-07-19 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('id',), 'verbose_name': 'Фаилы', 'verbose_name_plural': 'Фаилы'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('last_update',), 'verbose_name': 'Посты', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('name',), 'verbose_name': 'Темы', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterField(
            model_name='post',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name_post',
            field=models.CharField(blank=True, help_text='Назовите данный пост', max_length=2000, null=True, verbose_name='Название поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(help_text='Тема поста', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.Topic', verbose_name='Выберите тему к которой относится пост'),
        ),
    ]