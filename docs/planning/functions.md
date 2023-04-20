# Fonksiyonlar

Bu dosya ilk fazlarda dahil edilecek fonksiyonların pseudocodelarını içerir.

- "*" işareti ile gösterilenlerin faz2'de
- "**" işareti ile gösterilenlerin faz3'te

yapılması planlanmaktadır.

## checks docker is installed

TR: Docker'ın kurulu olup olmadığını kontrol eder

``` python
check_install() bool *
{
 if(docker is installed){
  return 1
 } else{
  return 0
 }
}
```

## Shows runable functions

TR: Yapılabilecek fonksiyonları gösterir

``` python
showFunctions()
{
 #NOT
 #BU FONKSİYON MAINDE OLMALI
 #THIS FUNCTION NEEDS TO BE IN MAIN
 
 show all functions
 #take user's choice as number
 chouse = input(num)
 
 
 #run chosen function
 switch (num)
  case 0:
   f1()
  case 1:
   f2()
  .
  .
  .

} 
```

## Installs docker

TR: Sisteme docker kurar

``` python
install()* {
 if(isInstalled){
  print(Docker already installed)
  break
 } else {
  install docker
 }

}
```

## Shows running containers

TR: Çalışan containerları gösterir

``` python
show() {
 print(docker ps -al)
}
```

## Shows logs given container

TR:  Log kayıtlarını gösterir

``` python
show_log(containerName) {
 if containerName==NULL
  print(error message)
  break
 docker log -f --details containerName
}
```


## ???
docker compose(){

}

## Builds simple container from available images

TR:  Uygun imajlardan basit bir konteynır oluşturur

``` python
build()
{
 show available images to user
 imageName = input()
 if imageName==NULL
  print(error message)
  choose recent
   imageName = recent image
 docker build imageName
}
```

## Starts a container

TR: Konteynır başlatır

``` python
run(containerName)
{
 if containerName==NULL
  print(error message)
  break
 docker run containerName
}
```

## Pull an image or a repository from a registry (from given list)

TR: Registry'den imaj veya bir repository çeker (verilen listeden)

``` python
pull() *
{
 show options
 x = input(option)
 docker pull x
}
``` 

## ?

``` python
start()
{

 #GEREK VAR MI?
 
}
```

## Stops given container

TR: İstenen konteynırı durdurur

``` python
stop(containerName)
{
 if containerName==NULL
  print(error message)
  break
 docker stop containerName
}
```

## Restarts given container

``` python
restart(containerName)
{
 if containerName==NULL
  print(error message)
  break
 docker restart containerName
}
```

## Delete given container

``` python
delete(containerName) *
{
 if containerName==NULL
  print(error message)
  break
 docker delete containerName
}
```

## Mounts given file to docker

TR: Verilen dosyaları Dockera bağlar

``` python
mount() *
{
 source = input(file name)
 destination = input(file name)
 imageName = input(image name)
 docker mount imageName source destination
}
```

## For risky and advanced level functions

TR: Riskli ve ileri düzey fonksiyonlar için

``` python
advancedMod() **
{

 key = input(****)
 encode key
 store key somewhere
 
 //GÜNCELLENMELİ

}
```
