
import fitz
doc = fitz.open('/Users/a23135334/Downloads/faizan-notes/ORM-3_L-1.pdf')
for page in doc:
    pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,
                          colorspace=fitz.csRGB, clip=None, alpha=True, annots=True)
    pix.save("/Users/a23135334/Downloads/faizan-notes/samplepdfimage-%i.jpg" % page.number)
    break