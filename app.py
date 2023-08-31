from lib.Customer import Customer
from lib.Restaurant import Restaurant

# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create restaurants
restaurant1 = Restaurant("Pizza Place")
restaurant2 = Restaurant("Burger Joint")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 3)
customer2.add_review(restaurant1, 5)

# Calculate average star ratings
average1 = restaurant1.average_star_rating()
average2 = restaurant2.average_star_rating()

print("Average rating for", restaurant1.name, ":", average1)
print("Average rating for", restaurant2.name, ":", average2)

# Get restaurants reviewed by a customer
customer1_restaurants = customer1.restaurants()
print(customer1.full_name(), "reviewed these restaurants:", [restaurant.name for restaurant in customer1_restaurants])

# Get customers who reviewed a restaurant
restaurant1_customers = restaurant1.customers()
print(restaurant1.name, "was reviewed by these customers:", [customer.full_name() for customer in restaurant1_customers])


# Get restaurants reviewed by a customer
customer1_restaurants = customer1.restaurants()
print(customer1.full_name(), "reviewed these restaurants:", [restaurant.name for restaurant in customer1_restaurants])

# Get customers who reviewed a restaurant
restaurant1_customers = restaurant1.customers()
print(restaurant1.name, "was reviewed by these customers:", [customer.full_name() for customer in restaurant1_customers])

# Find customers by name
found_customer = Customer.find_by_name("John Doe")
if found_customer:
    print("Found customer:", found_customer.full_name())
else:
    print("Customer not found.")

# Find all customers with a given name
all_johns = Customer.find_all_by_given_name("John")
print("Customers with the given name 'John':", [customer.full_name() for customer in all_johns])
