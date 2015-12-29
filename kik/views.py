# -*- coding: utf-8 -*-
from django.http import HttpResponse

from .integrations.pkb import get_report as pkb_report
from .integrations.documentolog import move_document, edit_document
from .integrations.gcvp import get_report as gcvp_report
from .integrations.scoring import prepare_message


def pkb_test(request):
	iins = [620915401414, 650905300738, 761205402631, 680221302107, 690625300199, 670221301652, 581210403430, 550815400457, 730328402850, 730624401108, 690614300149, 820702350896, 680425401550, 720522401307, 590626401534, 510125401229, 601020450189, 681103300736, 670727450300, 671016300375, 660814350098, 780716300360, 770828400601, 550110401274, 520607300721, 580210450519, 600501305018, 650915301572, 761021450017, 751001402462, 810321400338, 500217301101, 660222400023, 620810402967, 731121402174, 751029300660, 811108400709, 720710450131, 571030401048, 570613350125, 620422300757, 660714300721, 640808450494, 810506300842, 820613300360, 530621300591, 661025350408, 651210401608, 711013402490, 721125401720, 661113400664, 840819301520, 620429300537, 530522401200, 540610400371, 560411450240, 571209401487]
	for iin in iins:
		report = pkb_report(iin)
		# print report
	# report = pkb_report(iins[0])
	# print report
	return HttpResponse('Done')

def gcvp_test(request):
	gcvp_report()
	return HttpResponse('Done')

def scoring_test(request):
	prepare_message(request_id=3)
	return HttpResponse('Done')

def documentolog_move_test(request):
	move_document(doc_id='2519fcd4-111a-44e3-beee-5677ddad0306')
	return HttpResponse('Done')

def documentolog_edit_test(request):
	edit_document(doc_id='fdea9786-c9b5-4899-a595-56767cec0301', status=u'Да')
	return HttpResponse('Done')