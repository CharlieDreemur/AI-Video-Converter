from PIL import Image, PngImagePlugin
def resize_png(image_path):
    with Image.open(image_path) as im:
        width, height = im.size
        if width > 800 or height > 800:
            ratio = min(800/width, 800/height)
            new_size = (int(width*ratio), int(height*ratio))
            im = im.resize(new_size)
            im.save(image_path)