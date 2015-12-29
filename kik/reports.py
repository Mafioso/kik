import os
import datetime
import time
from docxtpl import DocxTemplate
from django.conf import settings as ns
from .models import Person

AGENDA_DIR = getattr(ns, 'AGENDA_DIR', '/media/agendas')
TEMPLATE_DIR = getattr(ns, 'TEMPLATE_DIR', '/media/templates')
pj = os.path.join

def build_agenda(**kwargs):
    cnt = kwargs.get('cnt', 5)
    #persons = Person.build_agenda(cnt)
    file_dir = AGENDA_DIR
    fname = 'agenda__{}.docx'.format(str(time.time()))
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    full_filename = pj(file_dir, fname)
    if not os.path.isfile(full_filename):
        tpl = DocxTemplate(pj(TEMPLATE_DIR, 'forte_bank_assignments_of_protocol.docx'))
        context = {
            # here must be context
        }
        tpl.render(context)
        tpl.save(full_filename)
    return full_filename