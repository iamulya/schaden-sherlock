import os

path = "/home/amulya/Downloads/car-damage-dataset/data3a/validation/03-severe"
paths = [os.path.join(path,fn) for fn in next(os.walk(path))[2]]

for path in paths:
    new_path = path.split(".")[0] + "_val." + path.split(".")[1]
    os.rename(path, new_path)

