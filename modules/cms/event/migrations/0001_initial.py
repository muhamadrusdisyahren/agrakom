# Generated by Django 2.0.4 on 2018-05-09 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='static/images/detail_galery')),
                ('caption', models.CharField(blank=True, max_length=225, null=True)),
                ('status', models.BooleanField()),
                ('position', models.IntegerField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='detailevent_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'detail_event',
            },
        ),
        migrations.CreateModel(
            name='EventGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='static/images/galery')),
                ('status', models.BooleanField()),
                ('position', models.IntegerField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, db_column='created_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='eventgalery_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_column='modified_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='eventgalery_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event_galery',
            },
        ),
        migrations.AddField(
            model_name='detailevent',
            name='event_galery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.EventGalery'),
        ),
        migrations.AddField(
            model_name='detailevent',
            name='modified_by',
            field=models.ForeignKey(blank=True, db_column='modified_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='detailevent_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]