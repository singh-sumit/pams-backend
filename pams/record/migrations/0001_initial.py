# Generated by Django 4.0.6 on 2022-07-27 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_delete_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
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
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choosed_date', models.DateField(auto_now_add=True)),
                ('scheduled_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('SCHEDULED', 'Scheduled'), ('DONE', 'Done'), ('NOVISIT', 'NoVisit')], default='CREATED', max_length=20)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
                ('scheduled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.receptionist')),
            ],
            options={
                'db_table': 'appointments',
            },
        ),
    ]
