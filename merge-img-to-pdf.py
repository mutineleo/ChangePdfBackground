from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

def image_to_pdf(images, filename):
    (w, h) = landscape(letter)
    c = canvas.Canvas(filename, pagesize=landscape(letter))
    
    for image in images:
        c.drawImage(image, 0, 0, w, h)
        c.showPage()
        
    c.save()

images = ['/Users/a23135334/Downloads/faizan-notes/0.jpg', '/Users/a23135334/Downloads/faizan-notes/1.jpg', '/Users/a23135334/Downloads/faizan-notes/2.jpg','/Users/a23135334/Downloads/faizan-notes/3.jpg', '/Users/a23135334/Downloads/faizan-notes/4.jpg', '/Users/a23135334/Downloads/faizan-notes/5.jpg','/Users/a23135334/Downloads/faizan-notes/6.jpg', '/Users/a23135334/Downloads/faizan-notes/7.jpg', '/Users/a23135334/Downloads/faizan-notes/8.jpg']
image_to_pdf(images, 'images.pdf')
