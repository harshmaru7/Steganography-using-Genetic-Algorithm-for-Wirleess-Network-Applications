# This module is designed to extract the rgb channels of the image separately and save them into three separate files(using encryption)
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
class visual_cryptography:
	def __init__(self,imageName):
		self.imageName=imageName
	def encrypt(self):
		# We need to open the image and extract the pixel values from it
		# This part of the code is used to extract the pixel values of the image
		img=Image.open(self.imageName)
		#This returns the matrix of the pixels of the image
		arr=array(img)
		#print("The pixels of the image are:")
		#print(arr)
		row=len(arr)
		column=len(arr[0])
		#Now we are done with the extraction of image pixels from the given image

		#These three variables are used to store the corresponding channel pixel values
		red=""
		green=""
		blue=""
		# Now we need to parse the extracted matrix and extract pixel values of each channels
		count=0
		i=0
		j=0
		k=0

		while count<(row*column):
			#print("Progressing")
			#print(count)
			if i==row-1 and j==column-1:
				red=red+str(arr[i][j][0])
				green=green+str(arr[i][j][1])
				blue=blue+str(arr[i][j][2])
			else:
				red=red+str(arr[i][j][0])+','
				green=green+str(arr[i][j][1])+','
				blue=blue+str(arr[i][j][2])+','
			j=j+1
			if j>=column:
				j=0
				i=i+1
			count=count+1
		print("We have successfully extracted the rgb channels of the given image")
		#print("The red channel has:")
		#print(red)
		red=red.encode('utf-8')
		#print()
		#print("The green channel has:")
		#print(green)
		green=green.encode('utf-8')
		#print()
		#print("The blue channel has:")
		#print(blue)
		blue=blue.encode('utf-8')
		#This is the end of extraction phase of the pixels of the corresponding channels


		# Now we need to encrypt these pixel values 
		key = Fernet.generate_key()
		cipher_suite=Fernet(key)
		#Encrypting the red pixels
		cipher_text_red = cipher_suite.encrypt(red)
		test_red=cipher_suite.decrypt(cipher_text_red)
		print("The red pixel have been encrypted")
		#print("The encrypted text is:")
		#print(cipher_text_red)
		#print("The plain text is:")
		#print(test_red)

		#Encrypting the green pixels
		cipher_text_green = cipher_suite.encrypt(green)
		test_green=cipher_suite.decrypt(cipher_text_green)
		print("The green pixel have been encrypted")
		#print("The encrypted text is:")
		#print(cipher_text_green)
		#print("The plain text is:")
		#print(test_green)

		#Encrypting the blue pixels
		cipher_text_blue = cipher_suite.encrypt(blue)
		test_blue=cipher_suite.decrypt(cipher_text_blue)
		print("The blue pixel have been encrypted")
		#print("The encrypted text is:")
		#print(cipher_text_blue)
		#print("The plain text is:")
		#print(test_blue)
		#print()
		print("Important,")
		print(key)
		print("The key for the encryption is:",key.decode('utf-8'))
		print("Please note this key for decryption")
		#This brings us to the end of the encryption phase


		# Now the main task is to put these encrypted files into three different files
		# Now creating the file to store the red pixel values
		file_red=open('red_pixel','w')
		file_red.write(cipher_text_red.decode('utf-8'))
		file_red.write("\n")
		asd=str(row)+","+str(column)
		asd=cipher_suite.encrypt(asd.encode('utf-8'))
		asd=asd.decode('utf-8')
		file_red.write(asd)
		file_red.close()
		print("A file named red_pixel hsa been created to store the red pixels")

		# Now creating a fiel to store the blue pixel values
		file_green=open('green_pixel','w')
		file_green.write(cipher_text_green.decode('utf-8'))
		file_green.write('\n')
		file_green.write(asd)
		file_green.close()
		print("A file names green_pixel has been created to store the green pixels")
		#Now creating a file to store the green pixel values
		file_blue=open('blue_pixel','w')
		file_blue.write(cipher_text_blue.decode('utf-8'))
		file_blue.write('\n')
		file_blue.write(asd)
		file_blue.close()
		print("A file named blue_pixel has been created to store the blue pixels")
		#Now we have come to the end of the storing the pixel values into the files
		#print("The length of the red pixel is:",len(red.decode('utf-8')))
		#print("The length of the green pixel is:",len(green.decode('utf-8')))
		#print("The length of the blue pixel is:",len(blue.decode('utf-8')))

		#TEsting phase of the project
		file_red=open('red_pixel','r')
		qwerty1=file_red.read()
		#print("The lenght of red is:",len(qwerty1))
		file_red.close()
		file_green=open('green_pixel','r')
		qwerty2=file_green.read()
		#print("The lenght of green is:",len(qwerty2))
		file_green.close()
		file_blue=open('blue_pixel','r')
		qwerty3=file_blue.read()
		#print("The lenght of blue is:",len(qwerty3))
		file_blue.close()
		return(key.decode('utf-8'))