# coding: utf-8
#
import logging
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from splinter import Browser


logger = logging.getLogger('django')


class Crawler(object):
    def __init__(self):
        self.browser = Browser()

    def exists_element_with_css(self, css):
        element = self.browser.find.by_css(css)
        return True if element else False

    def next_page(self):
        number_results = self.browser.find_by_css(
            '#breadcrumb > li:nth-child(5) > div > span')
        number_results = number_results.replace('"', '')
        number_results = number_results.replace(')', '')
        number_results = number_results.replace('(', '')
        number_results = number_results.replace('resultados', '')
        number_results = int(number_results)

        return number_results

    def visit_href(self, number):
        number = number_results / 6
        i = 0
        while i <= number:
            self.browser.visit(
                'http://kekanto.com.br/newsearch/page:%s?&cidade_id=266911&cat=36') % i

    def write_txt(self):
        if self.exists_element_with_css(
            '#bizes-content-list > li.box-white.biz-card.js_biz_info'):
            import pdb; pdb.set_trace()

            for element in self.browser.find_by_css('#bizes-content-list > li.box-white.biz-card.js_biz_info'):
                arquivo.write(str(element.text))
                arquivo.write('/n')
            arquivo.close()

    def run(self):
        self.browser.visit('http://kekanto.com.br/newsearch/page:1?&cidade_id=266911&cat=36')
        number = self.next_page() / 6
        i = 1
        while i <= number:
            self.write_txt()
            i+=1
            self.browser.visit('http://kekanto.com.br/newsearch/page:%s?&cidade_id=266911&cat=36') % i




@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def test1():
    print "HELLO"
