Title: CSS ile Menü Yapmak I - Dikey Menüler
Date: 2006-11-05 20:50
Category: CSS, Web Standartları, XHTML
Tags: CSS, liste, menü, ul, Web Standartları, XHTML

Web sitelerinin vazgeçilmez öğelerinde biridir menüler. Menüler
kullanıcının oluşturduğumuz sayfalara hızlı erişimini sağlar. Bir çok
site de Ürünler, İletişim, Hakkımızda vb. bölümlerini menü öğesi olarak
görürüz. Bu makalede sırasız listeler(<ul>)ve CSS yardımı ile menü
yapımını anlatacağız. CSS ile yapılan menüler esnek, kolay
düzenlenebilir, güzel görünen ve rollover efekti uygulana bilen
menülerdir. <!--more-->

Sırasız listeler(<ul>) ilk olarak listeleme işlemleri için kullanılsa
da CSS'in yükselişi ile birlikte menü oluşturmak için kullanılmaya
başlandı. Aslında menülerde bir bakıma link listeleri olduğu düşünülürse
işlevinin dışında kullanılmadığı da doğru bir tespittir. Kodumuzu
yazmaya başlayalım:

[sourcecode language='html']

-   [Ana Sayfa][]
-   [Hakkımızda][]
-   [Ürünler][]



Kodlama sonucu görüntü aşağıdaki gibi olacaktır.

<div align="center">
![][]

</div>
Her linkin başındaki imgeleri kaldırmak için:

[sourcecode language='css'] ul.menu { list-style-type: none; }


<div align="center">
![][1]

</div>
Bir çok web tarayıcısı sırasız listeleri(<ul>) yorumlarken yukarıda
görüldüğü gibi otomatik olarak soldan bir padding/margin(bazı
tarayıcılarda padding uygularken bazılarında margin uygular) mesafesi
uygular bu mesafeyi sıfırlamak için:

[sourcecode language='css'] ul.menu { list-style-type: none; padding: 0;
margin: 0; } 

![][2]

Bu bölüme kadar yazılan kodlamalar hem dikey menüler hem de yatay
menüler içinde aynıdır. Ancak bundan sonra dikey menü ve yatay menü için
kodlar değişecektir.

###### Dikey Menüler

Dikey menülerde linkler yukarıdan aşağı doğru sıralanmıştır. Link
elementi(a) inline-elementtir, her linke rollover özelliği kazandırmak
için:

[sourcecode language='css'] ul.menu a { display: block; } 

Biraz görselliği arttırırsak:

[sourcecode language='css'] ul.menu a { display: block; color: #1B1B1B;
background-color: #E2E2E2; } 

![][3]

Linkler web tarayıcısının genişliği kadar uzayacaktır, kendi istediğimiz
genişliğe sahip olmak için:

[sourcecode language='css'] ul.menu a { display: block; color: #1B1B1B;
background-color: #E2E2E2; width:8em; } 

![][4]

Linkler arasına biraz boşluk verelim:

[sourcecode language='css'] ul.menu a { display: block; color: #1B1B1B;
background-color: #E2E2E2; width:8em; padding: .2em .8em; }


![][5]

Linklerin altındaki çizgileri kaldıralım:

[sourcecode language='css'] ul.menu a { display: block; color: #1B1B1B;
background-color: #E2E2E2; width:8em; padding: .2em .8em;
text-decoration: none; } 

![][6]

şžimdi linklerimize rollover efekti vermek için a:hover kullanacağız:

[sourcecode language='css'] ul.menu a:hover { background-color: #999; }


![][7]

son olarak linklerin arasını ayıralım:

[sourcecode language='css'] ul.menu li { margin: 0 0 .2em 0; }
 İşte menümüzün son hali
<iframe src="/static/dokumanlar/menu.htm" width="250" height="200" frameborder="0" scroll="auto"></iframe>

</p>

  [Ana Sayfa]: index.html
  [Hakkımızda]: hakkimizda.html
  [Ürünler]: urunler.html
  []: /static/dokumanlar/menu1.gif
  [1]: /static/dokumanlar/menu2.gif
  [2]: /static/dokumanlar/menu3.gif
  [3]: /static/dokumanlar/menu4.gif
  [4]: /static/dokumanlar/menu5.gif
  [5]: /static/dokumanlar/menu6.gif
  [6]: /static/dokumanlar/menu7.gif
  [7]: /static/dokumanlar/menu8.gif
