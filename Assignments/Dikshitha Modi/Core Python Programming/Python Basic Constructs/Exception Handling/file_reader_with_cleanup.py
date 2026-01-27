def read_config(filename):
    try:
        with open(filename,"r") as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        print("Not Found")
    finally:
        return "Check done"
print(read_config("missing.txt") )
