# Generated by Django 2.2 on 2019-08-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sen_num', models.IntegerField()),
                ('is_yuqing', models.IntegerField()),
                ('source', models.CharField(max_length=200)),
                ('introduce', models.TextField()),
                ('word', models.CharField(max_length=50)),
            ],
        ),
    ]
