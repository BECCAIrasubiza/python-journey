
import sys
from PIL import Image


def main():
    filenames = sys.argv[1:]
    check_files(filenames)
    speed = ask_speed()

    images = []
    for name in filenames:
        try:
            images.append(Image.open(name))
        except FileNotFoundError:
            sys.exit(f"{name} does not exist")

    images[0].save(
        "animation.gif", save_all=True, append_images=images[1:], duration=speed, loop=0
    )
    print(f"Saved animation.gif: {len(images)} frames, {speed} ms each")


def check_files(filenames):
    if len(filenames) < 2:
        sys.exit("Give at least 2 images")
    for name in filenames:
        if not (name.endswith(".gif") or name.endswith(".png") or name.endswith(".jpg")):
            sys.exit(f"{name} is not a .gif, .png or .jpg file")


def valid_speed(text):
    """Return True if text is a whole number from 50 to 2000."""
    try:
        number = int(text)
    except ValueError:
        return False
    return number >= 50 and number <= 2000


def ask_speed():
    while True:
        text = input("Milliseconds per frame (50-2000): ")
        if valid_speed(text):
            return int(text)
        print("Please type a whole number between 50 and 2000.")


if __name__ == "__main__":
    main()
