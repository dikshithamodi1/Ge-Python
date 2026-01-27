import os
def scan_files(path,depth=0):
    try:
        files=os.listdir(path)
        for item in files:
            full_path=os.path.join(path,item)
            if os.path.dir(full_path) or depth<3:#can recurse only if it's directory as it will have more depth to go into
                scan_files(full_path,depth+1)
            else:
                print(full_path)
    except RecursionError:
        print("Maximum recursion depth is reached")
        raise
scan_files("nonexsistent",1)
