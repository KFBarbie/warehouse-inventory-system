from collections import deque

import heapq

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

def process_orders(order_queue):
    if not order_queue:
        raise IndexError("No orders to process.")
    return order_queue.popleft()

def process_priority_task(priority_queue):
    if not priority_queue:
        raise IndexError("No priority tasks available.")
    return heapq.heappop(priority_queue)