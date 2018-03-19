from scrapinghub import ScrapinghubClient
import json

codelist = []
apikey = '11befd9da9304fecb83dfa114d1926e9'
client = ScrapinghubClient(apikey)
project = client.get_project(252342)

for job in list(project.jobs.iter_last(spider='myspider', state='finished')):
    codejob = job

print(codejob['key'])
lastcodejob = project.jobs.get(codejob['key'])

for item in lastcodejob.items.iter():
    codelist.append(item)

codelistobj = json.dumps(codelist)
codelistfile = open(r'/home/GoldenShark/codelist.json', 'w')
codelistfile.write(codelistobj)
codelistfile.close()
