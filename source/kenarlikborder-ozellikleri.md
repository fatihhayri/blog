Title: CSS Kutu Modeli - Kenarlık(border) Özellikleri
Date: 2006-07-31 22:56
Category: CSS
Tags: Border, border-bottom, border-left, border-right, border-top, CSS, kenarlık

Kenarlık(border), içerik alanı ve padding etrafındaki bir veya daha
fazla çizgiye denir.<!--more-->

![Kutu Modeli][]

-   boder-style
-   border-top-style, border-right-style, border-bottom-style,
    border-left-style
-   border-width
-   border-top-width, border-right-width, border-bottom-width,
    border-left-width
-   border-color
-   border-top-color, border-right-color, border-bottom-color,
    border-left-color
-   border

Sırasıyla incelersek:

### border-style

<div class="cssozelliktanimi">
**Yapısı :** border-style: <deger>  
**Aldığı Değerler :** [ none | hidden | dotted | dashed | solid | double | groove | ridge | inset | outset ]{1,4} | inherit  
**Başlnagıç değeri:**tanımlama yok   
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

</div>
**border-style** özelliği kenarlık stilini belirlememizi sağlar.(Örn:
dotted(noktalı), double(çift) vd.) 10 farklı değeri CSS
desteklemektedir. Bu özellik kenarlığın görünmesi için tanımlanması
gereklidir. Bir veya dört değer alabilir eğer dört değer alırsa
sırasıyla üst, sağ, alt ve sol kenarlık stilini belirler. Eğer tek
değeri varsa tüm kenarlık değeri ataması yapılmış demektir. Eğer iki
veya üç değer ataması yapılmış ise [margin][]'de gördüğümüz sıralama söz
konusudur.

	:::css
	 p.yeni { border-style: solid; }


<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+   
Netscape 4+   
Opera 3.6+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
### border-top-style, border-right-style, border-bottom-style, border-left-style

<div class="cssozelliktanimi">
**Yapısı :** border-[top,left,right,bottom]-style: <deger>  
**Aldığı Değerler :** none | hidden | dotted | dashed | solid | double
| groove | ridge | inset | outset | inherit  
**Başlangıç değeri:** tanımlama yok   
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

</div>
**border-top-style, border-right-style, border-bottom-style,
border-left-style** border-style özelliğinin her kenara ayrı ayrı
atamasını yapabilmek için kullanılır.

	:::css
	 h1{ border-style: solid; border-left-style:
none; } 

<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+(kısmen),6+ (tam)  
Netscape 4+(kısmen), 6+ (tam)  
Opera 3.6+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
### border-width

<div class="cssozelliktanimi">
**Yapısı :** border-width: <deger>  
**Aldığı Değerler :** [ thin | medium | thick | <[uzunluk değeri][]> ]{1,4} | inherit  
**Başlnagıç değeri:** tanımlama yok  
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

</div>
İlk olarak stili belirledikten sonra kenarlık kalınlığını belirlemek
için **border-width** değeri kullanılır.

<p>
**border-width** yüzde değeri alamaz. 	:::css
	 p {
margin: 5px; background-color: silver; border-style: solid;
border-width: 1px; }

</ol>


<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+   
Netscape (kısmen), 6+(tam)   
Opera 3.6+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
### border-top-width, border-right-width, border-bottom-width, border-left-width

<div class="cssozelliktanimi">
**Yapısı :** border-[top,left,right,bottom]-width: <deger>  
**Aldığı Değerler :** thin | medium | thick | <[uzunluk değeri][] > |
inherit  
**Başlnagıç değeri:** tanımlama yok  
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

</div>
**border-top-width, border-right-width, border-bottom-width,
border-left-width** border-width özelliğinin her kenara ayrı ayrı
atamasını yapabilmek için kullanılır.

	:::css
	 h2 { border-left-width: medium;
border-style: solid; } 

<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+ (kısmen), 6+(tam)   
Netscape 4+(kısmen), 6+ (tam)  
Opera 3.6, 4+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
### border-color

<div class="cssozelliktanimi">
**Yapısı :** border-color: <deger>  
**Aldığı Değerler :** [ <[renk][uzunluk değeri]> | transparent ]{1,4}
| inherit  
**Başlnagıç değeri:** tanımlama yok  
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

</div>
**border-color** özelliği kenarlık rengini belirler. (X)html'deki
**bordercolor** ile benzerdir.

	:::css
	 p { border-style: solid; border-color: gray;
} 

Tek değer tüm kenarlık renklerini belirler, her kenar için ayrı renk
tanımlamasıda yapılabilir.

<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+  
Netscape 4+(kısmen), 6+(tam)  
Opera 3.6+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
### border-top-color, border-right-color, border-bottom-color, border-left-color

<div class="cssozelliktanimi">
**Yapısı :** border-[top,left,right,bottom]-color: <deger>  
**Aldığı Değerler :** [ <[renk][uzunluk değeri]> | transparent ]{1,4}
| inherit  
**Başlnagıç değeri:** tanımlama yok  
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

</div>
**border-color**özelliğinin her kenara ayrı ayrı atamasını yapabilmek
için kullanılır.

**Not:** Bir kenarlığı yok etmek için kalınlık değeri veririz. Birde
CSS2 ile birlikte gelen transparent özelliği vardır ki bu kenarlığı yok
etmez sadece görünmez yapar.

	:::css
	 p { border-style: solid; border-color: gray;
} 

Tek değer tüm kenarlık renklerini belirler, her kenar için ayrı renk
tanımlamasıda yapılabilir.

<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+  
Netscape 4+(kısmen), 6+(tam)  
Opera 3.6+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
### border

**Yapısı :** border: <[deger][uzunluk değeri]>  
**Aldığı Değerler :** <border-width> | <border-style> |
<[renk][uzunluk değeri]>   
**Başlnagıç değeri:** tanımlama yok  
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

**border**yukarıda sıraladığımız özellikleri tek sefer de tanımlamak
için kullanılır. Bir [kısaltmadır][].

	:::css
	 h1 { border: thick silver solid; }


Bu özellikleri tek tek atamak isteseydik şöyle bir kod yazmamız
gerekecekti.

	:::css
	 h1 { border-top: thick silver solid;
border-bottom: thick silver solid; border-right: thick silver solid;
border-left: thick silver solid; }

<div class="tarayiciuyum">
**Browser Uyumu:**  
Internet Explorer 4+  
Netscape 4+(kısmen), 6+(tam)  
Opera 3.6+  
W3C's CSS Level 1+  
CSS Profile 1.0

</div>
</p>

  [Kutu Modeli]: http://fatihhayrioglu.com/images/basit_boxmodel.gif
  [margin]: http://www.fatihhayrioglu.com/?p=6#more-6
  [uzunluk değeri]: http://www.fatihhayrioglu.com/?p=95
  [kısaltmadır]: http://www.fatihhayrioglu.com/?p=6
