
import sys
from PIL import Image

images = []
for arg in sys.argv[1:]:          # every file name typed after the script name
    images.append(Image.open(arg))

images[0].save(
    "animation.gif",
    save_all=True,                # save ALL frames, not just the first
    append_images=images[1:],     # the frames that come after the first
    duration=300,                 # milliseconds per frame
    loop=0,                       # 0 = loop forever
)
print(f"Saved animation.gif with {len(images)} frames")
