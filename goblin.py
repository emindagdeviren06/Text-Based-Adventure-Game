
import PIL.Image

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Global variable to hold the ASCII image
ascii_image = ""  # Initialize at the top level
image_generated = False  # Flag to track if the image has been generated

# Resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to a string of ASCII characters
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def generate_ascii_image(new_width=100):
    global ascii_image, image_generated  # Declare to modify global variables
    # Attempt to open the image from user-input
    path = "goblin1.jpg"
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"{path} is not a valid pathname to an image. Error: {e}")
        return  # Exit the function if the image can't be opened

    # Process the image and convert to ASCII
    new_image_data = pixel_to_ascii(grayify(resize_image(image)))

    # Format the ASCII string
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    # Mark the image as generated
    image_generated = True


def get_ascii_image():
    """Return the ASCII image, generating it if it hasn't been done yet."""
    if not image_generated:
        generate_ascii_image()  # Generate ASCII art if it hasn't been done yet
    return ascii_image
