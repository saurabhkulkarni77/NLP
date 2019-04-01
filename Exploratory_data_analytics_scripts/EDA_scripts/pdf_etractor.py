from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
#converting pdf to imaget so that to extract text out of it for link12

PDF_file = "link12.pdf"
pages = convert_from_path(PDF_file, 500)
#print(pages)
image_counter = 1
for page in pages:
	filename = "page_"+str(image_counter)+".jpg"
	page.save(filename,'JPEG')
	image_counter = image_counter + 1
#get number of pages count
filelimit = image_counter - 1
print(filelimit)
outfile = "link123.txt"
f = open(outfile,'a')
for i in range(1, filelimit+1):
	filename = "page_"+str(i)+".jpg"
	text = str(((pytesseract.image_to_string(Image.open(filename)))))
	text = text.replace('-\n', '')
	f.write(text)
f.close()

