# Generated by Django 4.0 on 2022-01-03 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tours.district'),
            preserve_default=False,
        ),
    ]
