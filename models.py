# -*- coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    areaid = models.IntegerField(db_column='AreaID',primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    areatype = models.IntegerField(db_column='AreaType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area'


class Bigcate(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    cateid = models.IntegerField(db_column='CateID')  # Field name made lowercase.
    catename = models.CharField(db_column='CateName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BigCate'


class Cabinet(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID', primary_key=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    cabinetname = models.CharField(db_column='CabinetName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cabinetnetaddress = models.CharField(db_column='CabinetNetAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cabinetrows = models.IntegerField(db_column='CabinetRows', blank=True, null=True)  # Field name made lowercase.
    cabinetcolumns = models.IntegerField(db_column='CabinetColumns', blank=True, null=True)  # Field name made lowercase.
    backkeytime1 = models.CharField(db_column='BackKeyTime1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    backkeytime2 = models.CharField(db_column='BackKeyTime2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    backkeytime3 = models.CharField(db_column='BackKeyTime3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    communicationstate = models.IntegerField(db_column='CommunicationState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cabinet'


class Cabinetmsg(models.Model):
    cabinetid = models.IntegerField(db_column='CabinetId', blank=True, null=True)  # Field name made lowercase.
    cabinetname = models.CharField(db_column='CabinetName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keystate = models.CharField(db_column='KeyState', max_length=500, blank=True, null=True)  # Field name made lowercase.
    broadstate = models.CharField(db_column='BroadState', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CabinetMsg'


class Cabinetoperate(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID')  # Field name made lowercase.
    operateuser = models.CharField(db_column='OperateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operatedate = models.DateTimeField(db_column='OperateDate')  # Field name made lowercase.
    operatetype = models.IntegerField(db_column='OperateType')  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CabinetOperate'


class Camera(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    cameraid = models.IntegerField(db_column='CameraID', primary_key=True)  # Field name made lowercase.
    cameraname = models.CharField(db_column='CameraName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cameralevel = models.SmallIntegerField(db_column='CameraLevel')  # Field name made lowercase.
    cameratype = models.SmallIntegerField(db_column='CameraType')  # Field name made lowercase.
    cameraharddisk = models.IntegerField(db_column='CameraHardDisk')  # Field name made lowercase.
    cameragallery = models.IntegerField(db_column='CameraGallery', blank=True, null=True)  # Field name made lowercase.
    todevguid = models.CharField(db_column='ToDevGUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todevname = models.CharField(db_column='ToDevName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stime1 = models.CharField(db_column='STime1', max_length=5)  # Field name made lowercase.
    etime1 = models.CharField(db_column='ETime1', max_length=5)  # Field name made lowercase.
    stime2 = models.CharField(db_column='STime2', max_length=5)  # Field name made lowercase.
    etime2 = models.CharField(db_column='ETime2', max_length=5)  # Field name made lowercase.
    stime3 = models.CharField(db_column='STime3', max_length=5)  # Field name made lowercase.
    etime3 = models.CharField(db_column='ETime3', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Camera'


class Cameraharddisk(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    harddiskid = models.IntegerField(db_column='HardDiskID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraHardDisk'


class Carddoor(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', primary_key=True, max_length=20)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardDoor'


class Carddoorrecord(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    ftime = models.DateTimeField(db_column='FTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardDoorRecord'


class Carddooruser(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rolelevel = models.CharField(db_column='RoleLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardDoorUser'


class Cardreader(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', primary_key=True)  # Field name made lowercase.
    cardreaderip = models.CharField(db_column='CardReaderIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID', blank=True, null=True)  # Field name made lowercase.
    cardreadertype = models.IntegerField(db_column='CardReaderType', blank=True, null=True)  # Field name made lowercase.
    communicationstate = models.IntegerField(db_column='CommunicationState', blank=True, null=True)  # Field name made lowercase.
    flag = models.BooleanField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardReader'


class Checkmaintain(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    fdate = models.DateField(db_column='FDate', blank=True, null=True)  # Field name made lowercase.
    ftime = models.CharField(db_column='FTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcontent = models.CharField(db_column='FContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fbug = models.CharField(db_column='FBug', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fhandle = models.CharField(db_column='FHandle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fduty = models.CharField(db_column='FDuty', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fremark = models.CharField(db_column='FRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckMaintain'


class Databak(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    fdate = models.DateField(db_column='FDate', blank=True, null=True)  # Field name made lowercase.
    ftime = models.CharField(db_column='FTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcontent = models.CharField(db_column='FContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fway = models.CharField(db_column='FWay', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fbakid = models.CharField(db_column='FBakID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fduty = models.CharField(db_column='FDuty', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fremark = models.CharField(db_column='FRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataBak'


class Daytahrecord(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    fdate = models.DateField(db_column='FDate', blank=True, null=True)  # Field name made lowercase.
    ckh1 = models.DecimalField(db_column='CKH1', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wdam1 = models.DecimalField(db_column='WdAM1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdam1 = models.DecimalField(db_column='SdAM1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wdpm1 = models.DecimalField(db_column='WdPM1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdpm1 = models.DecimalField(db_column='SdPM1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ckh2 = models.DecimalField(db_column='CKH2', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wdam2 = models.DecimalField(db_column='WdAM2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdam2 = models.DecimalField(db_column='SdAM2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wdpm2 = models.DecimalField(db_column='WdPM2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdpm2 = models.DecimalField(db_column='SdPM2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ckh3 = models.DecimalField(db_column='CKH3', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wdam3 = models.DecimalField(db_column='WdAM3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdam3 = models.DecimalField(db_column='SdAM3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wdpm3 = models.DecimalField(db_column='WdPM3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdpm3 = models.DecimalField(db_column='SdPM3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DayTAHRecord'


class Detailcate(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    cateid = models.IntegerField(db_column='CateID', primary_key=True)  # Field name made lowercase.
    detailid = models.IntegerField(db_column='DetailID')  # Field name made lowercase.
    detailname = models.CharField(db_column='DetailName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetailCate'
        unique_together = (('cateid', 'detailid'),)


class Devoperatemsg(models.Model):
    onlyid = models.AutoField(db_column='OnlyId', primary_key=True)  # Field name made lowercase.
    devtype = models.IntegerField(db_column='DevType')  # Field name made lowercase.
    devid = models.IntegerField(db_column='DevId')  # Field name made lowercase.
    operate = models.CharField(db_column='Operate', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DevOperateMsg'


class Door(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    doorid = models.IntegerField(db_column='DoorID', primary_key=True)  # Field name made lowercase.
    cardreadernumber = models.IntegerField(db_column='CardReaderNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Door'


class Doorkey(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    doorid = models.IntegerField(db_column='DoorID', blank=True, null=True)  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID', blank=True, null=True)  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoorKey'


class Doormsg(models.Model):
    doorid = models.IntegerField(db_column='DoorId', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    doorname = models.CharField(db_column='DoorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WareHouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    broadstate = models.CharField(db_column='BroadState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    watchstate = models.CharField(db_column='WatchState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoorMsg'


class Efence(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    extip = models.CharField(db_column='ExtIP', max_length=50)  # Field name made lowercase.
    extchannel = models.SmallIntegerField(db_column='ExtChannel')  # Field name made lowercase.
    ewidth = models.IntegerField(db_column='EWidth')  # Field name made lowercase.
    eheight = models.IntegerField(db_column='EHeight')  # Field name made lowercase.
    etype = models.SmallIntegerField(db_column='EType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EFence'


class Extension(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    extensionid = models.IntegerField(db_column='ExtensionID', primary_key=True)  # Field name made lowercase.
    extensionname = models.CharField(db_column='ExtensionName', max_length=100)  # Field name made lowercase.
    communicationip = models.CharField(db_column='CommunicationIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temperaturenumber = models.IntegerField(db_column='TemperatureNumber', blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    extensiontype = models.IntegerField(db_column='ExtensionType', blank=True, null=True)  # Field name made lowercase.
    inputsignal1 = models.IntegerField(db_column='InputSignal1', blank=True, null=True)  # Field name made lowercase.
    inputsignal2 = models.IntegerField(db_column='InputSignal2', blank=True, null=True)  # Field name made lowercase.
    inputsignal3 = models.IntegerField(db_column='InputSignal3', blank=True, null=True)  # Field name made lowercase.
    inputsignal4 = models.IntegerField(db_column='InputSignal4', blank=True, null=True)  # Field name made lowercase.
    inputsignal5 = models.IntegerField(db_column='InputSignal5', blank=True, null=True)  # Field name made lowercase.
    inputsignal6 = models.IntegerField(db_column='InputSignal6', blank=True, null=True)  # Field name made lowercase.
    inputsignal7 = models.IntegerField(db_column='InputSignal7', blank=True, null=True)  # Field name made lowercase.
    inputsignal8 = models.IntegerField(db_column='InputSignal8', blank=True, null=True)  # Field name made lowercase.
    inputsignalcount = models.IntegerField(db_column='InputSignalCount', blank=True, null=True)  # Field name made lowercase.
    outputsignalflag1 = models.IntegerField(db_column='OutputSignalFlag1', blank=True, null=True)  # Field name made lowercase.
    outputsignalflag2 = models.IntegerField(db_column='OutputSignalFlag2', blank=True, null=True)  # Field name made lowercase.
    outputsignalflag3 = models.IntegerField(db_column='OutputSignalFlag3', blank=True, null=True)  # Field name made lowercase.
    outputsignalflag4 = models.IntegerField(db_column='OutputSignalFlag4', blank=True, null=True)  # Field name made lowercase.
    outputsignal1 = models.IntegerField(db_column='OutputSignal1', blank=True, null=True)  # Field name made lowercase.
    outputsignal2 = models.IntegerField(db_column='OutputSignal2', blank=True, null=True)  # Field name made lowercase.
    outputsignal3 = models.IntegerField(db_column='OutputSignal3', blank=True, null=True)  # Field name made lowercase.
    outputsignal4 = models.IntegerField(db_column='OutputSignal4', blank=True, null=True)  # Field name made lowercase.
    communicationstate = models.IntegerField(db_column='CommunicationState', blank=True, null=True)  # Field name made lowercase.
    remarkflag = models.IntegerField(db_column='RemarkFlag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Extension'


class Extensionmsg(models.Model):
    extensionid = models.IntegerField(db_column='ExtensionId', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    extensionname = models.CharField(db_column='ExtensionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WareHouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    broadstate = models.CharField(db_column='BroadState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agvtemperature = models.CharField(db_column='AgvTemperature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agvhumidity = models.CharField(db_column='AgvHumidity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    abshumidity = models.CharField(db_column='AbsHumidity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtensionMsg'


class Facedoor(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inip = models.CharField(db_column='InIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inport = models.IntegerField(db_column='InPort', blank=True, null=True)  # Field name made lowercase.
    outip = models.CharField(db_column='OutIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    outport = models.IntegerField(db_column='OutPort', blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FaceDoor'


class Facedoormsg(models.Model):
    facedoorname = models.CharField(db_column='FaceDoorName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WareHouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    broadstate = models.CharField(db_column='BroadState', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FaceDoorMsg'


class Facedooruser(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FaceDoorUser'


class Incomewarehouserecord(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID', blank=True, null=True)  # Field name made lowercase.
    doorid = models.IntegerField(db_column='DoorID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyphyid = models.CharField(db_column='KeyPhyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indate = models.DateTimeField(db_column='InDate', blank=True, null=True)  # Field name made lowercase.
    outdate = models.DateTimeField(db_column='OutDate', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    fleader = models.CharField(db_column='FLeader', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fcount = models.CharField(db_column='FCount', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fworkcontent = models.CharField(db_column='FWorkContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fremark = models.CharField(db_column='FRemark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isrelated = models.BooleanField(db_column='IsRelated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InComeWareHouseRecord'


class Keepnightline(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', primary_key=True)  # Field name made lowercase.
    watercard = models.CharField(db_column='WaterCard', max_length=10)  # Field name made lowercase.
    watercardplayer = models.IntegerField(db_column='WaterCardPlayer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightLine'


class Keepnightlinedetail(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', primary_key=True)  # Field name made lowercase.
    keepnightsiteid = models.IntegerField(db_column='KeepNightSiteID')  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteID')  # Field name made lowercase.
    mintime = models.IntegerField(db_column='MinTime')  # Field name made lowercase.
    maxtime = models.IntegerField(db_column='MaxTime')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightLineDetail'
        unique_together = (('lineid', 'siteid'),)


class Keepnightlinemsg(models.Model):
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keepnightstate = models.CharField(db_column='KeepNightState', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightLineMsg'


class Keepnightlog(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    watercardid = models.CharField(db_column='WaterCardID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    watercardplayer = models.CharField(db_column='WaterCardPlayer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID', blank=True, null=True)  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    dothing = models.CharField(db_column='DoThing', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightLog'


class Keepnightschedule(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='CardNo', max_length=10)  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=50)  # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightSchedule'


class Keepnightsite(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    keepnightsitenumber = models.IntegerField(db_column='KeepNightSiteNumber', primary_key=True)  # Field name made lowercase.
    cardreadernumber = models.IntegerField(db_column='CardReaderNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightSite'


class Keepnightsitemsg(models.Model):
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteId', blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    keepnightstate = models.CharField(db_column='KeepNightState', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeepNightSiteMsg'


class Keyuserecord(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID', blank=True, null=True)  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyID', blank=True, null=True)  # Field name made lowercase.
    keyuser1 = models.CharField(db_column='KeyUser1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyuser2 = models.CharField(db_column='KeyUser2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cabinetuser = models.CharField(db_column='CabinetUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workcontent = models.CharField(db_column='WorkContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dutyuser = models.CharField(db_column='DutyUser', max_length=500, blank=True, null=True)  # Field name made lowercase.
    taketime = models.DateTimeField(db_column='TakeTime', blank=True, null=True)  # Field name made lowercase.
    baketime = models.DateTimeField(db_column='BakeTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyUseRecord'


class Keys(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyID', primary_key=True)  # Field name made lowercase.
    keyphynum = models.CharField(db_column='KeyPhyNum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    locksiteid = models.IntegerField(db_column='LockSiteID', blank=True, null=True)  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID')  # Field name made lowercase.
    keytype = models.IntegerField(db_column='KeyType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Keys'
        unique_together = (('keyid', 'cabinetid'),)


class Keysoperate(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID')  # Field name made lowercase.
    operateuser = models.CharField(db_column='OperateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operatekeys = models.CharField(db_column='OperateKeys', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operatedate = models.DateTimeField(db_column='OperateDate')  # Field name made lowercase.
    operatetype = models.IntegerField(db_column='OperateType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeysOperate'


class Logs(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=100)  # Field name made lowercase.
    logdate = models.DateTimeField(db_column='LogDate', blank=True, null=True)  # Field name made lowercase.
    logmemo = models.CharField(db_column='LogMemo', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logs'


class Onlineclient(models.Model):
    clientip = models.CharField(db_column='ClientIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnLineClient'


class Phumidity(models.Model):
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PHumidity'


class Pointsite(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=100)  # Field name made lowercase.
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointSite'


class Sysoperatelog(models.Model):
    onlyid = models.AutoField(db_column='OnlyID',primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dothing = models.CharField(db_column='Dothing', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ftime = models.DateTimeField(db_column='FTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SysOperateLog'


class Systemconfig(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    configname = models.CharField(db_column='ConfigName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    configvalue = models.CharField(db_column='ConfigValue', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SystemConfig'


class Userrole(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', unique=True, blank=True, null=True)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleID', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRole'


class Usertocabinet(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID', primary_key=True)  # Field name made lowercase.
    modelid = models.IntegerField(db_column='ModelID')  # Field name made lowercase.
    modelgroupid = models.CharField(db_column='ModelGroupID', max_length=50)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserToCabinet'
        unique_together = (('cabinetid', 'modelid', 'modelgroupid'),)


class Usertokeys(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID')  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserToKeys'
        unique_together = (('userid', 'cabinetid', 'keyid'),)


class Users(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=100)  # Field name made lowercase.
    realname = models.CharField(db_column='RealName', max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='UserPassword', max_length=200)  # Field name made lowercase.
    stopflag = models.IntegerField(db_column='StopFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Warehouse(models.Model):
    onlyid = models.AutoField(db_column='OnlyID')  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID', primary_key=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WareHouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WareHouse'


class Warehousemsg(models.Model):
    warehouseid = models.IntegerField(db_column='WareHouseId', blank=True, null=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WareHouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    watchstate = models.CharField(db_column='WatchState', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WareHouseMsg'


class Warehousetempandhum(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID', blank=True, null=True)  # Field name made lowercase.
    extensionid = models.IntegerField(db_column='ExtensionID', blank=True, null=True)  # Field name made lowercase.
    tempnum = models.FloatField(db_column='TempNum', blank=True, null=True)  # Field name made lowercase.
    humnum = models.FloatField(db_column='HumNum', blank=True, null=True)  # Field name made lowercase.
    abshumnum = models.FloatField(db_column='AbsHumNum', blank=True, null=True)  # Field name made lowercase.
    tandhdate = models.DateTimeField(db_column='TandHDate', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WareHouseTempAndHum'


class Warehousetempandhumdetail(models.Model):
    onlyid = models.AutoField(db_column='OnlyID', primary_key=True)  # Field name made lowercase.
    extensionid = models.IntegerField(db_column='ExtensionID', blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WareHouseID', blank=True, null=True)  # Field name made lowercase.
    temperature1 = models.FloatField(db_column='Temperature1', blank=True, null=True)  # Field name made lowercase.
    humidity1 = models.FloatField(db_column='Humidity1', blank=True, null=True)  # Field name made lowercase.
    temperature2 = models.FloatField(db_column='Temperature2', blank=True, null=True)  # Field name made lowercase.
    humidity2 = models.FloatField(db_column='Humidity2', blank=True, null=True)  # Field name made lowercase.
    temperature3 = models.FloatField(db_column='Temperature3', blank=True, null=True)  # Field name made lowercase.
    humidity3 = models.FloatField(db_column='Humidity3', blank=True, null=True)  # Field name made lowercase.
    temperature4 = models.FloatField(db_column='Temperature4', blank=True, null=True)  # Field name made lowercase.
    humidity4 = models.FloatField(db_column='Humidity4', blank=True, null=True)  # Field name made lowercase.
    temperature5 = models.FloatField(db_column='Temperature5', blank=True, null=True)  # Field name made lowercase.
    humidity5 = models.FloatField(db_column='Humidity5', blank=True, null=True)  # Field name made lowercase.
    temperature6 = models.FloatField(db_column='Temperature6', blank=True, null=True)  # Field name made lowercase.
    humidity6 = models.FloatField(db_column='Humidity6', blank=True, null=True)  # Field name made lowercase.
    temperature7 = models.FloatField(db_column='Temperature7', blank=True, null=True)  # Field name made lowercase.
    humidity7 = models.FloatField(db_column='Humidity7', blank=True, null=True)  # Field name made lowercase.
    temperature8 = models.FloatField(db_column='Temperature8', blank=True, null=True)  # Field name made lowercase.
    humidity8 = models.FloatField(db_column='Humidity8', blank=True, null=True)  # Field name made lowercase.
    ftime = models.DateTimeField(db_column='FTime', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WareHouseTempAndHumDetail'


class Workstatus(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    fdate = models.DateField(db_column='FDate', blank=True, null=True)  # Field name made lowercase.
    fduty = models.CharField(db_column='FDuty', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fduty2 = models.CharField(db_column='FDuty2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcadre = models.CharField(db_column='FCadre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fsystem = models.CharField(db_column='FSystem', max_length=200, blank=True, null=True)  # Field name made lowercase.
    frecord = models.CharField(db_column='FRecord', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fbusiness = models.CharField(db_column='FBusiness', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fvideo = models.CharField(db_column='FVideo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fspecial = models.CharField(db_column='FSpecial', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkStatus'
