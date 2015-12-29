# -*- coding: utf-8 -*-
import random

from ..serializers import RequestSerializer
from ..models import Request
from .documentolog import edit_document, move_document
from .gcvp import get_report as gcvp_report
from .pkb import get_report as pkb_report


def prepare_message(request):
	rv = RequestSerializer(request).data
	
	pkb = pkb_report(rv['renter']['personal_data']['iin'])
	rv['pkb'] = pkb
	
	gcvp = gcvp_report()
	rv['gcvp'] = gcvp

	print rv

def mock_scoring_result(request):
	import random
	def get_fio(person):
		return '%s %s.%s.' % (person.personal_data.get('last_name', ''), person.personal_data.get('first_name', ' ')[0], person.personal_data.get('middle_name', ' ')[0],)

	def get_bank():
		banks = [u'АО «Альянс Банк»', u'ТОО "«ПростоКредит»']
		return banks[random.randrange(0, 2)]

	def get_money():
		return random.randrange(100000, 1000000)

	def get_days():
		return random.randrange(50, 3000)

	status = u'Проблема'
	credit_report = u"""Согласно расширенному кредитному отчету ТОО «Первое кредитное бюро» у """ + unicode(get_fio(request.renter)) + u""" имеется """ + \
					u"""кредитная история по завершенным кредитам: 1 .Потребительский кредит в """ + unicode(get_bank()) + u""", сумма кредита """ + unicode(get_money()) + u""" тенге, """ + \
					u"""максимальное количество дней просрочки """ + unicode(get_days()) + u""" день, максимальная сумма просроченных взносов """ + unicode(get_money()) + u""" тенге."""
	if float(request.msap) < 0 or float(request.lpk['od']) > 65 or float(request.lpk['pd']) > 70:
		status = u'Нет'
		credit_report = u''
	if random.randrange(0, 100) < 40:
		status = u'Да'
		credit_report = u"""Согласно расширенному кредитному отчету ТОО «Первое кредитное бюро» """ + unicode(get_fio(request.renter)) + u""" действующих и завершенных кредитов не имеет"""

	edit_document(request.document_id, **{
		u'Статус_скоринга': status,
		u'Кредитный_отчет': credit_report,
	})
	move_document(request.document_id)