# Generated by Django 2.2 on 2019-06-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='selections',
            field=models.ManyToManyField(db_table='movies_selection', related_name='movies', to='webapp.Selection'),
        ),
    ]
