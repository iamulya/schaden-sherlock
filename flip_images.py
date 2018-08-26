from PIL import Image
import os

path = "/home/amulya/Downloads/car-damage-dataset/damage_or_whole/whole"
def flip_image(image_path, saved_location):
    """
    Flip or mirror the image

    @param image_path: The path to the image to edit
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)

paths = [os.path.join(path,fn) for fn in next(os.walk(path))[2]]

for path in paths:
    new_path = path.split(".")[0] + "_flipped." + path.split(".")[1]
    flip_image(path, new_path)