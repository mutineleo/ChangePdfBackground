from PIL import Image,ImageEnhance


img=Image.open("a12a-modified_image.jpg")
img_contr_obj=ImageEnhance.Contrast(img)
factor=3
e_img=img_contr_obj.enhance(factor)
e_img.show()

