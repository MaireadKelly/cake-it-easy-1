import json
from products.models import Product

# File paths
input_file = "products/fixtures/expanded_fixtures_products.json"
output_file = "products/fixtures/filtered_fixtures_products.json"

# Load existing slugs from the database
existing_slugs = set(Product.objects.values_list("slug", flat=True))

# Filter the JSON file
def filter_fixtures(input_file, output_file, existing_slugs):
    with open(input_file, "r") as file:
        data = json.load(file)

    filtered_data = [item for item in data if item["fields"]["slug"] not in existing_slugs]

    with open(output_file, "w") as file:
        json.dump(filtered_data, file, indent=4)

    print(f"Filtered {len(data) - len(filtered_data)} duplicate entries.")
    print(f"Saved filtered data to {output_file}.")

# Run the filtering process
filter_fixtures(input_file, output_file, existing_slugs)
