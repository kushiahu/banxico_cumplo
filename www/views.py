# Django
from django.http import JsonResponse
from django.shortcuts import render

# Utils
from .banxico import Banxico

# Constant
TOKEN = '86bebc8b3193e923ba49ac91f00dc9798a44592fed4f60625279d9f1a977cd53'
SERIES = {
	'udis': 'SP68257',
	'dolar': 'SF43718',
}

# Views
def home(request):
	return render(request, 'index.html', {})


# SIMPLE API
def api_get_data_serie(request, serie, init_date, end_date):
	status_code, msg = 404, 'Has not been removed!'
	avg_data, min_data, max_data = 0, 0, 0
	average = lambda serie: sum(serie) / len(serie)
	data_list, graph_data = [], []

	banxico = Banxico(TOKEN)
	banxico.get_serie_by_range_date(SERIES[serie], init_date, end_date)

	data_list = banxico.get_data_list()
	graph_data = banxico.get_graph_list()

	print(data_list)

	if data_list:
		avg_data = average(data_list)
		min_data = min(data_list)
		max_data = max(data_list)

		status_code = 202
		msg = 'Not problem with data!'

	return JsonResponse({
		'status_code': status_code, 'msg': msg,
		'data_list': data_list, 'graph_data': graph_data,
		'min_data': min_data, 'max_data': max_data,
		'avg_data': avg_data,
	})