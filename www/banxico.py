import requests
from requests import RequestException


class Banxico:

	def __init__(self, token: str) -> None:
		self.token = token
		self.__url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series'
		self.__headers = {'Bmx-Token': self.token}
		self.__params = {}
		self.__error = 'Algo salió mal con la solicitud. Revise el token, la identificación de la serie o el formato de fecha'
		self.__graph_list = []
		self.__data_list = []

	def __get_only_data(self, data: dict) -> list:
		return [float(d['dato']) for d in data['bmx']['series'][0]['datos']]

	def __get_list_data(self, data: dict) -> list:
		return [[d['fecha'], d['dato']] for d in data['bmx']['series'][0]['datos']]

	def get_serie_by_range_date(self, serie: str, init_date: str, end_date: str) -> None:
		url_udis = f'{self.__url}/{serie}/datos/{init_date}/{end_date}'
		response = requests.get(url_udis, headers=self.__headers, params=self.__params)
		if response.status_code != 200:
			raise RequestException(f'{self.__error} >> Status code: {response.status_code}')
		self.__graph_list = self.__get_list_data(response.json())
		self.__data_list = self.__get_only_data(response.json())

	def get_data_list(self) -> list:
		return self.__data_list

	def get_graph_list(self) -> list:
		return self.__graph_list