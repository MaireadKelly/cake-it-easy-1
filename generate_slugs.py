import json
from slugify import slugify

# Load JSON file
with open("cakes_data_fixed.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Fix slugs by generating them from product names
for item in data:
    if "fields" in item and "name" in item["fields"]:
        item["fields"]["slug"] = slugify(item["fields"]["name"])  # Convert name to a URL-friendly slug

# Save the updated JSON file
with open("cakes_data_fixed.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("✅ Slugs successfully generated!")