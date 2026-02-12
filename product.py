
class Product:
    def __init__(self, product_id, name, unit_price, quantity):
        self.product_id = product_id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Unit Price: {self.unit_price}")
        print(f"Quantity: {self.quantity}")



class Customer:
    def __init__(self, customer_id, gender, name, loyalty_points, promotions, contact_no):
        self.customer_id = customer_id
        self.gender = gender
        self.name = name
        self.loyalty_points = loyalty_points
        self.promotions = promotions
        self.contact_no = contact_no

    def display_customer(self):
        print("\n--- Customer Details ---")
        print(f"Customer ID: {self.customer_id}")
        print(f"Gender: {self.gender}")
        print(f"Name: {self.name}")
        print(f"Loyalty Points: {self.loyalty_points}")
        print(f"Promotions: {self.promotions}")
        print(f"Contact No: {self.contact_no}")


class Invoice:
    def __init__(self, invoice_no, date, products):
        self.invoice_no = invoice_no
        self.date = date
        self.products = products
        self.total_price = self.calculate_total()

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.unit_price * product.quantity
        return total

    def display_invoice(self):
        print("\n--- Invoice Details ---")
        print(f"Invoice No: {self.invoice_no}")
        print(f"Date: {self.date}")
        print("\nPurchased Products:")
        for product in self.products:
            print(f"{product.name} - {product.quantity} x {product.unit_price}")
        print(f"\nTotal Price: {self.total_price}")



class PaymentHistory:
    def __init__(self, customer_id, invoice_no):
        self.customer_id = customer_id
        self.invoice_no = invoice_no

    def display_payment(self):
        print("\n--- Payment History ---")
        print(f"Customer ID: {self.customer_id}")
        print(f"Invoice No: {self.invoice_no}")



products = []
num_products = int(input("How many products? "))

for i in range(num_products):
    print(f"\nEnter details for Product {i+1}")
    pid = int(input("Product ID: "))
    pname = input("Product Name: ")
    unit_price = float(input("Unit Price: "))
    quantity = int(input("Quantity: "))

    product = Product(pid, pname, unit_price, quantity)
    products.append(product)

print("\nEnter Customer Details")
customer_id = int(input("Customer ID: "))
gender = input("Gender: ")
name = input("Name: ")
loyalty_points = int(input("Loyalty Points: "))
promotions = input("Promotions: ")
contact_no = input("Contact No: ")

customer1 = Customer(customer_id, gender, name, loyalty_points, promotions, contact_no)

print("\nEnter Invoice Details")
invoice_no = int(input("Invoice No: "))
date = input("Date (YYYY-MM-DD): ")

invoice1 = Invoice(invoice_no, date, products)


payment1 = PaymentHistory(customer_id, invoice_no)


print("\n==============================")
customer1.display_customer()
invoice1.display_invoice()
payment1.display_payment()
