Title: CSS ile Basit Şekilde Fare Üzerine Gelince(Rollover) Resim Değişimi Yapmak
Date: 2008-11-10 10:48
Category: CSS, Web Standartları, XHTML
Tags: fare üzerine gelince, link, resim, rollover

Daha önce bu konuya [Resimli Menüler][] kısmında anlatmıştım, ama orada
yapı daha karışık olduğu için anlaşılması ve basit uygulamalara
uyarlanması konusunda sıkıntılar oluyordu. Bu işi daha basit bir örnek
yardımı ile yapıp daha anlaşılır yapmak için beraber bir örnek yapalım.

Tek resimde işi halletmemiz, resmin sayfa yüklenmesinden önce yüklenmesi
sebebiyle fare üzerine geldiğinde herhangi bir resim yükleme işlemini
beklemediğimiz için daha akıcı olduğu gibi avantajlarını olduğunu daha
önce anlatmıştık.

İlk olarak fare imlecinin üzerine geldiğinde değişecek resmin her iki
hali yanyana gelecek şekilde yan yana veya alt alta gelecek şekilde tek
resim olarak hazırlıyoruz(aradaki çizgiyi iki resim arasındaki ayrımı
göstermek için koydum, normal resimde bu olmayacak)

![anasayfaya dön][]

Xhtml kodumuzu yazalım

[sourcecode language='html'][Ana Sayfaya Dön][][/sourcecode]

CSS kodumuzu yazalım

[sourcecode language='css']a.anasayfayaDon { display: block; width:
80px; height: 80px; background: url(images/degisen\_resim.gif) 0 0
no-repeat; text-decoration: none; text-indent:-999px; }
a:hover.anasayfayaDon { background-position: -80px 0; }[/sourcecode]

Yöntemi daha önce anlattığımız gibi ardalan kaydırmaca yöntemidir.
Hazırladığımız ardalan resminin ilk olarak istediğimiz kısmını
gösteriyoruz. Fare imleci üzerine geldiğinde ise yatayda aynı eksende
bulunan başlangıçta görünmeyen resmi eksi konum vererek gösteriyoruz.

Örnek sayfayı görmek için [tıklayınız][]

</p>

  [Resimli Menüler]: http://www.fatihhayrioglu.com/css-ile-menu-olusturmak-v-resimli-menuler
    "Resimli Menüler"
  [anasayfaya dön]: /images/mak_degisen_resim.gif
  [Ana Sayfaya Dön]: anasayfa.htm
  [tıklayınız]: /dokumanlar/fare_degisen_resim.html
