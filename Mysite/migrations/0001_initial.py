# Generated by Django 3.0.3 on 2020-02-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField(default=0)),
                ('empcode', models.TextField(max_length=50)),
                ('empname', models.TextField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=50)),
                ('dept', models.CharField(choices=[('python', 'python'), ('php', 'php'), ('ruby', 'ruby')], default='python', max_length=30)),
                ('hobbis', models.CharField(choices=[('reading', 'reading'), ('writing', 'writing'), ('playing', 'playing')], default='reading', max_length=50)),
                ('photo', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
    ]