# Generated by Django 3.0.8 on 2020-07-20 14:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('critical', 'critical.'), ('debug', 'debug'), ('error', 'error'), ('warning', 'warning'), ('information', 'info')], max_length=20)),
                ('environment', models.CharField(choices=[('produção', 'produção'), ('homologação', 'homologação'), ('dev', 'dev')], max_length=20)),
                ('log', models.TextField(max_length=500)),
                ('address', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv4_address])),
                ('date', models.DateField(auto_now_add=True)),
                ('archive', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
