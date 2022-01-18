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
	serie_rsl = []

	banxico = Banxico(TOKEN)
	serie_rsl = banxico.get_serie_by_range_date(SERIES[serie], init_date, end_date)

	if serie_rsl:
		avg_data = average(serie_rsl)
		min_data = min(serie_rsl)
		max_data = max(serie_rsl)

		status_code = 202
		msg = 'Not problem with data!'

	return JsonResponse({
		'status_code': status_code, 'msg': msg,
		'serie_rsl': serie_rsl, 'avg_data': avg_data,
		'min_data': min_data, 'max_data': max_data,
	})