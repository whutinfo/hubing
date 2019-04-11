from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json
from Module_test.com_func import *


def test(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''

	'''sys code define variable end  '''

	if request.method == 'GET':
		'''user code define variable begin  '''
		''' !!  都只改值，不动变量名    !!'''
		html_name = 'Module_test/test.html'  # 配置html的所在地址
		head_title = ''  # 网页的标题title

		'''!!    表格初始化  版本1  单表查字段注释   !! '''
		datagrid_version = 2  # 哪一代版本的 int
		datagrid_title = '分级表'  # 表格的名称

		datagrid_columncnt = 28  # 需要获取的列的数量 包括id
		datagrid_columnwidth = [0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10
								,10,10,10,10,10,10,10,10]  # 列的宽度 个数与cnt匹配
		datagrid_columnalign = ['center'] * datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！
		# '''   获取字段的注释的参数  直接写简单点  '''
		column_comment = ('ID', 'GUID', 'ExtensionID', 'ExtensionName', 'CommunicationIP', 'TemperatureNumber',
		                  'WareHouseID','CreateDate', 'ExtensionType', 'InputSignal1', 'InputSignal2', 'InputSignal3',
		                  'InputSignal4','InputSignal5','InputSignal6','InputSignal7','InputSignal8','InputSignalCount',
		                  'OutputSignalFlag1','OutputSignalFlag2','OutputSignalFlag3','OutputSignalFlag4','OutputSignal1',
		                  'OutputSignal2','OutputSignal3','OutputSignal14','CommunicationState','RemarkFlag')


		'''sys code begin  '''

		'''        表格初始化      '''
		base_html_construct = base_html_construct_trans(datagrid_version, datagrid_columnwidth, datagrid_columnalign)
		base_html_construct.encode()  # 先将传送进来的参数进行解析
		column = base_html_construct.fun_Get_Muti_Table(datagrid_columncnt, column_comment)  # 拼接cnt列Json

		return_dict = {'head_title': head_title, 'info_dict': column, 'datagrid_title': datagrid_title }

		return render(request, html_name, return_dict)  # 将初始化信息全部返回到前端
		'''sys code end'''

	else:
		'''user code define variable begin  '''
		model_name = models.Extension  # 想要展示的表的Model对象
		'''user code define variable end  '''

		'''usr code begin  '''

		if action == 'LoadData':
			querys = model_name.objects.all()  # 获取需要的字段名的数据
			value_dict = {'value0':'','value1': '', 'value2': '','value3':'','value4':'','value5':''
				, 'value6': ''	, 'value7': '', 'value8': '', 'value9': ''	, 'value10': '', 'value11': ''
				, 'value12': '', 'value13': '', 'value14': '', 'value15': '', 'value16': '', 'value17': ''
				, 'value18': '', 'value19': '', 'value20': '', 'value21': '', 'value22': '', 'value23': ''
				, 'value24': '', 'value25': '', 'value26': '', 'value27': '', 'value28': ''
				 }   #有几个需要的列就有多少value 包括Id
			value_list = []
			for row in querys:
				value_dict['value0'] = row.onlyid  # 一定要获取id 并放进第一个value0
				value_dict['value1'] = row.guid
				value_dict['value2'] = row.extensionid
				value_dict['value3'] = row.extensionname
				value_dict['value4'] = row.communicationip
				value_dict['value5'] = row.temperaturenumber
				value_dict['value6'] = row.warehouseid
				value_dict['value7'] = row.createdate.strftime("%Y-%m-%d %H:%M:%S")
				value_dict['value8'] = row.extensiontype
				value_dict['value9'] = row.inputsignal1
				value_dict['value10'] = row.inputsignal2
				value_dict['value11'] = row.inputsignal3
				value_dict['value12'] = row.inputsignal4
				value_dict['value13'] = row.inputsignal5
				value_dict['value14'] = row.inputsignal6
				value_dict['value15'] = row.inputsignal7
				value_dict['value16'] = row.inputsignal8
				value_dict['value17'] = row.inputsignalcount
				value_dict['value18'] = row.outputsignalflag1
				value_dict['value19'] = row.outputsignalflag2
				value_dict['value20'] = row.outputsignalflag3
				value_dict['value21'] = row.outputsignalflag4
				value_dict['value22'] = row.outputsignal1
				value_dict['value23'] = row.outputsignal2
				value_dict['value24'] = row.outputsignal3
				value_dict['value25'] = row.outputsignal4
				value_dict['value26'] = row.communicationstate
				value_dict['value27'] = row.remarkflag

				value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
				# 用.copy()就不会跟着改变
				value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

			return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]

def index(request):
	if request.method == 'GET':
		return render(request,'Module_test/data.html')
	else:
		querys = models.Extension.objects.all()  # 获取需要的字段名的数据
		value_dict = {'ExtensionID': '', 'ExtensionName': '', 'CommunicationIP': '', 'CreateDate': '' }  # 有几个需要的列就有多少value 包括Id
		value_list = []
		for row in querys:

			value_dict['ExtensionID'] = row.extensionid
			value_dict['ExtensionName'] = row.extensionname
			value_dict['CommunicationIP'] = row.communicationip

			value_dict['CreateDate'] = row.createdate.strftime("%Y-%m-%d %H:%M:%S")

			value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
			# 用.copy()就不会跟着改变
			value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪
		print(value_list)
		return HttpResponse(json.dumps(value_list) )  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
