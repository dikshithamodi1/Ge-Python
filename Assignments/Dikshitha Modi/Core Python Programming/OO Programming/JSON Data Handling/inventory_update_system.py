import json
def update_inventory(product_name, quantity):
    file_path=r"C:\Users\260016573\Box\Python\Assignments\Dikshitha Modi\Core Python Programming\OO Programming\JSON Data Handling\inventory.json"
    #read from exsisting memory
    try:
        with open(file_path,"r") as file:
            inventory=json.load(file)
    except FileNotFoundError:
        inventory={}

    #update value
    inventory[product_name]=quantity

    #save update inventory back to file
    with open(file_path,"w") as file:
        json.dump(inventory,file,indent=4)

update_inventory("Laptop", 15)
    
