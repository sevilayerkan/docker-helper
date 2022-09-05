#TODO
#1-Linuxta test edilecek
#2-https://www.youtube.com/watch?v=SZdQX4gbql0
#3-https://www.freecodecamp.org/news/use-the-rich-library-in-python/ veya curses


#Import required libraries
import os
import subprocess
import time as t

#Shows all containers with their states
#Tüm konteynerları gösterir
def show():
	subprocess.run("docker ps -a", shell=True)
    #Bug: If docker daemon is not running we got 'error during connect' error

def showImages():
    subprocess.run("docker images", shell=True)

#Shows logs given container
#Log kayıtlarını gösterir
def show_log():
    print("Var olan tüm konteynerlar şu şekildedir: \n")
    print(show() , "\n")
    containerName = input("\nLog kaydını görmek istediğiniz konteynerın ID'sini girin: \n").lower()
    if (containerName==0) :
        print("error message")
    subprocess.run("docker logs -f --details " + containerName, shell=True)
    #Possible bug: We might got timeout error if log is empty or not exist.

#Starts given container
#İstenen konteynırı başlatır
def start():
    print("Var olan tüm konteynırlar şu şekildedir: \n")
    print(show(), "\n")
    containerName = input("\nBaşlatmak istediğiniz konteynerın ID'sini girin: \n").lower()
    if (containerName==0) :
        print("error message\n")
    subprocess.run("docker start " + containerName, shell=True)
    repeat()


#Stops given container
#İstenen konteynerı durdurur
def stop():
    print("Var olan tüm konteynırlar şu şekildedir: \n")
    print(show(), "\n")
    containerName = input("\nDurdurmak istediğiniz konteynerın ID'sini girin: \n").lower()
    if (containerName==0) :
        print("error message\n")
    subprocess.run("docker stop " + containerName, shell=True)
    repeat()

#Restarts given container
#İstenen konteynerı durdurur
def restart():
    print("Var olan tüm konteynırlar şu şekildedir: \n")
    print(show(), "\n")
    containerName = input("\nYeniden başlatmak istediğiniz konteynerın ID'sini girin: \n").lower()
    if (containerName==0) :
        print("error message\n")
    subprocess.run("docker restart " + containerName, shell=True)
    repeat()

#Builds simple container from available images
#Uygun imajlardan basit bir konteyner oluşturur
def build():
    #show available images to user
    print("Mevcut imajlar şu şekildedir: \n")
    print(showImages())
	#imageName = input("\nKonteyner oluşrurmak istediğiniz imajı seçin:").lower()
	#if imageName==NULL:
		#print(error message)
		#choose recent
			#imageName = recent image
    #else:
    print("Demo web imajı oluşturulacaktır.\n")
    subprocess.run("docker build -t hello .")
    t.sleep(3)
    print("Tüm imajlar şu şekildedir:\n")
    t.sleep(3)
    print(showImages())
    repeat()

#Starts a container
#Konteyner başlatır
def run():
    subprocess.run("docker run -d -p 80:80 7b9")
    t.sleep(5)
    print("\nKonteyner oluşturuldu.\n")
    t.sleep(1)
    print(show())
    repeat()

#Stops and deletes given container
#Seçilen konteynerı durdurur ve siler
def deleteContainer():
    print("Var olan tüm konteynerlar şu şekildedir:\n")
    print(show())
    t.sleep(2)
    container_name=input("Silinmesi için bir konteyner seçin: \n").lower()
    t.sleep(1)
    sure=input("Emin misiniz? \nE:Seçtiğiniz konteyner durdurulur ve silinir! Bu işlem geri alınamaz! \nH:Vazgeçtim\n").lower()
    if(sure=='e'):
        subprocess.run("docker stop " + container_name, shell=True)
        print("Konteyner durduruldu şimdi silinecek.\n")
        t.sleep(2)
        subprocess.run("docker rm " + container_name, shell=True)
        t.sleep(2)
        print("Seçtiğiniz konteyner başarıyla silindi.\n")
        show()
    else:
        repeat()
    repeat()

def deleteImage():
    print("Var olan tüm imajlar şu şekildedir:\n")
    print(showImages())
    t.sleep(2)

    print("Bir imajın silimesi için referans verildiği konteyner silinmiş olmalıdır.\n")
    t.sleep(1)

    check_continue= input("Hala işleme devam etmek istiyor musunuz?  E/H\n").lower()
    if(check_continue=="e"):
        print("İşleme devam edilecektir.\n")
    else:
        print("İşlem sonlandırıldı.\n")
        repeat()

    image_name=input("Silinmesi için bir imaj seçin: \n").lower()
    t.sleep(1)
    sure=input("Emin misiniz? \nE:Seçtiğiniz imaj silinir! Bu işlem geri alınamaz! \nH:Vazgeçtim\n").lower()
    if(sure=='e'):
        print("Seçtiğiniz " + image_name + " imajı silinecek.\n")
        t.sleep(2)
        subprocess.run("docker rmi " + image_name, shell=True)
        t.sleep(2)
        print("Seçtiğiniz " + image_name + " imajı başarıyla silindi.\n")
        show()
    else:
        repeat()
    repeat()



#Shows runable functions
#Yapılabilecek fonksiyonları gösterir
def showFunctions():
	#NOT
	#BU FONKSİYON MAINDE OLMALI
	#THIS FUNCTION NEEDS TO BE IN MAIN

	#Show all functions
    print("0- Tüm imajları listele.\n")
    print("1- Tüm konteynerları listele.\n")
    print("2- Bir konteynerın logunu göster.\n")
    print("3- Bir konteynerı durdurun.\n")
    print("4- Bir konteynerı yeniden başlatın.\n")
    print("5- Bir konteynerı başlatın.\n")
    print("6- Bir konteyner inşa edin.\n")
    print("7- Bir konteynerı çalıştırın.\n")
    print("8- Bir konteynerı silin.\n")
    print("9- Bir imajı silin.\n")



    #Take user's choice as number
    choice = input("Lütfen istediğiniz işlemin numarasını girin:\n")

    #Run chosen function
    while (choice):
        if (choice == '1'):
            return show() 
        elif (choice == '2'):
            return show_log()
        elif (choice == '3'):
            return stop()
        elif (choice == '4'):
            return restart()
        elif (choice == '5'):
            return start()
        elif (choice == '6'):
            return build()
        elif (choice == '0'):
            return showImages()
        elif (choice == '7'):
            return run()
        elif (choice == '8'):
            return deleteContainer()
        elif (choice == '9'):
            return deleteImage()
        else:
            repeat()
        repeat()

def repeat():
    repeat = input("Başka bir işlem yapmak ister misiniz? Evet - E, Hayır - H\n").lower()
    if(repeat=='e'):
        print(showFunctions())
    elif(repeat=='h'):
        print("Güle güle :)")
        exit()
    else:
        print("Error message: geçersiz bir komut verdiniz")
        repeat()


#Primative test functions
print(showFunctions())

#start()

print(repeat())
    






