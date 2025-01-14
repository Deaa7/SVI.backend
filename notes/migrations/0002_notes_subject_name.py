# Generated by Django 5.1.1 on 2024-10-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='subject_name',
            field=models.CharField(blank=True, choices=[('math_12', ' رياضيات بكلوريا'), ('science_12', ' علوم بكلوريا'), ('english_12', 'انكليزي بكلوريا'), ('arabic_12', 'عربي بكلوريا'), ('physics_12', 'فيزياء بكلوريا'), ('chemistry_12', 'كيمياء بكلوريا'), ('national_12', ' وطنية بكلوريا'), ('france_12', 'فرنسي بكلوريا'), ('math_9', 'رياضيات تاسع'), ('science_9', 'علوم تاسع'), ('english_9', 'انكليزي تاسع'), ('arabic_9', 'عربي تاسع'), ('physics_chemistry_9', 'فيزياء و كيمياء تاسع'), ('geography_9', 'اجتماعيات تاسع'), ('france_9', 'فرنسي تاسع')], default='math_12', max_length=25),
        ),
    ]
