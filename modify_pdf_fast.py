import fitz
import numpy as np
import os
import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import tkinter as tk
from tkinter import *
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas


top=tk.Tk()
top.geometry('400x400')
top.title('Modify your PDF!')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

img_count=0
images = []
def image_to_pdf(images, filename):
    (w, h) = landscape(letter)
    c = canvas.Canvas(filename, pagesize=landscape(letter))
    
    for image in images:
        c.drawImage(image, 0, 0, w, h)
        c.showPage()
    c.save()

def split_pdf_then_remove(pdfPath):
    doc = fitz.open(pdfPath)
    for page in doc:
        pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,
                            colorspace=fitz.csRGB, clip=None, alpha=True, annots=True)
        pix.save("samplepdfimage.jpg")
        remove_bg("samplepdfimage.jpg", pdfPath)
        if os.path.exists("samplepdfimage.jpg"):
            os.remove("samplepdfimage.jpg")        

def remove_bg(imgPath, pdfPath):
    img = cv2.imread(imgPath)
    img = img + np.array([255, 255, 255])
    # img[img < 300] = 255
    # img[img > 430] = 0
    img[img > 480] = 0
    img[img > 450] = 60
    img[img > 420] = 90
    img[img > 390] = 120
    img[img > 360] = 150
    img[img > 300] = 210
    img[img > 280] = 230
    img[img > 255] = 255
    global img_count
    global images
    # Clip the pixel values to [0, 255] to avoid overflow
    img = np.clip(img, 0, 255).astype('uint8')
    modifiedImgPath = pdfPath[0:pdfPath.rindex('/')+1]+str(img_count)+'.jpg'
    img_count += 1
    cv2.imwrite(modifiedImgPath, img)
    images.append(modifiedImgPath)

def delete_images(images):
    for imagePath in images:
        if os.path.exists(imagePath):
            os.remove(imagePath)

def upload():
    global images
    global img_count
    pdfPath=easygui.fileopenbox()
    split_pdf_then_remove(pdfPath)
    modifiedPdfPath = pdfPath[0:pdfPath.rindex('.')]+'modified' +'.pdf'
    print("modifiedPdfPath : ", modifiedPdfPath)
    image_to_pdf(images, modifiedPdfPath)
    delete_images(images)
    print("\n\n\nPDF SUCCESSFULLY MODIFIED\n\n")
    img_count=0
    images = []

upload=Button(top,text="Modify the PDF",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)
top.mainloop()
