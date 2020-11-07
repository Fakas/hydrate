import hydrate
import json


log = r"C:\Users\matcaz\temp\ct.log"
drink_stats = r"C:\Users\matcaz\temp\drink_stats.json"

items = hydrate.search(log)

exclude = ("juicer", "maker", "toughasnails", "milkweed", "smoothie_book")
filtered = []

for item in items:
    bad = False
    for keyword in exclude:
        if keyword in item:
            bad = True
            break
    if not bad:
        filtered.append(item)

drinks = hydrate.generate_drinks(filtered)

with open(drink_stats, "w") as file:
    json.dump(drinks, file, indent=2)

print("here")