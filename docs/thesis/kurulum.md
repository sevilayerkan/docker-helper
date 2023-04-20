# Kurulum (Gerekli Uygulamalar)

Kurulumlara başlamadan şu an üstlendiğim proje ve kullanabileceğimiz teknolojilere göre bir planlama yaptım. Bu planlamada DevOps süreçlerini düşündüm ve buna göre bir liste çıkardım. Bu listeye yazılım geliştirme ve deployment için çeşitli programları da eklediğimde listemin son hali şu şekilde oldu.

- IDE/Kod Editörü: VS Code, Notepad ++
- Versiyon kontrolü: Git
- Yazılım Geliştirme: Python, Go, C
- İşletim Sistemi Ortamları: WSL, Ubuntu, Debian, Oracle Virtual Box
- Diğer: Docker, Docker Desktop, MobaXTerm

Kurulum süreçleri tamamlanırken uygulamaların kullanımı hakkında ilgili dokümantasyonları okuyarak bilgi edindim. Bu şekilde de kurulumlar hem gerçekleşirken vaktimi değerlendirmiş oldum hem de bu programları daha efektif kullanmak için kendime yatırım yapmış oldum.

## VS Code

## Notepad ++

Not alma, dokümantasyon takibi tutma amacıyla kişisel olarak da kullandığım bu uygulama aynı zamanda kod editörü olarak da kullanılabiliyor. 2003 yılında Don Ho tarafından Windows işletim sistemine sahip cihazlar için C++ ile geliştirilen Notepad++ bir metin ve kaynak kod editörü olarak kullanılabiliyor. Sekmeli çalışma yapmamıza olanak verir, 78’den fazla programlama dili için syntax desteği sunar, ekran bölme, satır kaydetme, metin tamamlama, plugin/macro desteği gibi çeşitli güzel özellikleri vardır. Ayrıca GNU General Public lisansıyla lisanslanmış özgür bir yazılımdır.
Dünya çapında ve benim bu uygulamayı tercih etmemdeki en önemli etmen ise geliştirildiği teknolojiler sebebiyle uygulama boyutunun küçük olması ve CPU gibi sistem kaynaklarını daha az kullanması. Bu sayede bilgisayarın güç kullanımı düşüyor ve çevreye daha az karbon ayak izi bırakmış oluyoruz.

## Git

Özgür bir versiyon kontrol sistemi olan git Linus Torvalds tarafından 2005 yılında Linux kernelının geliştirmesi sırasında diğer kernel geliştiricilerinin katkı sağlayabilmesi için özgür, ücretsiz bir alternatif gerekliliğinden hareketle ortaya çıkmıştır. Geliştirilmesindeki en önemli neden aslında daha önceden kullanılan BitKeeper’ın ücretsiz kullanımındaki değişiklikti.
Bu teknolojiyi kullanmak için ilgili uygulamaları indirdim ve git sunucusuna bağlantı yapabilmek için GitHub hesabımdan yeni SSH anahtarı oluşturup git shelli üzerinde tanımladım. Ve VSCode üzerinde gerekli clientleri kullanarak da GitHub hesabımı yazılım geliştirme ortamıma bağlamış oldum.

Bunun ardından git bilgimi tazelemek için çeşitli git makalelerine kısa bir göz attım.

Git dokumanı için : /git.md

## WSL

Çalışmak için Linux bir makineye/shelle gereksinimim olabileceğinden Windows’un Windows Subsystem for Linux olarak bilinen Linux komutlarının çalıştırılmasını sağlayan uyumluluk katmanını Ubuntu işletim sistemi kullanarak denedim.

### Debian
WSL’in ihtiyaçlarımı karşılayacağından emin olmadığımdan kullanabileceğim, elimin altında duracak birkaç Linux dağıtımı seçtim ve kurulumu için gerekli iso dosyasını indirdim.

### Ubuntu

Debian’daki aynı sebeble bu Linux dağıtımının da iso dosyasını indirdim.
Oracle Virtual Box: İndirdiğim Linux dağıtımlarını kullanmak için bu uygulamayı kullanmayı planladım. Oracle Virtual Box 2007 yılında x86 sistemler için sanallaştırma desteği sağlayan open source bir hypevisor dır.

Kurulumun ardından indirdiğim Linux dağıtımlarından Debian 11’i UI (User Interface) olmadan network ve benzeri işler için gerekli araçları da ekleyerek yükledim bu şekilde Linux çalışma ortamımı tamamlamış oldum.

## MobaXterm

Cloud veya OnPrem sunuculara bağlanmam gerekebileceğinden bir SSH  client olan bu uygulamayı kurdum ve üzerinde nasıl kullanıldığına dair incelemeler yaptım.
