import math

# Classes and Structures
class Customer:
    def __init__(self, id, latitude, longitude, demand):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.demand = demand
        self.visited = False

class Vehicle:
    def __init__(self, type, capacity, cost_per_km):
        self.type = type
        self.capacity = capacity
        self.cost_per_km = cost_per_km
        self.route = []
        self.current_load = 0
        self.total_distance = 0
        
# Function to calculate Euclidean distance
def calculate_distance(customer1, customer2):
    delta_longitude = customer2.longitude - customer1.longitude
    delta_latitude = customer2.latitude - customer1.latitude
    distance = 100 * math.sqrt(delta_longitude**2 + delta_latitude**2)
    return distance

# Function to find the closest customer
def find_closest_customer(current_customer, customers, vehicle):
    closest_customer = None
    min_distance = float('inf')
    for customer in customers:
        if not customer.visited and vehicle.current_load + customer.demand <= vehicle.capacity:
            distance = calculate_distance(current_customer, customer)
            if distance < min_distance:
                min_distance = distance
                closest_customer = customer
    return closest_customer

# Route Construction with Dynamic Vehicle Assignment
def construct_initial_routes(vehicles, customers, depot):
    customers.sort(key=lambda c: c.demand, reverse=True)  # Sort by demand to try packing larger demands first

    # Filter to use only vehicles that are needed based on the total demand and vehicle capacities
    total_demand = sum(c.demand for c in customers)
    available_vehicles = [v for v in vehicles if v.capacity >= min(c.demand for c in customers)]

    potential_routes = []
    for customer in customers:
        assigned = False
        # Try to add customer to existing routes first
        for route in potential_routes:
            if route['load'] + customer.demand <= route['vehicle'].capacity:
                route['customers'].append(customer)
                route['load'] += customer.demand
                customer.visited = True
                assigned = True
                break
        
        # If customer not assigned, try to assign to a new vehicle if any vehicle is available
        if not assigned:
            for vehicle in available_vehicles:
                if customer.demand <= vehicle.capacity:
                    new_vehicle = Vehicle(vehicle.type, vehicle.capacity, vehicle.cost_per_km)
                    potential_routes.append({
                        'vehicle': new_vehicle,
                        'customers': [customer],
                        'load': customer.demand
                    })
                    customer.visited = True
                    break

    # Add depot as the start and end point for each route
    for route in potential_routes:
        route['vehicle'].route = [depot] + route['customers'] + [depot]
        route['vehicle'].current_load = route['load']

    return [route['vehicle'] for route in potential_routes]

# Helper function to reset the 'visited' flag for all customers
def reset_customer_visits(customers):
    for customer in customers:
        customer.visited = False

# Function to check if all customers are served
def all_customers_served(customers):
    return all(customer.visited for customer in customers)

# Cost Calculation
def calculate_route_cost(vehicle):
    total_cost = 0
    for i in range(len(vehicle.route) - 1):
        distance = calculate_distance(vehicle.route[i], vehicle.route[i + 1])
        vehicle.total_distance += distance  # update total distance for each vehicle
        total_cost += distance * vehicle.cost_per_km
    return total_cost

# The optimization function requires significant work to integrate an actual optimization algorithm.
# It has been left as a placeholder.
# Modified main process function
def vehicle_routing_problem(vehicles, customers, depot):
    reset_customer_visits(customers)
    assigned_vehicles = construct_initial_routes(vehicles, customers, depot)
    
    if not all_customers_served(customers):
        raise ValueError("Not all customers have been served.")

    # Calculate the final routes and total costs
    total_distance = 0
    total_cost = 0
    for vehicle in assigned_vehicles:
        vehicle_cost = calculate_route_cost(vehicle)
        total_distance += vehicle.total_distance
        total_cost += vehicle_cost
        print(f"Vehicle {vehicle.type}:")
        print(f"Round Trip Distance: {vehicle.total_distance} km, Cost: RM {vehicle_cost:.2f}, Demand: {vehicle.current_load}")
        route_str = " -> ".join(["Depot"] + ["C" + str(cust.id) for cust in vehicle.route[1:-1]] + ["Depot"])
        print(f"Route: {route_str}\n")

    print(f"Total Distance = {total_distance} km")
    print(f"Total Cost = RM {total_cost:.2f}")
    

# Data
depot = Customer(0, 4.4184, 114.0932, 0)
customers_data = [
    {'id': 1, 'latitude': 4.3555, 'longitude': 113.9777, 'demand': 5},
    {'id': 2, 'latitude': 4.3976, 'longitude': 114.0049, 'demand': 8},
    {'id': 3, 'latitude': 4.3163, 'longitude': 114.0764, 'demand': 3},
    {'id': 4, 'latitude': 4.3184, 'longitude': 113.9932, 'demand': 6},
    {'id': 5, 'latitude': 4.4024, 'longitude': 113.9896, 'demand': 5},
    {'id': 6, 'latitude': 4.4142, 'longitude': 114.0127, 'demand': 8},
    {'id': 7, 'latitude': 4.4804, 'longitude': 114.0734, 'demand': 3},
    {'id': 8, 'latitude': 4.3818, 'longitude': 114.2034, 'demand': 6},
    {'id': 9, 'latitude': 4.4935, 'longitude': 114.1828, 'demand': 5},
    {'id': 10, 'latitude': 4.4932, 'longitude': 114.1322, 'demand': 8},
    # Add the rest of the customers data here
]
vehicles = [
    {'type': "Type A", 'capacity': 25, 'cost_per_km': 1.2},
    {'type': "Type B", 'capacity': 30, 'cost_per_km': 1.5},
    # Define more vehicles if needed
]
customers = [Customer(**data) for data in customers_data]
vehicles = [Vehicle(**data) for data in vehicles]

# Execute the main process
vehicle_routing_problem(vehicles, customers, depot)
