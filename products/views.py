from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cake, Category
from .forms import ProductForm, CommentForm, RatingForm, CustomCakeForm
from home.models import Comment, Rating
from django.contrib import messages
from django.db.models import Q
from django.views.generic import DetailView, ListView


# View to list all products
def all_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    query = None
    selected_category = None
    print(categories)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if "category" in request.GET:
            category_id = request.GET["category"]
            if category_id:
                selected_category = category_id
                # Filter products by selected category
                products = products.filter(category_id=category_id)

    context = {
        "products": products,
        "categories": categories,
        "search_term": query,
        "selected_category": selected_category,
    }

    return render(request, "products/products.html", context)


"""A view to show all products, including sorting, search queries and category filters """

@login_required
def custom_cake_order(request, pk):
    # Logic to handle custom cake order
    pass


# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    ratings = product.ratings.all()

    return render(
        request,
        "products/product_detail.html",
        {"product": product, "comments": comments, "ratings": ratings},
    )


# View All Cakes
class CakeListView(ListView):
    model = Cake
    template_name = "products/cake_list.html"
    context_object_name = "cake"


# View to Add New Product
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect("products:product_detail", pk=product.pk)
    else:
        form = ProductForm()
    return render(request, "products/add_product.html", {"form": form})


# View to edit existing product
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "products/edit_product.html", {"form": form})


# View to delete a product
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products:products")
    return render(request, "products/delete_product.html", {"product": product})


# View to handle adding comments
@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.customer = request.user.customer  # Assuming user is logged in
            comment.product = product
            comment.save()
            return redirect("products:product_detail", pk=product.id)
    else:
        form = CommentForm()
    return render(
        request, "products/add_comment.html", {"form": form, "product": product}
    )


# View to handle adding ratings
@login_required
def add_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.customer = request.user.customer
            rating.product = product
            rating.save()
            return redirect("products:product_detail", pk=product.id)
    else:
        form = RatingForm()
    return render(
        request, "products/add_rating.html", {"form": form, "product": product}
    )


@login_required
def custom_cake_order(request):
    if request.method == "POST":
        form = CustomCakeForm(request.POST, request.FILES)
        if form.is_valid():
            custom_cake = form.save()
            return redirect("products:product_detail", pk=custom_cake.pk)

    else:
        form = CustomCakeForm()
    return render(request, "products/custom_cake_order.html", {"form": formS})
