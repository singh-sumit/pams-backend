# Generated by Django 4.0.6 on 2022-07-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import pams.config.core.fields.model_fields
import pams.config.core.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', pams.config.core.fields.model_fields.LowercaseEmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50, validators=[pams.config.core.validators.validate_alphabet])),
                ('last_name', models.CharField(max_length=50, validators=[pams.config.core.validators.validate_alphabet])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_receptionist', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(choices=[('GENERAL', 'General'), ('CARDIOLOGY', 'Cardiology'), ('NEUROLOGY', 'Neurology'), ('HEMATOLOGY', 'Hematology'), ('SURGERY', 'Surgery'), ('ORTHOPEDICS', 'Orthopedics'), ('PEDIATRICS', 'Pediatrics')], default='GENERAL', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('doctor', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, validators=[pams.config.core.validators.validate_alphabet])),
                ('last_name', models.CharField(max_length=50, validators=[pams.config.core.validators.validate_alphabet])),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
            options={
                'db_table': 'records',
            },
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('receptionist', django.db.models.manager.Manager()),
            ],
        ),
    ]
