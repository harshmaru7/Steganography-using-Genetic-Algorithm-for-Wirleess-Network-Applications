from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Utils import Utils
from Population import Population
from Chromosome import Chromosome
from Fitness import Fitness
from GA import GA
from Pit import Pit
from visual_cryptography import visual_cryptography
import time

def getMinDx(allGenes,solution):
        genes=allGenes
        minDX=abs(solution-genes[0])
        chosen=0
        for i in range(len(genes)):
            if abs(solution-genes[i])<minDX:
                minDX=abs(solution-genes[i])
                chosen=i
        for i in range(len(genes)):
            if chosen==i:
                genes[i]=(solution-genes[i])
            else:
                genes[i]=-1000
        return genes                                       

class Encrypt():
    def __init__(self):
        #Encryption of plain text
        message=input("Enter the message to be hidden within the given image: ");
        messageUtf=message.encode('utf-8')
        key = Fernet.generate_key()
        print("The key generated for this encryption is: ",key)
        print()
        time.sleep(1)
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(messageUtf)
        plain_text = cipher_suite.decrypt(cipher_text)
        data=cipher_text.decode('utf-8')
        data=data+'~'
        cipher=[]
        for i in data:
            cipher.append(ord(i))
        qwerty=cipher[:]

        #Extract pixel
        img=Image.open('rsz_abc.png')
        arr=array(img)
        row=len(arr)
        column=len(arr[0])
        testing=row
        testing1=column

        print('Initializing the initial population ')
        time.sleep(1)
        chromosomes= [None]*(row*column)
        index=0

        #Initialise chromosomes with pixel values
        for x in range(column):
            for y in range(row): 
                chromosomes[index]=Chromosome(index,arr[x][y][0],arr[x][y][1],arr[x][y][2],-1,x,y,-1)
                index+=1

        print("Starting the genetic algorithm...")
        time.sleep(1)
        geneticAlgoritm = GA(cipher,len(chromosomes))
        for i in range(len(cipher)):
            geneticAlgoritm.initializePopulation(chromosomes)
            pop = geneticAlgoritm.evolvePopulation()
            chroms = pop.getAllChromosome()
            for j in range(len(chroms)):
                chromosomes[j]=chroms[j]
        print("Genetic algorithm has completed execution..")
        time.sleep(1)


        print("Started burning the data into the image")
        time.sleep(1.5)
        if len(cipher)>(row*column):    
            print('The image will not be able to accomodate the data')
            print("Try with some other image")
        else:
            print('The image will be able to accomodate the data')
            time.sleep(1.5)
            i=0
            j=0
            k=0
            a=arr[:]
            count=0
            for i in range(row):
                for j in range(column):
                    for k in range(len(chromosomes)):
                        if chromosomes[k].getX()==i and chromosomes[k].getY()==j:
                            a[i][j][0]=chromosomes[k].getGene(0)
                            a[i][j][1]=chromosomes[k].getGene(1)
                            a[i][j][2]=chromosomes[k].getGene(2)
            print('We have now completed building the new image...')
            time.sleep(1)
            final_img=Image.fromarray(a)
            final_img.save('final.png')
            print('The image has been saved as final.png in the same folder as this program.')
            print()
            print()
            time.sleep(1.5)

            print('Visual cryptography algorithm has started to run')
            time.sleep(1.5)
            objVisual=visual_cryptography("final.png")
            keyVisual=objVisual.encrypt()
            print()
    
            print("Generating the pixel index table....")
            time.sleep(1.5)
            pitTable=[]
            for i in range(len(cipher)):
                pitTable.append(Pit())
            pitTableIndex = 0

            for i in range(len(cipher)):
                for j in range(len(chromosomes)):
                    if chromosomes[j].getSolutionId()==i:
                        test=chromosomes[j].getAllGenes()                
                        minDxs = getMinDx(chromosomes[j].getAllGenes(),cipher[i])
                        pitTable[pitTableIndex] = Pit(chromosomes[j].getX(),chromosomes[j].getY(),minDxs)
                        pitTableIndex+=1 
            for i in range(len(pitTable)):
                f = open("pit1.csv",'a')
                f.write(pitTable[i].toString()+"\n")
            f.close()
            print('The Pixel Index Table file has been generated.') 
        print('The key for decryption of the visual cryptography is: ',keyVisual)
        time.sleep(1.5)
        print('The key for decryption of message is: ',key.decode('utf-8'))
        time.sleep(1.5)

        pass1='The key for decryption of the visual cryptography is:'+keyVisual
        pass2='The key for decryption of message is:'+key.decode('utf-8')
        file=open('Passwords','w')
        file.write(pass1)
        file.write('\n')
        file.write(pass2)
        print('The keys for decryption are stored in Passwords file in the same folder as this code.')

def main():
    E=Encrypt()
 
if __name__ == '__main__':
    main()


