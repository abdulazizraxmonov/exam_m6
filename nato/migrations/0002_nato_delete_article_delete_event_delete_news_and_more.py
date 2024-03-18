# Generated by Django 5.0.3 on 2024-03-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NATO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('founding_date', models.DateField()),
                ('headquarters', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='country',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='country',
            name='year_joined',
        ),
        migrations.AddField(
            model_name='country',
            name='joined_date',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='nato',
            name='members',
            field=models.ManyToManyField(related_name='nato_membership', to='nato.country'),
        ),
    ]
