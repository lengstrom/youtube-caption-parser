import os, sys, pdb, json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from unicodedata import normalize
import requests

def make_json_from_xml(lang, vid_id, und_is_en, GB_is_en):
    lang_ = lang
    if lang == 'en' and und_is_en:
        lang_ = 'und'

    if lang == 'en' and GB_is_en:
        lang_ = 'en-GB'

    xml = requests.get('http://video.google.com/timedtext?lang=' + lang_ + '&v=' + vid_id).text
    soup = BeautifulSoup(xml, 'xml')
    fin_txt = FUCKXML([i for i in soup.children][0])
    
    with open('./' + lang + '.json', 'w') as f:
        f.write(json.dumps(fin_txt))

def FUCKXML(soup):
    out = []
    for child in soup.children:
        out.append({u'ts':child['start'],u'l':BeautifulSoup(child.text, 'lxml').text})
    return out
