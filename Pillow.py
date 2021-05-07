from PIL import Image, ImageFilter
image = Image.open( 'test.jpg' )
print(image.format)
print(image.mode)
print(image.size)
image.show()
image_sharp = image.filter( ImageFilter.SHARPEN )
image_sharp.save( 'image_sharpened.jpg', 'JPEG' )
r,g,b = image_sharp.split()
exif_data = im._getexif()
exif_data
img_resized = image.resize((200,200))
print(img_resized.size)
