import json


new_person = {
    "First Name": "First Name3",
    "Last Name": "Last Name3",
    "age": "29"
}

#reading person
with open('test.json', mode="r") as file:
    products = json.load(file)
products.append(new_person)

#reading each person index by using a loop    
for product in products:
    print(f"Product: {product['First Name']}, Age: {product['age']}")

#writing a new person
with open('test.json', mode='w') as file:
    json.dump(products, file, indent=4)