import urllib.request
import json
import random
from pprint import PrettyPrinter

# Opening the CanIUse data.JSON file from GitHub [https://github.com/Fyrd/caniuse/blob/main/data.json] raw
with urllib.request.urlopen("https://raw.githubusercontent.com/Fyrd/caniuse/main/data.json") as json_file:
    json_data = json.load(json_file)

# Get the data
data = json_data.get("data")
web_components = [comp for comp in data]
    
# Get the web elements where
## browser support is over 95% (prefixed and not prefixed)
## and either HTML5 or CSS/CSS3
good_candidates = [item for item in data.values() 
    if ((item['usage_perc_y'] 
    + item['usage_perc_a']
    ) >= 95 
    and ('HTML5' in item['categories'] or 'CSS' in item['categories']))]

# Get 3x5 random sets (for blog post ideas)
random_sets = []
for i in range(3):
    random_sets.append(random.choices(good_candidates, k=5))
selected_items = [{(dict.get("title")) for dict in item} for item in random_sets]

# Using PrettyPrinter
pp = PrettyPrinter(indent=2)
pp.pprint(selected_items)
