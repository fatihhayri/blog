Title: CSS3 :target seçicisi
Date: 2011-05-03 20:34
Category: CSS
Tags: :target seçicisi, css3, hedef seçme

:target seçicisi CSS3 ile birlikte gelen yeni seçilerden biri. :target
seçicisi doküman içi linklere odaklanmamızı sağlıyor. Daha önce bu işi
yapmak için javascript ile yapıyorduk. CSS3’ün bizlere kazandırdığı
birçok yenilikte olduğu gibi bu özellikte basit bir şekilde
sayfalarımıza güzel etkiler kazandırır. :target sözde sınıfı :hover
seçicisi gibi dinamik bir seçicidir.

[css] h3:target { background-color: \#ff0 } [/css]

<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 9+ ;  
Firefox 1+ ;  
Safari 3.1+ ;  
Opera 9.5+;  
Chrome 2+

</div>
Sayfa içi bağlantıları nasıl yaptığımı hatırlayalım.

[html] \<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"\> \<html
xmlns="http://www.w3.org/1999/xhtml"\> \<head\> \<meta
http-equiv="Content-Type" content="text/html; charset=utf-8" /\>
\<title\>Hedef Trabzon\</title\> \<style\> body { width:550px; margin:0
auto; font:14px/1.5em Arial, Helvetica, sans-serif; border-color:\#C03;
border-style:solid; border-width:20px 5px 50px 5px; padding:20px } div {
border:1px solid \#06F; margin-bottom:15px; padding:10px;
border-radius:15px; -moz-border-radius:15px; -webkit-border-radius:15px;
} div:target { -moz-box-shadow: 0 0 10px \#9c9c9c; -webkit-box-shadow: 0
0 10px \#9c9c9c; box-shadow: 0 0 10px \#9c9c9c;
background-color:\#D5E3FD; border-width:2px } \</style\> \</head\>
\<body id="tepe"\> \<h1\>Trabzon\</h1\> \<p\>\<a
href="\#b1"\>Coğrafya\</a\> | \<a href="\#b2"\>Nüfus\</a\> | \<a
href="\#b3"\>Tarihçe\</a\> | \<a href="\#b4"\>Toplum ve
Kültür\</a\>\</p\> \<p\>Trabzon, Karadeniz Bölgesi'nin Doğu Karadeniz
bölümünde yer alan merkezii bir şehirdir....\</p\> \<div id="b1"\>
\<h3\>Coğrafya\</h3\> \<p\>Dar bir sahil şeridinin ardında denize dikey
uzanan dağlık bir araziye sahip olan ilin merkezi Boztepe (antik
Minthrion tepesi) üzerine kurulmuştur. İl topraklarının % 22,4 yayla, %
77,6 si ise tepelerden oluşmaktadır. \<strong\>Dereler\</strong\>
Değirmendere (Piksidis), Yanbolu, Fol, Ağasar, İskefiye, Kalenima,
Karadere (Araklı), Küçükdere, Koha, Sürmene (Manahos), Solaklı, Baltacı
deresi, Sera Deresi...\</p\> \<p\>\<a href="\#tepe"\>yukarı\</a\>\</p\>
\</div\> \<div id="b2"\> \<h3\>Nüfus\</h3\> \<p\>Toplam nüfusu
765.127'dur. Bu nüfusun yaklaşık %54'ü şehir ve ilçe gibi
merkezlerde,%46'sı ise kırsal kesimlerde yani köylerde
yaşamaktadır.\</p\> \<p\>\<a href="\#tepe"\>yukarı\</a\>\</p\> \</div\>
\<div id="b3"\> \<h3\>Tarihçe\</h3\> \<p\> Eusebius'a göre şehrin
kuruluş tarihini MÖ 756 olmakla birlikte bu iddia Trabzon'u İstanbul,
Roma hatta, genel kanıya göre Trabzon ve diğer Doğu Karadeniz
kolonizasyonunu gerçekleştiren Sinop'tan daha eski bir kent
yapmaktadır...\</p\> \<p\>\<a href="\#tepe"\>yukarı\</a\>\</p\> \</div\>
\<div id="b4"\> \<h3\>Toplum ve Kültür\</h3\>
\<p\>\<strong\>Halk\</strong\> Trabzon halkı adet , yaşam tarzı ,
gelenek ve görenek bakımından kendine ve yöreye özgü özellikler
taşımaktadır...\</p\> \<p\>\<a href="\#tepe"\>yukarı\</a\>\</p\>
\</div\> \</body\> \</html\> [/html]

Örneği görmek için [tıklayınız.][]

![][]

Benzer yapının yatay kaydırma çubuğu ile olanını yapabiliriz

![][1]

Örneği görmek için [tıklayınız.][2]

Sayfa içi linklerden farklı olarak **name** ile değil **id** ile
tanımlanan alanları hedef seçiyoruz. Buda bizi fazla kod yazmaktan
kurtarıyor.

Aşağıda bu özellik kullanılarak yapılmış bir iki güzel örneğe link
verdim.

### Örnek1: Dipnot

Bu özellik wikipedia tarafında dipnoların takibi için çok güzel bir
şekilde
kullanılmaktadır.[http://tr.wikipedia.org/wiki/Trabzon\_%28il%29][]
mesela Trabzon ili hakkında bilgiyi okurken herhangi bir dipnot linkine
tıkladığımızda ilgili dipnot ardalan rengi değiştirilerek
belirginleştirilmiştir.

![][3]  

[css] ol.references &gt; li:target { background-color:\#def; } [/css]

Bunun dışında eğlenceli örnekler geliştirilmiştir.

### Örnek 2: Basit Akordiyon

[http://kaioa.com/b/0903/target\_faq\_demo.html][]

![][4]

[css] \#faq\>li:target\>div{ display:block; } [/css]

örnekte gizle-göster ile basit bir akordeon içerik yapısı
oluşturulabilir.

### Örnek3: Galeri

[http://kaioa.com/b/0903/target\_gallery\_demo.html\#i1][]

![][5]

[css] dt:target+dd{ display:block; } dt:target img{ cursor:default;
border-bottom:5px solid \#000; border-top:5px solid \#000;
margin-top:401px; } [/css]

Örneğinde ise basit bir galeri yapısı kurulabilir.

Zamanla çok daha güzel örneklerin çıkacağını düşünüyorum.

### Kaynaklar

-   [http://dev.opera.com/articles/view/css3-target-based-interfaces/][]
-   [http://thinkvitamin.com/design/stay-on-target/][]
-   [http://www.smashingmagazine.com/2011/03/30/how-to-use-css3-pseudo-classes/][]
-   [http://www.red-team-design.com/get-to-know-your-css3-target-pseudo-class][]
-   [http://www.css3.info/making-an-image-gallery-with-target/][]
-   [http://virtuelvis.com/gallery/css3/target/interface.html\#recycle][]
-   [http://webdesignernotebook.com/css/the-css3-target-pseudo-class-and-css-animations/][]
-   [http://kaioa.com/node/93][]
-   [http://reference.sitepoint.com/css/pseudoclass-target][]

</p>

  [tıklayınız.]: http://www.fatihhayrioglu.com/dokumanlar/target_sozde_sinifi/target_sozde_sinif.html
  []: https://lh6.googleusercontent.com/_cLb1J3SgGfIwlvlO8Dl0X-p4BJVhIEGpvnTDdfhcwVqz1kOSXWgvYq2qZkKg_5nD2gLoutyeF2qeg8xyhmIRuQK0mophK76F3yxAcSrXTY4kL8IEw
  [1]: https://lh4.googleusercontent.com/rREDSpEu15zUN-f6f1Wd8ua6LgWmX9YatGoULf1kmIJQ9LapqA-HWwnvyLESxxzICXQ3Y-HMm5TwL2kAce28fa1_pnOU--hFX8Ay4VFSET_NePdfJQ
  [2]: http://www.fatihhayrioglu.com/dokumanlar/target_sozde_sinifi/target_sozde_sinif_yatay.html
  [http://tr.wikipedia.org/wiki/Trabzon\_%28il%29]: http://tr.wikipedia.org/wiki/Trabzon_%28il%29
  [3]: https://lh6.googleusercontent.com/0G2gsPGXTQ2SDAqEYXAMsVPpCRvSyTzkoR_Ubb-P2eq3zdhBo4ARPTD06UnDknSB3U2XEPJ443-fcloiH22zHNodmCLgBui2jGpJQZDJiw95lZWlpQ
  [http://kaioa.com/b/0903/target\_faq\_demo.html]: http://kaioa.com/b/0903/target_faq_demo.html
  [4]: https://lh6.googleusercontent.com/WxInkt_K1Za-AOK1mwFR6QdopkG_Jclf-0V7rM3rcGQI6BHXmerN7GNbKQOMN8UudczO0029sdlSjgc7UYXBpgye2ISmIWMgx9z5ERDMEp9mbMYIxw
  [http://kaioa.com/b/0903/target\_gallery\_demo.html\#i1]: http://kaioa.com/b/0903/target_gallery_demo.html#i1
  [5]: https://lh5.googleusercontent.com/JIw7mpQZ1vZlRkcjZijKVbCoe5SqXeq4TGx0pNrW0qSVOhmS3u-7xQacBlvxzWBf55OWlzYxf2B7k0u89CHVa2fFdlTL4F410blisNOAz9eF2LjNlw
  [http://dev.opera.com/articles/view/css3-target-based-interfaces/]: http://dev.opera.com/articles/view/css3-target-based-interfaces/
  [http://thinkvitamin.com/design/stay-on-target/]: http://thinkvitamin.com/design/stay-on-target/
  [http://www.smashingmagazine.com/2011/03/30/how-to-use-css3-pseudo-classes/]:
    http://www.smashingmagazine.com/2011/03/30/how-to-use-css3-pseudo-classes/
  [http://www.red-team-design.com/get-to-know-your-css3-target-pseudo-class]:
    http://www.red-team-design.com/get-to-know-your-css3-target-pseudo-class
  [http://www.css3.info/making-an-image-gallery-with-target/]: http://www.css3.info/making-an-image-gallery-with-target/
  [http://virtuelvis.com/gallery/css3/target/interface.html\#recycle]: http://virtuelvis.com/gallery/css3/target/interface.html#recycle
  [http://webdesignernotebook.com/css/the-css3-target-pseudo-class-and-css-animations/]:
    http://webdesignernotebook.com/css/the-css3-target-pseudo-class-and-css-animations/
  [http://kaioa.com/node/93]: http://kaioa.com/node/93
  [http://reference.sitepoint.com/css/pseudoclass-target]: http://reference.sitepoint.com/css/pseudoclass-target
