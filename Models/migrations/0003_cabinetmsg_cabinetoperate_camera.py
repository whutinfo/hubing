# Generated by Django 2.1.5 on 2019-04-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_cabinet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinetmsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinetid', models.IntegerField(blank=True, db_column='CabinetId', null=True)),
                ('cabinetname', models.CharField(blank=True, db_column='CabinetName', max_length=50, null=True)),
                ('keystate', models.CharField(blank=True, db_column='KeyState', max_length=500, null=True)),
                ('broadstate', models.CharField(blank=True, db_column='BroadState', max_length=50, null=True)),
            ],
            options={
                'db_table': 'CabinetMsg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cabinetoperate',
            fields=[
                ('onlyid', models.AutoField(db_column='OnlyID', primary_key=True, serialize=False)),
                ('cabinetid', models.IntegerField(db_column='CabinetID')),
                ('operateuser', models.CharField(blank=True, db_column='OperateUser', max_length=50, null=True)),
                ('operatedate', models.DateTimeField(db_column='OperateDate')),
                ('operatetype', models.IntegerField(db_column='OperateType')),
                ('flag', models.IntegerField(blank=True, db_column='Flag', null=True)),
            ],
            options={
                'db_table': 'CabinetOperate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('onlyid', models.IntegerField(auto_created=True, db_column='OnlyID')),
                ('guid', models.CharField(db_column='GUID', max_length=100)),
                ('cameraid', models.IntegerField(db_column='CameraID', primary_key=True, serialize=False)),
                ('cameraname', models.CharField(blank=True, db_column='CameraName', max_length=50, null=True)),
                ('cameralevel', models.SmallIntegerField(db_column='CameraLevel')),
                ('cameratype', models.SmallIntegerField(db_column='CameraType')),
                ('cameraharddisk', models.IntegerField(db_column='CameraHardDisk')),
                ('cameragallery', models.IntegerField(blank=True, db_column='CameraGallery', null=True)),
                ('todevguid', models.CharField(blank=True, db_column='ToDevGUID', max_length=100, null=True)),
                ('todevname', models.CharField(blank=True, db_column='ToDevName', max_length=50, null=True)),
                ('stime1', models.CharField(db_column='STime1', max_length=5)),
                ('etime1', models.CharField(db_column='ETime1', max_length=5)),
                ('stime2', models.CharField(db_column='STime2', max_length=5)),
                ('etime2', models.CharField(db_column='ETime2', max_length=5)),
                ('stime3', models.CharField(db_column='STime3', max_length=5)),
                ('etime3', models.CharField(db_column='ETime3', max_length=5)),
            ],
            options={
                'db_table': 'Camera',
                'managed': False,
            },
        ),
    ]