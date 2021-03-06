# Generated by Django 2.0 on 2017-12-08 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.AutoField(db_column='CID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('description', models.TextField(db_column='Description')),
                ('icon', models.TextField(db_column='Icon')),
                ('date', models.DateTimeField(db_column='Date')),
                ('cost', models.IntegerField(db_column='Cost')),
                ('enrollNumber', models.IntegerField(blank=True, db_column='EnrollNumber', null=True)),
                ('avgRate', models.IntegerField(blank=True, db_column='AvgRate', null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coursematerial',
            fields=[
                ('cmid', models.AutoField(db_column='CMID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'coursematerial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('tid', models.AutoField(db_column='TID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('email', models.CharField(db_column='Email', max_length=100, unique=True)),
                ('firstName', models.CharField(db_column='FirstName', max_length=50)),
                ('lastName', models.CharField(db_column='LastName', max_length=50)),
                ('pw', models.CharField(db_column='PW', max_length=300)),
                ('profilePict', models.CharField(db_column='ProfilePict', max_length=50)),
                ('country', models.CharField(db_column='Country', max_length=50)),
                ('city', models.CharField(db_column='City', max_length=50)),
                ('street', models.CharField(db_column='Street', max_length=200)),
                ('postalCode', models.CharField(db_column='PostalCode', max_length=20)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('userID', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='trainly.User')),
                ('grantTime', models.DateTimeField(db_column='GrantTime')),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuyCourse',
            fields=[
                ('userID', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='trainly.User')),
                ('buyTime', models.DateTimeField(db_column='BuyTime')),
                ('code', models.CharField(db_column='Code', max_length=100)),
                ('isComplete', models.IntegerField(db_column='IsComplete')),
                ('completeTime', models.DateTimeField(db_column='CompleteTime')),
                ('rating', models.IntegerField(db_column='Rating')),
                ('comment', models.TextField(db_column='Comment')),
            ],
            options={
                'db_table': 'buycourse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompleteMaterial',
            fields=[
                ('cmid', models.ForeignKey(db_column='CMID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='trainly.Coursematerial')),
                ('completeTime', models.DateTimeField(db_column='CompleteTime')),
            ],
            options={
                'db_table': 'completematerial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('userID', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='trainly.User')),
                ('website', models.CharField(db_column='Website', max_length=200)),
                ('affiliation', models.CharField(db_column='Affiliation', max_length=50)),
                ('title', models.CharField(db_column='Title', max_length=300)),
                ('grantTime', models.DateTimeField(db_column='GrantTime')),
            ],
            options={
                'db_table': 'faculty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('userID', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='trainly.User')),
            ],
            options={
                'db_table': 'interested',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Secondarytopic',
            fields=[
                ('cid', models.ForeignKey(db_column='CID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='trainly.Course')),
            ],
            options={
                'db_table': 'secondarytopic',
                'managed': False,
            },
        ),
    ]
