Title: Git Öğreniyorum -2
Date: 2011-09-07 21:40
Category: Haberler
Tags: git, macos, sürüm kontrol sistemi, terminal

Daha önce [Sürüm Kontrol Sistemi Git][] adlı bir makale yazmıştım,
öğrenme sürecim devam ediyor. Git kullanırken komut satırını
kullanıyoruz. MacOs’da Terminal’e denk geliyor. Bu nedenle genel
Terminal komutlarınıda bilmekte yarar var. Benim gibi mac terminaline
yabancı biri iseniz(aslında linux komut satırı ile benzer kodlar)
aşağıdaki basit komutları bilmenizde yarar var.

[![][]][]

Terminal giriş görünümü yukarıdaki gibidir. (Renklere takılmayın bu
benim seçimim)

### ls (list files)

Çalıştığımız klasörün içeriğini göstermek için kullanılır. Windows’taki
dir ile aynı anlamdadır.

Sonuç aşağıdaki gibi olacaktır

[bash] ls aFolder    another.txt    bilgilendirme.txt   deneme.html
[/bash]

### cd (Change Directory)

Bu komut ile dosyalar arası geçiş için kullanırız. Mesela image
klasörüne geçmek için

[bash] cd images [/bash]

Tek seviyede değil birden fazla seviyede geçişte yapabiliriz.

[bash] cd images/icons/ust [/bash]

Bir alt klasöre inmek için

[bash] cd .. [/bash]

Kök dizinine(root) inmek için ise

[bash] cd [/bash]

yazmak yeterlidir. Ufak bir ipucu klasör isimlerinin uzun olması
durumunda akılda tutmak zor oluyor. Klasör veya dosya isminin başında
bir kaç karakter yazdıktan sonra tab tuşuna basarak gerisini
tamamlayabilirsiniz.

### mkdir (Make Directory)

Yeni klasör oluşturmak için kullanıyoruz. Mac ve Windows’ta kullanımı
aynıdır.

[bash] mkdir yeniKlasor [/bash]

### rm (remove)

Dosya ve klasörleri silmek için kullanılır. Silme işlemlerinde her zaman
dikkatli olmak lazım.

[bash] rm deneme.html rm images_klasoru [/bash]

### cp (copy) ve mv (move)

Çok basit bir kullanımı vardır. İlk parametre kopyalanacak dosyayı
ikinci parametre ise hedefi gösterir.

[bash] cp deneme.html ~/dosya/deneme.html [/bash]

Eğer taşımak istiyorsanız, aynı şekilde kullanabiliriz.

[bash] mv deneme.html /dosya/deneme.html [/bash]

mv komutu dosya ismini değiştirmek içinde kullanılabilir.

[bash] mv deneme.html /dosya/test.html [/bash]

deneme.html dosyası ismi test.html olarak değiştirilip taşınmıştır.

### clear

Terminal ekranını temizlemek için kullanılır.

### Dosya Açmak

Komut satırlarından harici programlarda da açabiliyoruz veya kendi
içinde açabiliyoruz.

Mesela MacOs için ilgili klasörde iken

[bash] nano deneme.html [/bash]

komutu deneme.html dosyamızı nano editöründe açmamızı sağlayacaktır.

### exit

Eğer uzak dosya yönetimi ile çalışıyorsanız. Kurduğunuz bağlantıyı
sonlandırır.  exit komutu ile Terminalide kapatmak mümkün. Terminal -
Preferences.. - Settings - Shell oradanda “Close the Window”
işaretleyerek exit komutu ile hem bağlantıyı hemde pencereyi
kapatabiliriz.

Benim ihtiyaç duyduğum komutlar bunlar tüm liste için
[http://ss64.com/osx/][] sitesineden yardım alabilirsiniz.

Git Kullanırken Öğrendiğim İpuçları
-----------------------------------

Yukarıda genel komutları anlattım, aşağıda ise kullandıkça gördüğüm
komutları ve ipuçlarını paylaşacağım.

### İki dosya arasındaki farkı görmek

Bir branchdeki veya bir dosya üzerindeki değişiklikleri görmek için
branchde iken

[php] $git log [/php]

yazarız bu komut bize

[php] commit f491239170cb1463c7c3cd970862d6de636ba787 Author: Matt
McCutchen &lt;matt@mattmccutchen.net&gt; Date:   Thu Aug 14 13:37:41
2008 -0400 git format-patch documentation: clarify what --cover-letter
does commit 7950659dc9ef7f2b50b18010622299c508bfdfc3 Author: Eric Raible
&lt;raible@gmail.com&gt; Date:   Thu Aug 14 10:12:54 2008 -0700 bash
completion: 'git apply' should use 'fix' not 'strip' Bring completion up
to date with the man page. [/php]

gibi bir sonuç döndürür. O dosya veya o branch üzerinde yapılan tüm
değişiklikler hakkında bilgileri içeren bir listedir bu. Bu listede
commit … ile başlayan satırda verilen numara yapılan ve gönderilen her
iş için farklıdır biz bu sözdizimini kullanarak iki farklı gönderi
arasındaki farkı bulabiliriz.

[php] $git diff f491239170cb1463c7c3cd970862d6de636ba787
7950659dc9ef7f2b50b18010622299c508bfdfc3  Html/index.html [/php]

İki farklı branchdeki HTML/index.html dosyasındaki farklılıkları
gösterir yukarıdaki kod. Farkları renkli görmek için --color
parametresini kullanabiliriz.

[php] $git diff --color  d76192b2c7a61d2aea62c7aec21e14cda72f9e32
fe0dba7b841e86b095d2aefbd6bd755a0d9d1e90  Html/index.html [/php]

Eklenenleri yeşil, çıkarılanları kırmızı renkte gösterecektir. Ayrımı
görmek için renkler güzel oluyor.

### Dallanma (Brach) Silmek

git branch -d: Yanlışlıkla açtığımız branchlerı silmek için

[php] $git branch -d branch_ismi [/php]

### Kısayol kullanmak

Git kullanırken aynı kodları tekrar tekrar çok kullanıyoruz. Bu
komutları kısaltarak daha hızlı kod yazabilme imkanı sağlıyor bize komut
sistemi.

git config dosyasına kısayolllarımızı ekleyebiliyoruz. git cofig ile
ilgili ayrıntılı bilgiyi
[http://tybarts.wordpress.com/2011/05/07/git-global-config-dosyasini-ayarlamak/][]
bağlantısından edinebilirsiniz.

Global congif dosyasına eklemek için

[php] $git config --global alias.ci commit [/php]

**ci** kısaltma **commit** normali. Eğer projeye özgü kısayollar
oluşturmak için

[php] $git config alias.ci commit [/php]

**--global** parametresini kaldırmamız yeterli olacaktır. git config
dosyasını görmek için

[php] $git config --edit [/php]

yazmamız yeterli burada eklediğimiz kısayolları görebiliriz. Benim
listem aşağıdaki gibi.  
  
[alias]  
st = status  
br = branch  
co = checkout  
ci = commit

Siz bu listeyi kendinize göre düzenleyebilirsiniz.

### Git için kaynaklar

[http://sixrevisions.com/resources/git-tutorials-beginners/][] bu
bağlantıda Git kaynakları listelenmiş. Git’in güzel yanlarında birisi
öğrenmek için kaynağın bol olması.

### Başka Branch’den dosya almak

[php] $git checkout branch_adi dosya_adi [/php]

Benzer bir şekilde branchde yaptığımız değişikliği geri almak için
master’dan dosyayı alabiliriz.

[php] git checkout master dosya_adi [/php]

### Değişen dosya isimleri

Çalıştığımız branchde değişiklik yaptığımız dosyaları görmek için

[php] $git diff master --name-only [/php]

kodunu kullanıyoruz.

Bana üşenmeyip bunları ve aklımda kalmayan bir çok bilgiyi öğreten Onur
Yerlikaya'ya şükranlarımı sunarım. Gitmeyeydin Git daha kolay olacaadı.
:D

Kalın sağlıcakla

### Kaynaklar

-   [http://tybarts.wordpress.com/2011/05/07/git-global-config-dosyasini-ayarlamak/][]
-   [https://git.wiki.kernel.org/index.php/Aliases][]
-   [http://sixrevisions.com/resources/git-tutorials-beginners/][]
-   [http://ss64.com/osx/][]

</p>

  [Sürüm Kontrol Sistemi Git]: http://www.fatihhayrioglu.com/surum-kontrol-sistemi-git/
  []: http://www.fatihhayrioglu.com/wp-content/terminal-300x187.png
    "terminal"
  [![][]]: http://www.fatihhayrioglu.com/wp-content/terminal.png
  [http://ss64.com/osx/]: http://ss64.com/osx/
  [http://tybarts.wordpress.com/2011/05/07/git-global-config-dosyasini-ayarlamak/]: http://tybarts.wordpress.com/2011/05/07/git-global-config-dosyasini-ayarlamak/
  [http://sixrevisions.com/resources/git-tutorials-beginners/]: http://sixrevisions.com/resources/git-tutorials-beginners/
  [https://git.wiki.kernel.org/index.php/Aliases]: https://git.wiki.kernel.org/index.php/Aliases
