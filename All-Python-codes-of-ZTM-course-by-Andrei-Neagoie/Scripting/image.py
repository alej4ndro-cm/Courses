from PIL import Image, ImageFilter

img = Image.open(
    './Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/blur.png", "png")

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/smooth.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/sharpen.png", "png")

# it converts the image to grey scale, that is Black and White. Similarly RGB = Red Green Blue
filtered_img = img.convert('L')
filtered_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/grey.png", "png")

# filtered_img.show()    # this opens the image in the default player

rotated_img = img.rotate(45)
rotated_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/rotated.png", "png")

# but this can ruin the aspect ratio hence we use thumbnail method
resized_img = img.resize((100, 50))
resized_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/resized.png", "png")

box = (100, 100, 400, 400)
cropped_img = img.crop(box)
cropped_img.save(
    "./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/cropped_img.png", "png")

# it will keep max. 50*50 aspect ratio, it can be like 30*50, but it won't exceed 50 pixels
img.thumbnail((100, 50))
img.save("./Courses/All-Python-codes-of-ZTM-course-by-Andrei-Neagoie/Scripting/Pokedex/thumbnailed.png", "png")
