# TODO
# 2-https://www.youtube.com/watch?v=SZdQX4gbql0
# 3-https://www.freecodecamp.org/news/use-the-rich-library-in-python/ veya curses


# Import required libraries
import os
import subprocess
import time as t


class DockerHelper:
    # Shows all containers with their states
    # Tüm konteynerları gösterir

    def show(self):
        subprocess.run("docker ps -a", shell=True)
    # Bug: If docker daemon is not running we got 'error during connect' error (needs to be deleted)
    # Shows only current running containers

    def showCurrent(self):
        subprocess.run("docker ps", shell=True)
        # Bug: If docker daemon is not running we got 'error during connect' error

    def showImages(self):
        subprocess.run("docker images", shell=True)

    # Shows logs given container
    # Log kayıtlarını gösterir
    # subprocess.run("docker logs -f --details " + containerName, shell=True)

    def show_log(self):
        print("Var olan tüm konteynerlar şu şekildedir: \n")
        print(self.show(), "\n")
        containerName = input(
            "\nLog kaydını görmek istediğiniz konteynerın ID'sini girin: \n").lower()
        if not containerName:
            print("Error: Konteyner ID'si boş olamaz.\n")
            return
        try:
            subprocess.run("docker logs -f --details " + containerName, shell=True)
            print("Log kaydı görüntüleniyor.\n")
        except subprocess.CalledProcessError:
            print("Error: Konteyner logları gösterilemiyor.\n")
       

    # Starts given container
    # İstenen konteynırı başlatır

    def start(self):
        print("Var olan tüm konteynırlar şu şekildedir: \n")
        print(self.show(), "\n")
        containerName = input(
            "\nBaşlatmak istediğiniz konteynerın ID'sini girin: \n").lower()
        if (containerName == 0):
            print("error message\n")
        subprocess.run("docker start " + containerName, shell=True)
        self.repeat()


    # Stops given container
    # İstenen konteynerı durdurur

    def stop(self):
        print("Var olan tüm konteynırlar şu şekildedir: \n")
        print(self.show(), "\n")
        containerName = input(
            "\nDurdurmak istediğiniz konteynerın ID'sini girin: \n").lower()
        if (containerName == 0):
            print("error message\n")
        subprocess.run("docker stop " + containerName, shell=True)
        self.repeat()

    # Restarts given container
    # İstenen konteynerı durdurur

    def restart(self):
        print("Var olan tüm konteynırlar şu şekildedir: \n")
        print(self.show(), "\n")
        containerName = input(
            "\nYeniden başlatmak istediğiniz konteynerın ID'sini girin: \n").lower()
        if (containerName == 0):
            print("error message\n")
        subprocess.run("docker restart " + containerName, shell=True)
        self.repeat()

    # Builds simple container from available images
    # Uygun imajlardan basit bir konteyner oluşturur

    def build(self):
        # show available images to user
        print("Mevcut imajlar şu şekildedir: \n")
        print(self.showImages())
        #imageName = input("\nKonteyner oluşrurmak istediğiniz imajı seçin:").lower()
        # if imageName==NULL:
        # print(error message)
        # choose recent
        # imageName = recent image
        # else:
        print("Demo web imajı oluşturulacaktır.\n")
        subprocess.run("docker build -t hello .")
        t.sleep(3)
        print("Tüm imajlar şu şekildedir:\n")
        t.sleep(3)
        print(self.showImages())
        self.repeat()

    # Starts a container
    # Konteyner başlatır

    def run(self):
        subprocess.run("docker run -d -p 80:80 7b9")
        t.sleep(5)
        print("\nKonteyner oluşturuldu.\n")
        t.sleep(1)
        print(self.show())
        self.repeat()

    # Stops and deletes given container
    # Seçilen konteynerı durdurur ve siler

    def deleteContainer(self):
        print("Var olan tüm konteynerlar şu şekildedir:\n")
        print(self.show())
        t.sleep(2)
        container_name = input("Silinmesi için bir konteyner seçin: \n").lower()
        t.sleep(1)
        sure = input(
            "Emin misiniz? \nE:Seçtiğiniz konteyner durdurulur ve silinir! Bu işlem geri alınamaz! \nH:Vazgeçtim\n").lower()
        if (sure == 'e'):
            subprocess.run("docker stop " + container_name, shell=True)
            print("Konteyner durduruldu şimdi silinecek.\n")
            t.sleep(2)
            subprocess.run("docker rm " + container_name, shell=True)
            t.sleep(2)
            print("Seçtiğiniz konteyner başarıyla silindi.\n")
            self.show()
        else:
            self.repeat()
        self.repeat()

    # Deletes image
    # İmajı siler

    def deleteImage(self):
        print("Var olan tüm imajlar şu şekildedir:\n")
        print(self.showImages())
        t.sleep(2)

        print("Bir imajın silimesi için referans verildiği konteyner silinmiş olmalıdır.\n")
        t.sleep(1)

        check_continue = input(
            "Hala işleme devam etmek istiyor musunuz?  E/H\n").lower()
        if (check_continue == "e"):
            print("İşleme devam edilecektir.\n")
        else:
            print("İşlem sonlandırıldı.\n")
            self.repeat()

        image_name = input("Silinmesi için bir imaj seçin: \n").lower()
        t.sleep(1)
        sure = input(
            "Emin misiniz? \nE:Seçtiğiniz imaj silinir! Bu işlem geri alınamaz! \nH:Vazgeçtim\n").lower()
        if (sure == 'e'):
            print("Seçtiğiniz " + image_name + " imajı silinecek.\n")
            t.sleep(2)
            subprocess.run("docker rmi " + image_name, shell=True)
            t.sleep(2)
            print("Seçtiğiniz " + image_name + " imajı başarıyla silindi.\n")
            self.show()
        else:
            self.repeat()
        self.repeat()

    def repeat(self):
        repeat = input(
            "Başka bir işlem yapmak ister misiniz? Evet - E, Hayır - H\n").lower()
        if (repeat == 'e'):
            print(self.showFunctions())
        elif (repeat == 'h'):
            print("Güle güle :)")
            exit()
        else:
            print("Error message: invalid command")
            self.repeat()

    
"""
    def showFunctions(self):
        # NOT
        # BU FONKSİYON MAINDE OLMALI
        # THIS FUNCTION NEEDS TO BE IN MAIN

        # Show all functions
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
        print("10- Şu an çalışan konteynerları göster.\n")

        # Take user's choice as number
        choice = input("Lütfen istediğiniz işlemin numarasını girin:\n")

        # Run chosen function
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
            elif (choice == '10'):
                return showCurrent()
            else:
                repeat()
            repeat()
"""





def main():
    docker = DockerHelper()

    # Shows runable functions
    # Yapılabilecek fonksiyonları gösterir
        
    while True:
        print("Merhaba, Docker Helper'a hoşgeldiniz.\n")
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
        print("10- Şu an çalışan konteynerları göster.\n")
        print("11- Çıkış yap.\n")


        choice = input("\nLütfen istediğiniz işlemin numarasını girin: [0-11] ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 11:
            print("Error: Hatalı seçim yaptınız. Lütfen 0-11 arası bir sayı girin.")
            continue

        choice = int(choice)
        if choice == 0:
            docker.showImages()
        elif choice == 1:
            docker.show()
        elif choice == 2:
            docker.show_log()
        elif choice == 3:
            docker.stop()
        elif choice == 4:
            docker.restart()
        elif choice == 5:
            docker.start()
        elif choice == 6:
            docker.build()
        elif choice == 7:
            docker.run()
        elif choice == 8:
            docker.deleteContainer()
        elif choice == 9:
            docker.deleteImage()
        elif choice == 10:
            docker.showCurrent()
        else:
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()
