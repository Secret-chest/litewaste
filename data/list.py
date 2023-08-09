#!/usr/bin/python3

with open("list.txt", "w") as f:
    import os
    for root, dirs, files in os.walk("."):
       for name in files:
          print(os.path.join(root, name), file=f)

