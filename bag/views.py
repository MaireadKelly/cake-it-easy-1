from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Cake


# View that renders the bag contents page
def view_bag(request):
    """A view that renders the bag contents page"""
    return render(request, "bag/bag.html")


# View to add a quantity of the specified cake to the shopping bag
def add_to_bag(request, cake_id):
    """Add a quantity of the specified cake to the shopping bag"""
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = request.POST.get("quantity")
    redirect_url = request.POST.get("redirect_url", reverse("view_bag"))

    # Get the bag session or create a new one if not exist
    bag = request.session.get("bag", {})

    # Handle the case where quantity is missing
    if not quantity:
        messages.error(request, "Quantity not specified. Please try again.")
        return redirect(redirect_url)

    # Convert quantity to an integer and validate it
    try:
        quantity = int(quantity)
        if quantity <= 0:
            messages.error(request, "Please enter a valid quantity.")
            return redirect(redirect_url)
    except ValueError:
        messages.error(request, "Invalid quantity. Please enter a valid number.")
        return redirect(redirect_url)

    # Adding items to bag
    if str(cake_id) in bag:
        bag[str(cake_id)] += quantity
        messages.success(
            request, f"Updated {cake.name} quantity to {bag[str(cake_id)]}"
        )
    else:
        bag[str(cake_id)] = quantity
        messages.success(request, f"Added {cake.name} to your bag")

    # Save the updated bag to the session
    request.session["bag"] = bag
    return redirect(redirect_url)


# View to update the quantity of a specified cake in the bag
def update_bag(request, cake_id):
    """Adjust the quantity of the specified cake in the shopping bag"""
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = request.POST.get("quantity")

    # Get the bag session or create a new one if not exist
    bag = request.session.get("bag", {})

    # Handle the case where quantity is missing
    if not quantity:
        messages.error(request, "Quantity not specified. Please try again.")
        return redirect("view_bag")

    # Convert quantity to an integer and validate it
    try:
        quantity = int(quantity)
        if quantity < 0:
            messages.error(request, "Please enter a valid quantity.")
            return redirect("view_bag")
    except ValueError:
        messages.error(request, "Invalid quantity. Please enter a valid number.")
        return redirect("view_bag")

    # Update items in the bag
    if quantity > 0:
        bag[str(cake_id)] = quantity
        messages.success(
            request, f"Updated {cake.name} quantity to {bag[str(cake_id)]}"
        )
    else:
        bag.pop(str(cake_id), None)
        messages.success(request, f"Removed {cake.name} from your bag")

    # Save the updated bag to the session
    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


# View to remove a cake from the shopping bag
def remove_from_bag(request, cake_id):
    """Remove the specified cake from the shopping bag"""
    try:
        cake = get_object_or_404(Cake, pk=cake_id)

        # Get the bag session or create a new one if not exist
        bag = request.session.get("bag", {})

        # Remove items from the bag
        bag.pop(str(cake_id), None)
        messages.success(request, f"Removed {cake.name} from your bag")

        # Save the updated bag to the session
        request.session["bag"] = bag
        return redirect("view_bag")

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect("view_bag")
