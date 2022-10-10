# Generated by Django 4.1.1 on 2022-10-05 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('order_menu', models.SmallIntegerField(default=0)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('kind', models.SmallIntegerField(choices=[(1, 'Frontend'), (2, 'Backend')], default=1)),
                ('is_visibled', models.BooleanField(default=True)),
                ('is_external', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('menu_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.menugroup')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_group',
            field=models.ManyToManyField(blank=True, null=True, to='menu.menugroup'),
        ),
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
    ]
