import json
import os
import urllib.request

from scrapinghub import ScrapinghubClient

codelist = []
apikey = '11befd9da9304fecb83dfa114d1926e9'
client = ScrapinghubClient(apikey)
project = client.get_project(252342)

for job in list(project.jobs.iter_last(spider='myspider', state='finished')):
    codejob = job

print(codejob['key'])
lastcodejob = project.jobs.get(codejob['key'])

codecounter = 0
pagesection = 20
pagecounter = 101

for item in lastcodejob.items.iter():
    if not os.path.exists(r'/home/GoldenShark/static/images/' + item['code'] + ".jpg"):
        print('Downloading ' + item['code'] + ".jpg")
        urllib.request.urlretrieve(
            item['imgf'], r'/home/GoldenShark/static/images/' + item['code'] + ".jpg")
    if codecounter < pagesection:
        codelist.append(item)
        codecounter = codecounter + 1
    else:
        codelistobj = json.dumps(codelist)
        codelistfile = open(r'/home/GoldenShark/codelist/' +
                            str(pagecounter) + r'.json', 'w')
        codelistfile.write(codelistobj)
        codelistfile.close()
        codelist.clear()
        codecounter = 0
        pagecounter = pagecounter + 1

codelistobj = json.dumps(codelist)
codelistfile = open(r'/home/GoldenShark/codelist/' +
                    str(pagecounter) + r'.json', 'w')
codelistfile.write(codelistobj)
codelistfile.close()
