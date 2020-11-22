# Generated by Django 3.1.3 on 2020-11-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('contact', models.CharField(choices=[('t', 'Telegram'), ('i', 'Instagram'), ('w', 'WhatsUp'), ('m', 'Mail')], default='t', max_length=1, verbose_name='Telegram/WhatsApp/Istagram/Mail')),
                ('contact_name', models.CharField(max_length=250, verbose_name='nickname')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'ordering': ['-created'],
            },
        ),
    ]