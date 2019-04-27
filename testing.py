# This module is mainly for the decryption purpose
# Here we import the required modules
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Utils import Utils
from Population import Population
from Chromosome import Chromosome
from Fitness import Fitness
from GA import GA
from Pit import Pit

# Here we build the pitTable from the generated pit1.csv file
file=open('pit1.csv','r')
a=file.readlines()
cipherLen=len(a)
pitTable=[]
for i in range(cipherLen):
    pitTable.append(Pit())
xValue=0
yValue=0
diff=[None]*3
index=0
for i in a:
    t=i.split(',')
    xValue=int(t[0])
    yValue=int(t[1])
    diff[0]=int(t[2])
    diff[1]=int(t[3])
    string=t[4]
    string=string[:len(string)-1]
    diff[2]=int(string)
    pitTable[index]=Pit(xValue,yValue,diff)
    index+=1
print('Pit table is complete')
#print('Length of the pit table is:',len(pitTable))
#print('The values in the pitTable is:')
#for i in range(cipherLen):
#    print("x:",pitTable[i].getX()," y:",pitTable[i].getY(),"deltas:",pitTable[i].getDeltas())
# Now we have generated the pitTable

# Now we need to read the image for decoding the hidden message
# Here we start the decoding part of the code
print("Reading the image for decoding")
#This part of the code is used httpto extract the pixel values of the image
img=Image.open('final.png')
#This returns the matrix of the pixels of the image
arr1=array(img)
height=len(arr1)
width=len(arr1[0])
#Now we are done with the extraction of image pixels from the given image
print('Successfully extracted the pixels of the image')
dcipherBytes=[None]*len(pitTable)
dcipherIndex=0
count=0
poi=0
toi=0
print('Extracting the details from the pixel index table and extracting the cipher text')
for i in range(len(pitTable)):
    for x in range(width):
        for y in range(height):
            if(pitTable[i].getX()==x and pitTable[i].getY()==y):
                count+=1
                decodedIndex=pitTable[i].getDecodedValueIndex()
                decodedValue=0
                pitValue=0
                # If the data is hidden inside the red pixel
                if(decodedIndex==0):
                    pitValue=pitTable[i].getDecodeValue()
                    if(pitValue>=0):
                        decodedValue=arr1[x][y][0] + pitTable[i].getDecodeValue()
                    else:
                        decodedValue=pitTable[i].getDecodeValue() + arr1[x][y][0]
                # If the data is hidden inside the green pixel    
                elif(decodedIndex==1):
                    pitValue=pitTable[i].getDecodeValue()
                    if(pitValue>=0):
                        decodedValue=arr1[x][y][1] + pitTable[i].getDecodeValue()
                    else:
                        decodedValue = pitTable[i].getDecodeValue() + arr1[x][y][1]
                # If the data is hidden inside the blue pixel
                elif(decodedIndex==2):
                    pitValue =  pitTable[i].getDecodeValue()
                    if(pitValue>=0):
                        decodedValue = arr1[x][y][2] + pitTable[i].getDecodeValue()
                    else:
                        decodedValue = pitTable[i].getDecodeValue() + arr1[x][y][2]
                dcipherBytes[dcipherIndex] = decodedValue
                dcipherIndex+=1
print('Successfully extracted the cipher text.')
asdf=""
for i in range(len(dcipherBytes)-1):
    asdf+=chr(dcipherBytes[i])
print('The encrypted string is:',asdf)         

#Now we need to decrypt the message to get the original message
key=input("Enter the key to decrypt the extracted message")
key=key.encode('utf-8')
print("The entered key is:",key)
cipher_suite = Fernet(key)
dcipherBytes=asdf.encode('utf-8')
plain_text = cipher_suite.decrypt(dcipherBytes)
plain_text=plain_text.decode('utf-8')
print("The message hidden in the image is:",plain_text)
print('We have successfully completed the extraction phase.')