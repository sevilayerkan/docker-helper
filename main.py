#Import required libraries
import os
from pickle import TRUE
import subprocess

#Shows all containers with their states
#Tüm konteynerları gösterir
def show():
	subprocess.run("docker ps -a", shell=True)
    #Bug: If docker daemon is not running we got 'error during connect' error

#Shows logs given container
#Log kayıtlarını gösterir
def show_log():
    print("Var olan tüm konteynerlar şu şekildedir: \n")
    print(show() , "\n")
    containerName = input("\nLog kaydını görmek istediğiniz konteynerın ID'sini girin: \n")
    if (containerName==0) :
        print("error message")
    subprocess.run("docker logs -f --details " + containerName, shell=True)
    #Possible bug: We might got timeout error if log is empty or not exist.

#Stops given container
#İstenen konteynırı durdurur
def stop():
    print("Var olan tüm konteynırlar şu şekildedir: \n")
    print(show(), "\n")
    containerName = input("\nDurdurmak istediğiniz konteynerın ID'sini girin: \n")
    if (containerName==0) :
        print("error message\n")
    subprocess.run("docker stop " + containerName, shell=True)



#Shows runable functions
#Yapılabilecek fonksiyonları gösterir
def showFunctions():
	#NOT
	#BU FONKSİYON MAINDE OLMALI
	#THIS FUNCTION NEEDS TO BE IN MAIN

	#Show all functions
    print("1- Tüm konteynerları listele\n")
    print("2- Bir konteynerın logunu göster\n")
    print("3- Bir konteynerı durdurun\n")


    #Take user's choice as number
    choice = input("Lütfen istediğiniz işlemin numarasını girin:\n")

    #run chosen function
    while (choice != '0'):
        if (choice == '1'):
            return show() 
        elif (choice == '2'):
            return show_log()
        elif (choice == '3'):
            return stop()
        else:
            break

        """
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

#print(stop())




