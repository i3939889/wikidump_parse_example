# -*- coding: utf-8 -*-

from lxml import etree
import wikitextparser as wtp
import mwparserfromhell
import codecs
import csv
import time
import os

FILENAME_WIKI='wiki/zhwiki-20181001-pages-articles.xml'
ENCODING = "utf-8"
count = 1
pcount = 1

def strip_tag_name(t):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t

def process_text(id,title,text):
    
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates()

    for template in templates:
        if 'linux' in template.name:
            print(id,text)
    
    del templates
    del wikicode

for event, elem in etree.iterparse(FILENAME_WIKI, events=('start', 'end')):
    count+= 1
        
    tname = strip_tag_name(elem.tag)
    
    if event == 'start':
        #print(event,tname)
        if tname == 'title':
            title = ''
            id = -1
            redirect = ''
            inrevision = False
            ns = 0
            text = ''
        elif tname == 'revision':
            # Do not pick up on revision id's
            inrevision = True
    else:
        #print('-',event,tname)
        val = elem.text
        if tname == 'title':
            title = val
        elif tname == 'text':
            text = val
        elif tname == 'id' and not inrevision:
            id = int(val)
        elif tname == 'redirect':
            redirect = elem.attrib['title']
        elif tname == 'ns':
            ns = int(val)
        elif tname == 'page':
            process_text(id,title,text)

        #free memory
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
            



