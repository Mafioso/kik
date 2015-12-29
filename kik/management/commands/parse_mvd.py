from django.core.management.base import BaseCommand, CommandError
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from bs4 import BeautifulSoup
import requests
import itertools
from kik.models import MVDPerson


def gen_range(start, stop, step):
    current = start
    while current < stop:
        next_current = current + step
        if next_current < stop:
            yield (current, next_current)
        else:
            yield (current, stop)
        current = next_current + 1


def parse_table(html_content):
    f = open('parse_output.txt', 'a')
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all(
            attrs={"align":"center", "cellpadding":"0", "cellspacing":"0", "border":"0", "width":"99%"})
    if len(tables)==1:
        table = tables[0]
    elif len(tables) > 1:
        tables.reverse()
        table = tables[0]
    else:
        return
    imgs = table.find_all('img')
    if not imgs:
        print 'no imgs'
        f.write('No imgs' + ' \n')
    for img in imgs:
        alt = img.attrs.get('alt','')
        f.write(alt.encode('utf-8')+ ' \n')
        print alt
        if alt:
            person = MVDPerson(name_year=alt)
            # person.save()
        else:
            f.write('None' + ' \n')
    f.close()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print 'parsing mvd database'
        x = '<table align="center" cellpadding="0" cellspacing="0" border="0" width="99%">'
        r = requests.get('http://mvd.gov.kz/portal/page/portal/mvd/MVD/mvd_nav_roz/look')
        parse_table(r.content)
        min = 1
        max = 878
        for i,j in gen_range(11, 878, 9):
            f = open('parse_output.txt', 'a')
            print i,j
            f.write(str(i)+', '+str(j)+' \n')
            f.close()
            r = requests.post(
                'http://mvd.gov.kz/portal/page/portal/mvd/MVD/mvd_nav_roz/look', 
                data={'x554106_d':'NEXT','x554106_fh':i, 'x554106_lh':j, 'x554106_p_action':'NP'}
                )
            parse_table(r.content)

            
