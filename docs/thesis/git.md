# Versiyon Kontrol Sistemi Olarak Git

Günümüzün yazılım geliştirme süreçleri, birçok geliştiricinin aynı projede bir arada çalışmasını gerektirir. Bu nedenle, bir proje üzerinde birden fazla kişi çalıştığında, tüm değişiklikleri izlemek ve kontrol etmek önemli hale gelir. İşte tam burada sürüm kontrol sistemleri devreye girer. Bu yazıda, en sevilen sürüm kontrol sistemlerinden biri olan Git'i inceleyip ve neden bu kadar popüler olduğunu öğreneceğiz.

## Versiyon Kontrol Sistemleri

Versiyon kontrol sistemleri, projelerde yapılan değişiklikleri izlemek, paylaşmak ve yönetmek için kullanılan yazılımlardır. Merkezi ve dağıtık olmak üzere iki tür versiyon kontrol sistemi vardır. Merkezi versiyon kontrol sistemlerinde, tüm veriler merkezi bir sunucuda saklanırken, dağıtıgit k versityon kontrol sistemlerinde, her kullanıcının kendi kopyası vardır ve herhangi bir değişiklik yapılabilir.

## Git Nedir ve Tarihi

Git, 2005 yılında Linus Torvalds tarafından Linux çekirdeği geliştirme sürecinde kullanılmak üzere oluşturulmuş bir sürüm kontrol sistemi olarak ortaya çıkmıştır. Git'in ortaya çıkışı, çok sayıda Linux çekirdeği geliştiricisinin proje yönetimi için bir önceki sürüm kontrol sistemi olan BitKeeper'ı tercih etmesiyle başlamıştır. Andrew Tridgell, bir takım tersine-mühendislik yöntemleriyle BitKeeper protokolüne müdahalelerde bulunmuş, ancak BitKeeper'ın telif haklarını elinde bulunduran Larry McVoy, BitKeeper'ın ücretsiz kullanımını reddederek konuyu hukuki platforma taşıyınca BitKeeper'ın kullanımından vazgeçilmiş, böylece Git'in temelleri atılmıştır.

## Git'in Sürüm Kontrol Olarak Avantajları

Git, bir sürüm kontrol sistemi olarak birçok avantaja sahiptir. Bu avantajlar şunlardır:

- Kolay işbirliği ve kod paylaşımı
- Değişiklikleri izleme ve önceki sürümlere geri dönme yeteneği
- Paralel geliştirme için dallanma ve birleştirme yetenekleri
- Çevrimdışı çalışma için dağıtık mimari

### İşbirliği ve Ekip Çalışması

Git, geliştiricilerin kod tabanı üzerinde işbirliği yapmasını kolaylaştırır. Her geliştiricinin kendi kod tabanı kopyasının olması nedeniyle, farklı geliştiriciler aynı anda kodun farklı parçalarında çalışabilirler ve birbirleriyle etkileşime girmezler. Git, farklı geliştiriciler tarafından yapılan değişiklikleri gözden geçirme ve birleştirme araçları da sağlar.

### Dallanma (Branch) ve Birleştirme (Merge)

Git'in branch ve merge yetenekleri, kodun farklı sürümleri üzerinde aynı anda çalışmayı kolaylaştırır. Geliştiriciler, özellikler veya düzeltmeler üzerinde çalışmak için yeni branchler oluşturabilir ve bu değişiklikleri hazır olduklarında ana kod tabanına mergeleyebilirler.

### Kolay Değişiklik Takibi

Gitte her bir değişiklik, "commit" olarak adlandırılan bir işlemle takip edilir. Bu sayede, herhangi bir zamanda, bir önceki sürüme geri dönüp hataları düzeltmek veya daha önce yapılan bir değişikliği geri getirmek mümkündür.

## Temel Git Komutları

Git kullanmanın en temel yollarından biri, öncelikle bir Git deposu oluşturmaktır. Bunun için aşağıdaki komutu kullanabilirsiniz:

git init

Depoyu oluşturduktan sonra, Git'te birçok komut kullanılabilir. Bazı temel komutlar şunlardır:

Dosyaları ekleme: git add dosya adı  
Veya tüm dosyaları eklemek için git add -A
Değişiklikleri kaydetme: git commit -m "açıklama"
Depo durumunu kontrol etme: git status
Değişiklik geçmişini görüntüleme: git log
Değişikleri göndermek için uzak sunucu eklemek için: git remote add uzaksunucuismi uzaksunucuadresi
Değişikleri uzak git sunucusuna yollamak için: git push
