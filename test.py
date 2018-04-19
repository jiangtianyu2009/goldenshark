import json

from algoliasearch import algoliasearch

client = algoliasearch.Client("P7KK27HK91", 'ea4c0f459be0c5aa47abf593071a119e')
index = client.init_index("testind")
batch = json.load(open(r'/home/GoldenShark/codelist/101.json'))
index.add_objects(batch)
index.set_settings({"customRanking": ["desc(href)"]})
print(index.search("SSNI"))
