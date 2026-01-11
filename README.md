##Project Description
This project implements a simplified inventory and order management system for warehousing, 
developed for a fictional company. The system is designed to support efficient inventory access, 
real-time inventory updates, order processing, priority-based task handling, and basic inventory anaytics.
Multiple data structures are used to model real-world warehouse operations and ensure the system is efficient, 
scalable, and fault-tolerant.


##Function Descriptions
The system contains 5 core Python functions, each addressing a specific operational requirement. The lookup_inventory 
function retrieves the current stock level for a given product using its stock-keeping unit. This function facilitates 
rapid inventory access by utilizing a dictionary structure and ensures that invalid product identifiers are handled 
securely.

The update_inventory function updates inventory levels during restocking or shipping operations. It adjusts stock 
quantities in real time while preventing invalid updates, such as reducing inventory below zero, to maintain data 
integrity.

The process_orders function manages customer orders using a first-in, first-out workflow. Orders are processed in 
the sequence they are received, ensuring predictable and fair order fulfillment.

The process_priority_task function handles urgent tasks such as expedited orders or critical restocking requests. 
Tasks are retrieved based on priority, ensuring that high-impact operations are addressed first.

The generate_inventory_report function analyzes inventory data to identify items with low stock levels. This function 
supports reporting and space optimization by highlighting products that may require replenishment.


##How to Run the Program
To run the system, open the Python source file in IntelliJ and execute it directly. When the program runs, a built-in 
test block executes automatically, demonstrating the behavior of each function. Output is displayed in the Run window, 
including successful operations and error conditions that are handled.


##Error and Edge Case Handling
The system is designed to handle errors and edge cases gracefully. Invalid product identifiers are detected and 
reported without causing system failure. Inventory updates are validated to prevent harmful stock levels. Order and 
priority task processing functions safely handle empty queues by raising meaningful exceptions. These safeguards ensure 
reliable system behavior under unexpected or boundary conditions.


##Summary
This project demonstrates how multiple data structures can be applied effectively to solve real-world logistics 
problems. By combining dictionaries, queues, and priority-based structures, the system meets the operational needs of 
Corollary Warehousing while maintaining clarity, efficiency, and robustness.
