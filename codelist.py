import json
import os
import urllib.request

from algoliasearch import algoliasearch
from scrapinghub import ScrapinghubClient

codelist = []
codelistall = []
apikey = '11befd9da9304fecb83dfa114d1926e9'
shclient = ScrapinghubClient(apikey)
project = shclient.get_project(252342)
asclient = algoliasearch.Client(
    "P7KK27HK91", 'ea4c0f459be0c5aa47abf593071a119e')
asindex = asclient.init_index("testind")
asindex.set_settings({"customRanking": ["desc(href)"]})

for job in list(project.jobs.iter_last(spider='myspider', state='finished')):
    codejob = job

print(codejob['key'])
lastcodejob = project.jobs.get(codejob['key'])

codecounter = 0
pagesection = 15
pagecounter = 101
imgbaseurl = 'https://www.goldenshark.me/images/'

for item in lastcodejob.items.iter():

    if item['imgf'] is not None and 'http' in item['imgf']:
        if not os.path.exists(r'/home/GoldenShark/static/images/' + item['code'] + ".jpg"):
            print('Downloading ' + item['code'] + ".jpg from " + item['imgf'])
            urllib.request.urlretrieve(
                item['imgf'], r'/home/GoldenShark/static/images/' + item['code'] + ".jpg")
            item['imgf'] = imgbaseurl + item['code'] + ".jpg"
        else:
            print(item['code'] + ".jpg exist.")
            item['imgf'] = imgbaseurl + item['code'] + ".jpg"
            asindex.add_objects(item)

        codelistall.append(item)
        codelist.append(item)
        if codecounter < pagesection:
            codecounter = codecounter + 1
        else:
            codelistfile = open(r'/home/GoldenShark/codelist/' +
                                str(pagecounter) + r'.json', 'w')
            codelistfile.write(json.dumps(codelist))
            codelistfile.close()
            codelist.clear()
            codecounter = 0
            pagecounter = pagecounter + 1

if codelist:
    codelistfile = open(r'/home/GoldenShark/codelist/' +
                        str(pagecounter) + r'.json', 'w')
    codelistfile.write(json.dumps(codelist))
    codelistfile.close()

codelistallfile = open(r'/home/GoldenShark/codelist/000.json', 'w')
codelistallfile.write(json.dumps(codelistall))
codelistallfile.close()
