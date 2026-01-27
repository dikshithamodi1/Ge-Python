def invoke(command_name, commands_dict):
    if command_name in commands_dict:
        return commands_dict.get(command_name)()#() is req to execute command
print(invoke("start", {"start": lambda: "System started"}))
