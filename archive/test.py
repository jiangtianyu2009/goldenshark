import json

from algoliasearch import algoliasearch

asclient = algoliasearch.Client(
    "P7KK27HK91", 'ea4c0f459be0c5aa47abf593071a119e')
asindex = asclient.init_index("testind")
batch = json.load(open(r'/home/GoldenShark/codelist/101.json'))
asindex.add_objects(batch)
asindex.set_settings({"customRanking": ["desc(href)"]})
print(asindex.search("SSNI"))
