from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Product View
def product(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    ratings = product.ratings.all()

    return render(request, 'products/product_detail.html', {'product': product, 'comments': comments, 'ratings': ratings})


# View to Add New Product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


# View to edit existing product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})


# View to delete a product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:shop')
    return render(request, 'products/delete_product.html', {'product': product})


# View to list all products
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


# View to handle adding comments
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
    return render(request, "products/add_comment.html", {"form": form, "product": product})


# View to handle adding ratings
def add_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.customer = request.user.customer
            rating.product = product
            rating.save()
            return redirect("products:product_detail", pk=product.id)
    else:
        form = RatingForm()
    return render(request, 'products/add_rating.html', {'form': form, 'product': product})
