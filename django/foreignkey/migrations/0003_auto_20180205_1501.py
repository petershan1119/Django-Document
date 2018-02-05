# Generated by Django 2.0.2 on 2018-02-05 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkey', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('dex_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foreignkey.Type'),
        ),
    ]
