from algoliasearch import algoliasearch
from scrapinghub import ScrapinghubClient

apikey = '11befd9da9304fecb83dfa114d1926e9'
shclient = ScrapinghubClient(apikey)
project = shclient.get_project(252342)
asclient = algoliasearch.Client(
    "P7KK27HK91", 'ea4c0f459be0c5aa47abf593071a119e')
asindex = asclient.init_index("thzalgolia")
asindex.clear_index()
asindex.set_settings({"customRanking": ["desc(pday)"]})

for job in list(project.jobs.iter_last(spider='myspider', state='finished')):
    codejob = job

print(codejob['key'])
lastcodejob = project.jobs.get(codejob['key'])

imgbaseurl = 'https://www.alpacapapahub.com/images/'

for item in lastcodejob.items.iter():
    if item['imgf'] is not None and 'http' in item['imgf']:
        item['imgf'] = imgbaseurl + item['code'] + ".jpg"
        asindex.add_object(item)
