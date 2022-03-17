from PIL import Image


def reduce_brightness(image_path):
    """
    function to  reduce brightness of a given image
    """
    image = Image.open(image_path)
    source = image.split()

    R, G, B = 0, 1, 2
    constant = 1.5  # constant by which each pixel is divided
    red = source[R].point(lambda i: i/constant)
    green = source[G].point(lambda i: i/constant)
    blue = source[B].point(lambda i: i/constant)

    image = Image.merge(image.mode, (red, green, blue))
    image.save('./modified.jpeg', 'JPEG', quality=100)


if __name__ == "__main__":
    image_path = "./test.jpeg"
    reduce_brightness(image_path)
