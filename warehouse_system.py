def lookup_inventory(inventory, sku):
    if sku not in inventory:
        raise KeyError("SKU not found in inventory.")
    return inventory[sku]

def update_inventory(inventory, sku, quantity_change):
    if sku not in inventory:
        raise KeyError("SKU not found in inventory.")
    if inventory[sku] + quantity_change < 0:
        raise ValueError("Insufficient stock for this operation.")

    inventory[sku] += quantity_change
    return inventory[sku]