### Vehicle Routing Problem

This Python script solves the Vehicle Routing Problem (VRP), an optimization challenge involving routing a fleet of vehicles to serve customers efficiently.

#### Overview:
The script models the VRP using classes and functions:

- **Customer Class**: Represents a customer with attributes like ID, location (latitude and longitude), demand, and a visited flag.
- **Vehicle Class**: Represents a vehicle with attributes such as type, capacity, cost per kilometer, current route, current load, and total distance traveled.
- **calculate_distance Function**: Computes the Euclidean distance between two customer locations.
- **find_closest_customer Function**: Finds the closest unserved customer to a given customer.
- **construct_initial_routes Function**: Constructs initial routes by assigning customers to vehicles based on demand and capacity.
- **reset_customer_visits Function**: Resets the 'visited' flag for all customers.
- **all_customers_served Function**: Checks if all customers have been served.
- **calculate_route_cost Function**: Calculates the cost of a route based on distance traveled and vehicle cost per kilometer.
- **vehicle_routing_problem Function**: Main function to solve the VRP, constructing initial routes and calculating total distance and cost for each vehicle.

#### Usage:
**Input Data:**
- Define the depot location.
- Specify customer data including ID, location (latitude and longitude), and demand.
- Define vehicle data including type, capacity, and cost per kilometer.

**Execution:**
- Call the `vehicle_routing_problem` function with the provided input data to solve the VRP.
- The function outputs routes for each vehicle, including round trip distance, cost, demand served, and the route itself.

#### Dependencies:
The script requires the `math` module for distance calculations.

#### Result:
