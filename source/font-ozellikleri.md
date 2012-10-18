Title: Font Özellikleri
Date: 2006-08-01 23:12
Category: CSS
Tags: CSS, font, font-family, font-size, font-weight, line-height

Font özellikleri sayfalarımızdaki metinlerin font ailesini, kalınlık
ayarlarını,boyutunu, büyük-küçük harf olmasını ve stilini değiştirmemizi
sağlar. CSS fontlar üzerinde tam hakimolmamızı sağlar. <!--more-->

-   color
-   font-family
-   font-size
-   font-weight
-   font-style
-   font-variant
-   font

### color

<div class="cssozelliktanimi">
**Yapısı :** color: <deger> **Aldığı Değerler :**<[renk][]> |
inherit **Başlangıç değeri:**web tarayıcısı belirler **Uygulanabilen
elementler:** tüm elementler **Kalıtsallık:** Var

</div>
**color** metinlerimizin rengini tanımlamamız için kullanılır.

	:::css
	 p{ color:#f00; /* kırmızı renk kodu */ }


Renk kullanımına daha önce değinmiştik. Detay için [tıklayınız.][renk]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### font-family

<div class="cssozelliktanimi">
**Yapısı :** font-family : [[<font aile ismi > | <soysal aile ismi >],]* [<font aile ismi > | <soysal aile ismi >] | inherit **Aldığı
Değerler :**

<font aile ismi >- herhangi bir font ailesi ismi kullanılabilir.

<soysal aile ismi >

-   **serif** (*örn:* Times)
-   **sans-serif** (*örn:* Arial or Helvetica)
-   **cursive** (*örn:* Zapf-Chancery)
-   **fantasy** (*örn:* Western)
-   **monospace** (*örn:* Courier)

**Başlangıç değeri:**web tarayıcısı belirler **Uygulanabilen
elementler:** tüm elementler **Kalıtsallık:** Var

</div>
Metinlerin kullanılacağı font ailesini belirlemek için kullanılır.
Birden fazla fontailesi kullanılacaksa aralarına virgül (,) konur.
Genelde son font ailesiolarak soysal font ailesi yazılır. Örnek:

	:::css
	 p { font-family: Verdana, Arial, Helvetica,
sans-serif; } 

Eğer font ismi bir den fazla kelimeden olşuyorsa çift tırnak içine
alınır.Örn:

	:::css
	 h1 { font-family: Georgia, "Times New
Roman", serif; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### font-size

<div class="cssozelliktanimi">
**Yapısı :**font-size: <kesin değerler > | <göreceli değerler > |
<[uzunluk][renk]> | <[yüzde][renk]> **Aldığı Değerler :**

-   <kesin değerler >
    -   xx-small | x-small | small | medium | large | x-large | xx-large

-   <göreceli değerler >
    -   larger | smaller

-   [<uzunluk>][renk]
-   [<yüzde>][renk] (üst elementlere(ebveyn) bağlı olarak)

**Başlangıç değeri:**medium **Uygulanabilen elementler:** tüm elementler
**Kalıtsallık:** Var

</div>
CSS, Font boyutlandırmaya daha esnek tanımlama yapmamızı olanak sağladı.
Mesela 11px değeri HTML'de2 ve 3 değeri arasında bir değer denk geliyor
ve HTML font elementi ile birlikte kullanılamıyordu.CSS'de font boyutunu
belirlemek için bir çok birim kullanılır. Örn: px, em,pt, in, cm vd.
	:::css
	 td { font-size :12px; } td { font-size :
150%; } td { font-size : xx-small; } td { font-size : x-large; }


<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### font-weight

<div class="cssozelliktanimi">
**Yapısı :**font-weight: <değer> **Aldığı Değerler :**normal |
**bold** | **bolder** | lighter | 100 | 200 | 300 | 400 | 500 | **600**
| **700** | **800** | **900** **Başlangıç değeri:**normal
**Uygulanabilen elementler:** tüm elementler **Kalıtsallık:** Var

</div>
Fontun kalınlık incelik durumunu belirler.
**100(ince)-900(kalın)**arasında bir değer alabildiği gibi bold, bolder
ve normal değerlerini de alır.

	:::css
	 p{ font-weight: bolder; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### font-style

<div class="cssozelliktanimi">
**Yapısı :**font-style: <değer> **Aldığı Değerler :** normal | italic
| oblique | inherit **Başlangıç değeri:**normal **Uygulanabilen
elementler:** tüm elementler **Kalıtsallık:** Var

</div>
Fontun eğik(italiktik) olup olamamasını belirler.

	:::css
	 p { font-style: italic; } h4{ font-style:
oblique; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### font-variant

<div class="cssozelliktanimi">
**Yapısı :**font-variant: <değer> **Aldığı Değerler :**normal |
small-caps | inherit **Başlangıç değeri:**normal **Uygulanabilen
elementler:** tüm elementler **Kalıtsallık:** Var

</div>
Metnin küçü-büyük harf ile gösterilmesini belirler. İki değer alır.
**normal | small-caps.**

	:::css
	 span { font-variant: small-caps; }


<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
Türkçe karakterlerde sorun çıkardığı unutulmamalı

### font

Yukardı anlatılan font özelliklerinin hatta ek olrak **line-height**
değerinide tek sefer de tanımlamak için kullanılır. Bir [kısaltmadır][].

<div class="cssozelliktanimi">
**Yapısı :**font: <değer> **Aldığı Değerler :**[ <font-style> || <font-variant> || <font-weight> ]? <font-size> [ / <line-height> ]? <font-family> **Başlangıç değeri:**tanımsız **Uygulanabilen
elementler:** tüm elementler **Kalıtsallık:** Var

</div>
	:::css
	 h2 { font: bold italic 200%/1.2 Verdana,
Helvetica, Arial, sans-serif; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
</p>

  [renk]: http://www.fatihhayrioglu.com/?p=95
  [kısaltmadır]: http://www.fatihhayrioglu.com/?p=6
