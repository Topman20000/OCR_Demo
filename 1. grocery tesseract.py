import os
print('os imported')

# import packages
from PIL import Image
import pytesseract
import cv2

print('packages imported')

'''Part 1: store image names in dictionary'''

dir_name = ".\\grocery_cve_project"
# This is where we get our array
# of file names and store in results
result = os.listdir(dir_name)

key_index_store = {}
for i, e in enumerate(result):
    key_index_store[i] = e
    print(i, e)

#print("Our key value store is: ")
#print(key_index_store)

#  The types of file names we care about.
photo_extensions = [".jpg", ".png"]

for file_index in key_index_store:
    if key_index_store[file_index][-4:] in photo_extensions:
        # print("This is a file type we care about!")
        # print("This is where we do our OCR magic!")
        pass




'''Part 2: image processing'''


# declare the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

for e in key_index_store[e]:
	image_to_ocr = cv2.imread('grocery_cve_project_\\%s' % 'e')
	print(image_to_ocr)
	
	# convert to gray
	preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)

	#step 2: do binary and Otsu thresholding
	preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # step 3: Median Blur to remove noise in image
	preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

	'''Step 4: SAVE AND LOAD IMAGE AS PIL image'''

	# step 1: Save the processed image to convert to PIL image
	for i in key_index_store[i]:
		cv2.imwrite(("tempdir\\temp_img_%s.jpg" % 'i'), preprocessed_img)
		# step 2: load the image as a PIL/Pillow image
		preprocessed__pil_img = Image.open('temp_img.jpg')


	# step 1: do OCR of image using Tesseract
	text_extracted = pytesseract.image_to_string(preprocessed__pil_img)
	#Step 2: print the text
	print(text_extracted)