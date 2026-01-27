import os
def scan_directory(path):
    files=[]
    for item in os.listdir(path):
        full_path=os.path.join(path,item)
    if os.path.isfile(full_path):
        files.append(full_path)
    elif os.path.isfir(full_path):
        files.extend(scan_directory(full_path))
    return files
print(scan_directory("/project/logs"))
