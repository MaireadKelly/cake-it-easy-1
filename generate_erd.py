import matplotlib.pyplot as plt
import networkx as nx


# Function to generate ERD using NetworkX and Matplotlib
def generate_erd():
    # Create a directed graph
    G = nx.DiGraph()

    # Adding entities and relationships
    entities = [
        "User",
        "CustomerProfile",
        "Order",
        "OrderLineItem",
        "Cake",
        "Category",
        "Basket",
        "BasketItem",
    ]

    # Define relationships
    relationships = [
        ("User", "CustomerProfile", "has many"),
        ("User", "Order", "has many"),
        ("User", "Basket", "has many"),
        ("CustomerProfile", "User", "belongs to"),
        ("Order", "User", "belongs to"),
        ("Order", "OrderLineItem", "has many"),
        ("OrderLineItem", "Order", "belongs to"),
        ("OrderLineItem", "Cake", "belongs to"),
        ("Cake", "Category", "belongs to"),
        ("Category", "Cake", "has many"),
        ("Basket", "User", "belongs to"),
        ("Basket", "BasketItem", "has many"),
        ("BasketItem", "Basket", "belongs to"),
        ("BasketItem", "Cake", "belongs to"),
    ]

    # Add nodes (entities)
    for entity in entities:
        G.add_node(entity)

    # Add edges (relationships)
    for src, tgt, rel in relationships:
        G.add_edge(src, tgt, label=rel)

    # Draw the ERD
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(15, 10))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=3000,
        font_size=10,
        font_weight="bold",
        arrows=True,
    )

    # Adding edge labels
    edge_labels = {(src, tgt): rel for src, tgt, rel in relationships}
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color="red", font_size=8
    )

    plt.title("Entity Relationship Diagram (ERD) for Cake It Easy Project")
    plt.show()


# Generate the ERD
generate_erd()
