#Import required libraries
import os
import subprocess

#Shows all containers with their states
#Çalışan tüm containerları gösterir
def show():
	subprocess.call("docker ps -a", shell=True)


#Shows runable functions
#Yapılabilecek fonksiyonları gösterir
def showFunctions():
	#NOT
	#BU FONKSİYON MAINDE OLMALI
	#THIS FUNCTION NEEDS TO BE IN MAIN

	#Show all functions
    print("1- Tüm konteynırları listele\n")


    #Take user's choice as number
    choice = input("Lütfen istediğiniz işlemin numarasını girin:\n")

    #run chosen function
    while (choice != '0'):
        if (choice == '1'):
            return show() 
        else:
            break

        """elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        """
        

print(showFunctions())




