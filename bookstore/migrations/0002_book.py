# Generated by Django 4.1.3 on 2023-02-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('romance', 'Romance'), ('scifi', 'Sci-Fi')], default='education', max_length=30)),
            ],
        ),
    ]
