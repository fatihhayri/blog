Title: Genişlik ve Yüksekliğin Sınırlarını Belirlemek(min-width, min-height,max-width, max-height)
Slug: genislik-ve-yuksekligin-sinirlarini-belirlemekmin-width-min-heightmax-width-max-height
Date: 2006-10-09 11:21
Category: CSS, Javascript, Web Standartları, XHTML
Tags: CSS, css2, expression, ie-fix, Javascript, maksimum, max-height, max-width, min-height, min-width, Web Standartları, XHTML

Bir kapsayıcı kutunun genişlik değerini minimum ve maksimum değerleri
ile sınarlandırabilriz. Bu özellikler CSS2 ile birlikte gelmiştir.
<!--more-->

#### min-width, min-height

**Yapısı :** min-width, min-height: <deger>  
**Aldığı Değerler :** [<uzunluk değeri >][] | [<yüzde>][<uzunluk değeri >] | inherit  
**Başlnagıç değeri:** 0   
**Uygulanabilen elementler:** inline nonreplacement elementler ve tablo
elementlere  
**Kalıtsallık:** Yok

min-width, min-height kapsayıcı kutunun minimum alacağı değerleri
belirtmek için kullanırız.

	:::css
	 p.menu { float:left; width:200px;
min-width:150px; } 

<div class="tarayiciuyum">
**Web Tarayıcı Uyumu:**

</p>
<p>
Internet Explorer 7+  
Netscape 6+  
Opera 6+  
W3C’s <acronym title="Stil şablonu">CSS</acronym> Level 2+  
<acronym title="Stil şablonu">CSS</acronym> Profile 2.0

</div>
 

Aynı şekilde max-width ve max-height tanımlamalarıda yapılır.

#### max-width, max-height

**Yapısı :** max-width, max-height: <deger>  
**Aldığı Değerler :** [<uzunluk değeri >][] | [<yüzde>][<uzunluk değeri >] | none | inherit  
**Başlnagıç değeri:** 0   
**Uygulanabilen elementler:** inline nonreplacement elementler ve tablo
elementlere  
**Kalıtsallık:** Yok

max-width, max-height kapsayıcı kutunun maksimum alacağı değerleri
belirtmek için kullanırız.

	:::css
	 p.menu { float:left; width:200px;
max-width:400px; }

<div class="tarayiciuyum">
**Web Tarayıcı Uyumu:**

</p>
<p>
Internet Explorer 7+  
Netscape 6+  
Opera 5+  
W3C’s <acronym title="Stil şablonu">CSS</acronym> Level 2+  
<acronym title="Stil şablonu">CSS</acronym> Profile 2.0

</div>
 

şžöyle bir sonumuz vardır ki oda IE'nin 7 versiyonundan sonra bu
özellikleri desteklemeye başlamasdır. Bu çok kullanışlı özellikleri bu
nedenden dolayı kullanmamazlık yapmayacağız tabi.

IE için bir çözüm vardır. **expression()** özelliği bu özellik sadece IE
tarafından yorumlanır. Bu özellik dinamik özellik olarak tanımlanır.
Yani bu kod normalde bir javascript kodudur.

	:::css
	 #icerik { min-width: 600px; max-width:
1200px; width:expression(document.body.clientWidth < 600? "600px" :
document.body.clientWidth > 1200? "1200px" : "auto"); }

<div id="icerik">
....

</div>


Yukarıdaki tanımlamda css içerisinde javascript komutları
kullanılmıştır. Bu tanımlamaları sadece IE anlayacaktır ve
uygulayacaktır. Kodda eğer genişlik belirtilen maksimum değerden büyükse
atanan değeri alacak değilse auto değeri alacaktır.

Ayrıca min-height için daha kısa bir çözüm vardır

	:::css
	 #menu { min-height:500px; height:auto
!important; height:500px; } 

</p>

  [<uzunluk değeri >]: http://www.fatihhayrioglu.com/?p=95
