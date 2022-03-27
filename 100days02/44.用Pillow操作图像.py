from PIL import Image, ImageFilter

image = Image.open('./data/learn.jpg')
# print(image.format, image.size, image.mode)
# image.show()

# rect = 80, 20, 310, 360
# image.crop(rect).show()

# size = 128, 128
# image.thumbnail(size)
# image.show()
#
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()


# image.filter(ImageFilter.CONTOUR).show()

# image.convert(mode='L').show()

mord=3
image.filter(ImageFilter.GaussianBlur(mord)).show()