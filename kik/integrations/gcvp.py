import requests
from datetime import datetime

from django.conf import settings
from dateutil.relativedelta import relativedelta


def get_data(url=None):
	data = {
		'login': settings.DOCUMENTOLOG_LOGIN,
		'password': settings.DOCUMENTOLOG_PASSWORD,
	}
	r = requests.post(settings.DOCUMENTOLOG_LOGIN_URL, data=data)
	cookies = r.cookies

	gcvp_file = requests.get(url, cookies=cookies)
	return gcvp_file.content

def extract_intake_amount(data):
	return data.split('|')[7]

def extract_average_intake(data):
	return data.split('|')[8]

def get_report(url=None):
	url = 'http://kik.doc24.kz/media/download/f937d9a8-6acd-4647-9f40-56767955001c'

	gcvp_data = get_data(url).splitlines()
	general_info = gcvp_data[0]
	intakes = gcvp_data[1:]
	rv = {
		intake_amount: extract_intake_amount(general_info),
		average_intake: extract_average_intake(general_info),
	}
	return rv
