import json
from django.utils.text import slugify
from products.models import Cake

# Load existing slugs from the database
existing_slugs = set(Cake.objects.values_list("slug", flat=True))

# Path to your fixture
input_file = "products/fixtures/cakes_fixed_unique.json"
output_file = "products/fixtures/cakes_unique_slugs_final.json"


# Function to generate unique slugs
def generate_unique_slug(name, existing_slugs):
    base_slug = slugify(name)
    slug = base_slug
    counter = 1
    while slug in existing_slugs:
        slug = f"{base_slug}-{counter}"
        counter += 1
    existing_slugs.add(slug)
    return slug


# Update the fixture
with open(input_file, "r") as file:
    data = json.load(file)

for item in data:
    fields = item["fields"]
    fields["slug"] = generate_unique_slug(fields["name"], existing_slugs)

# Save the updated fixture
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print(f"Updated fixture saved to {output_file}")
