def lookup_inventory(inventory, sku):

    if sku not in inventory:
        raise KeyError("SKU not found in inventory.")
    return inventory[sku]