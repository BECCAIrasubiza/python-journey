
from PIL import Image

colours = ["red", "orange", "green", "blue"]
number = 1
for colour in colours:
    image = Image.new("RGB", (200, 200), colour)
    image.save(f"frame{number}.gif")
    number += 1
print("Saved frame1.gif ... frame4.gif")
