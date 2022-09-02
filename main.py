#Import required libraries
import os
import subprocess

#Shows all containers with their states
#Çalışan tüm containerları gösterir


def show():
	subprocess.call("docker ps -a", shell=True)

#Shows logs given container
#Log kayıtlarını gösterir


def show_log(containerName):
    containerName = input(
        "Lütfen logunu görüntülemek istediğiniz konteynırın adını yazın: \n")
    if containerName == 0:
        print("error message\n")
    subprocess.call("docker log -f --details" + containerName, shell=True)


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
        elif (choice == '2'):
            return X
        /*elif (choice == '2'):
            return X
        """
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        elif (choice == '2'):
            return X
        """
        else:
            break


print(showFunctions())




