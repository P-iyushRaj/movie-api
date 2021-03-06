# Generated by Django 3.1.7 on 2021-04-17 13:43

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_address_model',
            fields=[
                ('address_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address_street', models.CharField(blank=True, max_length=200, null=True)),
                ('address_street2', models.CharField(blank=True, max_length=200, null=True)),
                ('address_city', models.CharField(blank=True, max_length=200, null=True)),
                ('address_state', models.CharField(blank=True, max_length=200, null=True)),
                ('address_zip', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_model',
            fields=[
                ('patient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('lst_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('suffix_form', models.CharField(blank=True, max_length=200, null=True)),
                ('prefix_form', models.CharField(blank=True, max_length=200, null=True)),
                ('Home_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('work_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('Social_security_num', models.IntegerField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('emergency_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emergency_relation', models.CharField(blank=True, max_length=200, null=True)),
                ('sex', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_date', models.DateTimeField(blank=True, null=True)),
                ('employee_signature', models.FileField(blank=True, null=True, upload_to='upload/')),
                ('alter_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('alter_name', models.CharField(blank=True, max_length=200, null=True)),
                ('alter_relation', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='primerx_field_model',
        ),
        migrations.RenameField(
            model_name='form_field_model',
            old_name='Social_security_num',
            new_name='form_id',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='Home_number',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='address_city',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='address_state',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='address_street',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='address_zip',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='date_of_date',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='education',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='emergency_name',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='emergency_phone',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='emergency_relation',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='employee_signature',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='lst_name',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='prefix_form',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='suffix_form',
        ),
        migrations.RemoveField(
            model_name='form_field_model',
            name='work_number',
        ),
        migrations.AddField(
            model_name='form_field_model',
            name='Patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.patient_model'),
        ),
        migrations.AddField(
            model_name='form_field_model',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.patient_address_model'),
        ),
    ]
