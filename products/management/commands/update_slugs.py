from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Product, Cake, CustomCake

class Command(BaseCommand):
    help = "Ensure all product-related models have unique slugs"

    def handle(self, *args, **kwargs):
        # Keep track of processed slugs to ensure uniqueness across all models
        processed_slugs = set()

        def ensure_unique_slug(obj):
            """Generate a unique slug for an object and save it."""
            base_slug = slugify(obj.name if hasattr(obj, 'name') else obj.flavor)
            slug = base_slug
            counter = 1
            while slug in processed_slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
            processed_slugs.add(slug)
            obj.slug = slug
            obj.save()
            self.stdout.write(f"Updated slug for {obj}: {slug}")

        # Process the Product model
        self.stdout.write("Processing Product model...")
        for product in Product.objects.all():
            if not product.slug or product.slug in processed_slugs:
                ensure_unique_slug(product)

        # Process the Cake model
        self.stdout.write("Processing Cake model...")
        for cake in Cake.objects.all():
            if not cake.slug or cake.slug in processed_slugs:
                ensure_unique_slug(cake)

        # Process the CustomCake model
        self.stdout.write("Processing CustomCake model...")
        for custom_cake in CustomCake.objects.all():
            if not custom_cake.slug or custom_cake.slug in processed_slugs:
                ensure_unique_slug(custom_cake)

        self.stdout.write(self.style.SUCCESS("All product slugs updated successfully!"))
