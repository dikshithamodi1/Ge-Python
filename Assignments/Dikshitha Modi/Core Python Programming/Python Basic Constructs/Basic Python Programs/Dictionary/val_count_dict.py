dic={"fruits":["apple","orange","banana"],
     "vegetables":["tomato","carrot"]
     }
for key,val in dic.items():
    if isinstance(val,list):
        print(f"{key} has {len(val)} items")
