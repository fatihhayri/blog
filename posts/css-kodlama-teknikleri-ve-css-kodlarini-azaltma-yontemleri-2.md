Title: CSS Kodlama Teknikleri ve CSS Kodlarını Azaltma Yöntemleri - 2
Date: 2010-03-27 19:07
Category: CSS, Web Standartları, XHTML
Tags: bildirim alanları, css-menü, Kod Azaltma, Torun-Seçicisi

Her projeye başladığımızda belli bir bilgi birikimi ile başlarız. Ancak
her seferinde yazdığımız kodun en iyi ve optimum kod olduğunu
sorgulamamız gerekiyor(çok acil olmadığı sürece). Acaba bu işi daha az
kodla ve daha esnek nasıl yaparım düşüncesi ile davranmalıyız. Bu belki
kodlama zamanımızı uzatır ama sonuçta içimize sinen bir iş yapmış
oluyoruz ve daha sonraki projelerimizde bu bilgi bize tecrübe ve hız
kazandıracaktır. Her zaman en iyiyi aramak iyidir.

Daha önce [CSS Kodlama Teknikleri ve CSS Kodlarını Azaltma Yöntemleri][]
bahsetmiştim genel olarak buna bir ek daha yapacağım. Aslında o
makaledeki 1. maddeyi biraz daha genişleteceğim. Mesela bir eleman
altındaki tüm elemanlara uygulanan bir özellik tek tek uygulanacağına
genel uygulanır alttaki elemanlara ise kendine has özellikler
tanımlanarak daha optimum kodlar elde edilir. Yer kazanılır,
tekrarlardan kurtulmuş oluruz ve daha kolay müdahale imkanımız
olur.<!--more-->

Genelde bu tip ortak kullanım ile menülerde karşılaşıyorum. Resimli
menülerde

[sourcecode language="html"] <ul id="menu"> <li id="menu1"><a
href="">menü 1</a></li> <li id="menu2"><a href="">menü
2</a></li> <li id="menu3"><a href="">menü 3</a></li> <li
id="menu4"><a href="">menü 4</a<</li> <li id="menu5"><a
href="">menü 5</a></li> <li id="menu6"><a href="">menü
6</a></li> </ul> [/sourcecode]

Bu tip bir menümüz olsun ve menünün her elemanı için farklı tanımlarımız
olsun.

[sourcecode language="css"] li#menu1 a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 0 no-repeat;
text-indent:-9999px; } li#menu2 a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 -25px no-repeat;
text-indent:-9999px; } li#menu3 a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 -50px no-repeat;
text-indent:-9999px; } li#menu4 a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 -75px no-repeat;
text-indent:-9999px; } li#menu5 a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 -100px no-repeat;
text-indent:-9999px; } li#menu6 a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 -125px no-repeat;
text-indent:-9999px; } [/sourcecode]

Görüldüğü gibi bir resimli menü oluşturduk. Kod sorunsuz çalışır, ancak
bu kodu daha kısa yazabiliriz. Birbirini aynı tanımları genel bir
elemana atayıp, geriye sade o elemana ait özelliği bırakırsak kodumuz
daha az olacaktır. yukarıdaki örnekte bunu yapalım

[sourcecode language="css"] ul#menu li a{display:block; width:50px;
height:24px; background:(images/menu.png) 0 0 no-repeat;
text-indent:-9999px;} [/sourcecode]

Bu tanım ile tüm a elemanlarını etkileyecek bir kod yazdık. Daha sonrada
her elemana özel kodlarını tek tek tanımlayalım.

[sourcecode language="css"] li#menu1 a{ background-postion:0 0;}
li#menu2 a{background-postion:0 -25px; } li#menu3
a{background-postion:0 -50px;} li#menu4 a{background-postion:0 -75px;}
li#menu5 a{background-postion:0 -100px;} li#menu6
a{background-postion:0 -125px;} [/sourcecode]

Görüldüğü gibi kodumuz daha az oldu. Böylece kodu düzenlemek de
kolaylaştı. Yukarıdaki örnekte sadece background-position değerleri
değişti. Başka bir örnekte genişlik değeride değişebilir bu durumda da
her tanımda genişlik tanımı ekleyerek kodumuzu yazabiliriz. Benzer bir
yapıyı [Basit Resimli Menü Yapmak][] adlı makalemde anlatmıştım.
Örnekleri oradan inceleyebilirsiniz.

### Bilgilendirme Kutuları

Aynı mantığı site kodlarken farklı alanlarda da kullanabiliriz. Örneğin
sitemizde bilgi kutuları hazırladığımızı düşünelim.

Kullanıcıyı bilgilendirme amaçlı alanlarımız için "Bilgilendirme
Kutuları - #bilgilendirme", Hata durumunda kullanıcıyı bilgilendirmek
için "Hata Kutuları - #hata", Kullanıcıyı uyarmak içinde "Uyarı
Kutuları - #uyari" kutuları hazırlayalım.

[sourcecode language="html"] <div class="bilgilendirme">Bilgilendirme
metni</div> <div class="onay">Onay metni</div> <div
class="hata">Hata mesajı</div> <div class="uyari">Uyarı
mesajı</div> [/sourcecode]

Bu kutuların css kodlarını yazalım.

[sourcecode language="css"] div.bilgilendirme{display:block;
padding:15px 10px 15px 50px; background:#BDE5F8
url(images/bilgilendirme.png) 8px 8px no-repeat; color:#00529B;
border:1px solid #00529B; font:12px Arial, Tahoma, sans-serif;
margin:10px 0} div.onay{display:block; padding:15px 10px 15px 50px;
background:#DFF2BF url(images/bilgilendirme.png) 8px -92px no-repeat;
color:#4F8A10; border:1px solid #4F8A10; font:12px Arial, Tahoma,
sans-serif; margin:10px 0} div.hata{display:block; padding:15px 10px
15px 50px; background:#FFBABA url(images/bilgilendirme.png) 8px -292px
no-repeat; color:#D8000C; border:1px solid #D8000C; font:12px Arial,
Tahoma, sans-serif; margin:10px 0} div.uyari{display:block; padding:15px
10px 15px 50px; background:#FEEFB3 url(images/bilgilendirme.png) 8px
-195px no-repeat; color:#9F6000; border:1px solid #9F6000; font:12px
Arial, Tahoma, sans-serif; margin:10px 0} [/sourcecode]

Örneği görmek için [tıklayınız.][]

sonuç olarak her şey tamam, ancak kodumuzu daha da azaltabilirmiyiz?
Evet.

Bunun için her kutuya genel bir sınıf tanımlamamız gerekecek. Bu
bildirim kutularını içerik alanımız içinde olduğunu düşünerek

[sourcecode language="css"]#icerikAlani div[/sourcecode]

şeklindeki bir tanım bizim işimize yaramaz. Daha özel bir tanımlama
yapmamız için her bildirim kutusuna bir adet sınıf daha eklememiz
gerekecek.

[sourcecode language="html"] <div class="bildirim
bilgilendirme">Bilgilendirme metni</div> <div class="bildirim
onay">Bilgilendirme metni</div> <div class="bildirim hata">Hata
mesajı</div> <div class="bildirim uyari">Uyarı mesajı</div>
[/sourcecode]

Evet böylece bildirim kutuları katmalarını(div) diğer katmanlardan
ayırmış olduk. Buna göre css kodumuzu azaltalım.

[sourcecode language="css"] #icerikAlani div.bildirim{display:block;
padding:15px 10px 15px 50px; background:#BDE5F8
url(images/bilgilendirme.png) 8px 8px no-repeat; color:#00529B;
border:1px solid #00529B; font:12px Arial, Tahoma, sans-serif;
margin:10px 0} [/sourcecode]

Daha sonra her kutu için ayrı kendine özel kodlarını yazalım.

[sourcecode language="css"] #icerikAlani
div.bilgilendirme{background:#BDE5F8 url(images/bilgilendirme.png) 8px
8px no-repeat; color:#00529B; border:1px solid #00529B;} #icerikAlani
div.onay{background:#DFF2BF url(images/bilgilendirme.png) 8px -92px
no-repeat; color:#4F8A10; border:1px solid #4F8A10;} #icerikAlani
div.hata{background:#FFBABA url(images/bilgilendirme.png) 8px -292px
no-repeat; color:#D8000C; border:1px solid #D8000C;} #icerikAlani
div.uyari{background:#FEEFB3 url(images/bilgilendirme.png) 8px -195px
no-repeat; color:#9F6000; border:1px solid #9F6000;} [/sourcecode]

Örneği görmek için [tıklayınız.][1]

Burada şöyle bir kullanım şeklinide tercih edebiliriz. Katman(div)
yerine <blockquote> etiketini kullanarak daha uygun bir kodlama
yapabiliriz. Maksat en uygun kodu bulmak.

[sourcecode language="html"] <blockquote
class="bilgilendirme">Bilgilendirme metni</blockquote> <blockquote
class="onay">Onay mesajı</blockquote> <blockquote class="hata">Hata
mesajı</blockquote> <blockquote class="uyari">Uyarı
mesajı</blockquote> [/sourcecode]

CSS kodumuzda

[sourcecode language="css"] #icerikAlani blockquote{display:block;
padding:10px 10px 10px 25px; background:lightblue
(images/bilgilendirme.gif) 0 0 no-repeat; font:12px Arial, Tahoma,
sans-serif; margin:10px 0}
blockquote.bilgilendirme{background-color:lightblue; background-postion:
0 0; color:blue; border:1px solid blue;}
blockquote.onay{background-color:lightblue; background-postion: 0 0;
color:blue; border:1px solid blue;}
blockquote.hata{background-color:lightred; background-postion: 0 0;
color:red; border:1px solid red;}
blockquote.uyari{background-color:lightyellow; background-postion: 0 0;
color:black; border:1px solid yellow;} [/sourcecode]

Örneği görmek için [tıklayınız.][2]

Sonuç olarak en optimum kodu ettik.

Bu makaleyi yazmaktaki amacım bu ve benzeri yöntemleri projelerimizde en
uygun kodlama yöntemlerini uygulamamız gerektiğini göstermek içindir.
Yoksa yukarıdaki örnekleri bir çok makalemde anlatmıştım zaten.
Projemizin tüm bölümlerinde aynı mantıkla hareket etmemiz gerektiğini
düşünüyorum. Hoşçakalın.

### Kaynak

-   [http://www.jankoatwarpspeed.com/post/2008/05/22/CSS-Message-Boxes-for-different-message-types.aspx][]
    (bilgilendirme alanları için)

</p>

  [CSS Kodlama Teknikleri ve CSS Kodlarını Azaltma Yöntemleri]: http://www.fatihhayrioglu.com/css-kodlarini-temizlemeazaltma/
    "CSS Kodlama Teknikleri ve CSS Kodlarını Azaltma   Yöntemleri"
  [Basit Resimli Menü Yapmak]: http://www.fatihhayrioglu.com/basit-resimli-menu-yapmak/
    "Basit Resimli Menü Yapmak"
  [tıklayınız.]: http://www.fatihhayrioglu.com/dokumanlar/kodazaltma2/bilgilendirme_1.html
  [1]: http://www.fatihhayrioglu.com/dokumanlar/kodazaltma2/bilgilendirme_2.html
  [2]: http://www.fatihhayrioglu.com/dokumanlar/kodazaltma2/bilgilendirme_3.html
  [http://www.jankoatwarpspeed.com/post/2008/05/22/CSS-Message-Boxes-for-different-message-types.aspx]:
    http://www.jankoatwarpspeed.com/post/2008/05/22/CSS-Message-Boxes-for-different-message-types.aspx
    "http://www.jankoatwarpspeed.com/post/2008/05/22/CSS-Message-Boxes-for-different-message-types.aspx"
