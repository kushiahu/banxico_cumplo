import requests
from requests import RequestException


class Banxico:

	def __init__(self, token: str) -> None:
		self.token = token
		self.__url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series'
		self.__headers = {'Bmx-Token': self.token}
		self.__params = {}
		self.__error = 'Algo salió mal con la solicitud. Revise el token, la identificación de la serie o el formato de fecha'

	def __get_only_data(self, data: dict) -> list:
		return [d['dato'] for d in data['bmx']['series'][0]['datos']]

	def get_serie_by_range_date(self, serie: str, init_date: str, end_data: str) -> list:
		url_udis = f'{self.__url}/{serie}/datos/{init_date}/{end_date}'
		response = requests.get(url_udis, headers=self.__headers, params=self.__params)
		if response.status_code != 200:
			raise RequestException(f'{self.__error} >> Status code: {response.status_code}')		
		return self.__get_only_data(response.json())



# token = '86bebc8b3193e923ba49ac91f00dc9798a44592fed4f60625279d9f1a977cd53'
# udi_serie = 'SP68257'
# peso_dolar = 'SF43718'
# init_date = '2021-12-25'
# end_date = '2021-12-31'

# banxico = Banxico(token)
# udis = banxico.get_serie_by_range_date(peso_dolar, init_date, end_date)

# print(udis)
