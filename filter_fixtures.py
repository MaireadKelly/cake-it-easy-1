import json
from products.models import Product
from django.utils.text import slugify  # To generate slugs automatically

# File paths
input_file = "products/fixtures/expanded_fixtures_products.json"
output_file = "products/fixtures/filtered_fixtures_products.json"

# Load existing slugs from the database
existing_slugs = set(Product.objects.values_list("slug", flat=True))

# Filter and fix the JSON file
def filter_fixtures(input_file, output_file, existing_slugs):
    with open(input_file, "r") as file:
        data = json.load(file)

    filtered_data = []
    for item in data:
        fields = item["fields"]
        slug = fields.get("slug")

        # Generate a slug if it's missing
        if not slug:
            slug = slugify(fields["name"])
            fields["slug"] = slug

        # Skip duplicates
        if slug not in existing_slugs:
            filtered_data.append(item)

    with open(output_file, "w") as file:
        json.dump(filtered_data, file, indent=4)

    print(f"Filtered {len(data) - len(filtered_data)} duplicate or invalid entries.")
    print(f"Saved filtered data to {output_file}.")

# Run the filtering process
filter_fixtures(input_file, output_file, existing_slugs)
