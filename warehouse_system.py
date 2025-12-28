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


def process_priority_tasks(priority_queue):

    if not priority_queue:
        raise IndexError("No priority tasks available.")
    return heapq.heappop(priority_queue)


def generate_inventory_report(inventory, low_stock_threshold):

    report = {}
    for sku, quantity in inventory.items():
        if quantity <= low_stock_threshold:
            report[sku] = quantity
    return report


#test block

if __name__ == "__main__":
    #sample inventory
    inventory = {
        "SKU1001":50,
        "SKU1002":10,
        "SKU1003":0
    }
    #Inventory lookup
    print("Inventory Lookup:", lookup_inventory(inventory, "SKU1001"))

    #Inventory Update
    print("Inventory after restock:", update_inventory(inventory, "SKU1002", 20))

    #Order Processing
    orders = deque(["Order1", "Order2", "Order3"])
    print("Processed order:", process_orders(orders))
    print("Processed order:", process_orders(orders))

    #Priority task handling
    priority_tasks=[]
    heapq.heappush(priority_tasks, (1, "Urgent Restock"))
    heapq.heappush(priority_tasks, (3, "Routine Check"))
    print("Priority Tasks:", generate_inventory_report(inventory, 5))

    #Analytics
    print("Low stock report:", generate_inventory_report(inventory, 5))

    #Error Handling
    try:
        lookup_inventory(inventory, "SKU1003")
    except Exception as e:
        print("Error Handled:", e)

    try:
        update_inventory(inventory, "SKU1002", -100)
    except Exception as e:
        print("Invalid Quantity:", e)