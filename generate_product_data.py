import json
import random
from slugify import slugify

# Define category mapping for cakes and accessories
category_mapping = {
    "Wedding": 1,
    "Birthday": 2,
    "Anniversary": 3,
    "Baby Shower": 4,
    "Gender Reveal": 5,
    "Communion": 6,
    "Confirmation": 7,
    "Christening": 8,
    "Other": 9,
    "Candles": 10,
    "Toppers": 11,
    "Banners": 12,
    "Balloons": 13,
}

# Generate Cakes Data (50 items)
cakes_data = []
for i in range(1, 51):
    occasion = random.choice(list(category_mapping.keys())[:9])  # Cakes use the first 9 categories
    name = f"{occasion} Cake {i}"
    description = f"Delicious {occasion.lower()} cake made with high-quality ingredients."
    price = round(random.uniform(20.0, 150.0), 2)
    category_id = category_mapping[occasion]
    slug = slugify(name)

    cakes_data.append({
        "model": "products.cake",
        "pk": i,
        "fields": {
            "name": name,
            "description": description,
            "price": price,
            "category": category_id,
            "image": "",
            "occasion": occasion.lower(),
            "is_gluten_free": random.choice([True, False]),
            "is_vegan": random.choice([True, False]),
            "allergens": "Contains gluten, dairy, eggs",
            "rating": round(random.uniform(3.0, 5.0), 1),
            "num_reviews": random.randint(5, 100),
            "slug": slug,
        },
    })

# Generate Accessories Data (20 items)
accessories_data = []
for i in range(51, 71):
    accessory_type = random.choice(list(category_mapping.keys())[9:])  # Accessories use last 4 categories
    name = f"{accessory_type} {i}"
    description = f"A high-quality {accessory_type.lower()} to complement your cake."
    price = round(random.uniform(2.0, 20.0), 2)
    category_id = category_mapping[accessory_type]
    slug = slugify(name)

    accessories_data.append({
        "model": "products.accessory",
        "pk": i,
        "fields": {
            "name": name,
            "description": description,
            "price": price,
            "category": category_id,
            "image": "",
            "accessory_type": accessory_type.lower(),
            "slug": slug,
        },
    })

# Save JSON files
with open("cakes_data_fixed.json", "w", encoding="utf-8") as cakes_file:
    json.dump(cakes_data, cakes_file, indent=4)

with open("accessories_data_fixed.json", "w", encoding="utf-8") as accessories_file:
    json.dump(accessories_data, accessories_file, indent=4)

print("✅ JSON files generated successfully: cakes_data_fixed.json & accessories_data_fixed.json")
