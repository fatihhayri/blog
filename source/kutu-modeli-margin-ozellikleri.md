Title: CSS Kutu Modeli - Margin Özellikleri
Date: 2006-08-03 23:38
Category: CSS
Tags: bottom, CSS, left, Margin, margin-right, margin-top

Margin özelliği elementin etrafındaki boşluk olarak tanımlanır.
Negatifdeğer alabilir. Tek tek özellikler(margin-top,margin-left vd.)
atanabildiğigibi tek bir özellikle(margin) de tanımlama yapılabilir.
Margin özelliklerinianlamak için lütfen [Box modellerine][] bir göz
atın. <!--more-->

![Kutu Modeli][]

-   margin-top
-   margin-right
-   margin-bottom
-   margin-left
-   margin

### margin-top<a name="01"></a>

**Yapısı :** margin-top: <deger> **Aldığı Değerler :** [<uzunluk değeri >][] | [<yüzde>][<uzunluk değeri >] | auto **Başlnagıç
değeri:** 0 **Uygulanabilen elementler:** tüm elementler
**Kalıtsallık:** Yok

**margin-top** özelliği elementin üst kenar boşluğunu bellibir değer
kadar veya yüzde olarak belirler.Negatif değer alabilir.

[sourcecode language='css'] body { margin-top: 0 } 

<div class="tarayiciuyum">
**Browser Uyumu:** Internet Explorer 4+ Netscape 4+ Opera 3.6+ W3C's CSS
Level 1+ CSS Profile 1.0

</div>
### margin-right <a name="02"></a>

**Yapısı :** margin-right: <deger> **Aldığı Değerler :** [<uzunluk değeri >][] | [<yüzde>][<uzunluk değeri >] | auto **Başlnagıç
değeri:** 0 **Uygulanabilen elementler:** tüm elementler
**Kalıtsallık:** Yok

**margin-right** özelliği elementin sağ kenar boşluğunu bellibir değer
kadar veya yüzde olarak belirler.Negatif değer alabilir.

[sourcecode language='css'] p.diger { margin-right: 50% } 

<div class="tarayiciuyum">
**Browser Uyumu:** Internet Explorer 3+ Netscape 4+ Opera 3.6+ W3C's CSS
Level 1+ CSS Profile 1.0

</div>
### margin-bottom<a name="03"></a>

**Yapısı :** margin-bottom: <deger> **Aldığı Değerler :** [<uzunluk değeri >][] | [<yüzde>][<uzunluk değeri >] | auto **Başlnagıç
değeri:** 0 **Uygulanabilen elementler:** tüm elementler
**Kalıtsallık:** Yok

**margin-bottom** özelliği elementin alt kenar boşluğunu bellibir değer
kadar veya yüzde olarak belirler.Negatif değer alabilir. [sourcecode language='css'] p { margin-bottom: 10px } 

<div class="tarayiciuyum">
**Browser Uyumu:** Internet Explorer 4+ Netscape 4+ Opera 3.6+ W3C's CSS
Level 1+ CSS Profile 1.0

</div>
### margin-left<a name="04"></a>

**Yapısı :** margin-left: <deger> **Aldığı Değerler :** [<uzunluk değeri >][] | [<yüzde>][<uzunluk değeri >] | auto **Başlnagıç
değeri:** 0 **Uygulanabilen elementler:** tüm elementler
**Kalıtsallık:** Yok

**margin-left** özelliği elementin sol kenar boşluğunu bellibir değer
kadar veya yüzde olarak belirler.Negatif değer alabilir.

[sourcecode language='css'] p { margin-left: 10px } 

<div class="tarayiciuyum">
**Browser Uyumu:** Internet Explorer 3+ Netscape 4+ Opera 3.6+ W3C's CSS
Level 1+ CSS Profile 1.0

</div>
### margin<a name="05"></a>

**Yapısı :** margin: <deger> **Aldığı Değerler :** [[<percentage>][]
| [<length>][<percentage>] |auto]{1,4} **Başlnagıç değeri:**
Tanımsız **Uygulanabilen elementler:** tüm elementler **Kalıtsallık:**
Yok

**margin** özelliği yukardaki özelliklerin tek bir özellikle uygulanması
içinkullanılır.

[sourcecode language='css'] h1 { margin: 0.25in; background-color:
silver; } h1 { margin: 10px 20px 15px 5px; } 

yukarıda **h1** için margin değerleri sıralaması şöyledir:

**margin: üst sağ alt sol(saat yönünde)**

ikili ve üçlü kullanımda mevcuttur

[sourcecode language='css'] h1 {margin: 0.25em 0 0.5em;} /* esittir
'0.25em 0 0.5em 0' */ h2 {margin: 0.15em 0.2em;} /* esittir '0.15em
0.2em 0.15em 0.2em' */ p {margin: 0.5em 10px;} /* esittir '0.5em 10px
0.5em 10px' */ p.close {margin: 0.1em;} /* esittir '0.1em 0.1em 0.1em
0.1em' */ 

<div class="tarayiciuyum">
**Browser Uyumu:** Internet Explorer 4+ Netscape 4+ Opera 3.6+ W3C's CSS
Level 1+ CSS Profile 1.0

</div>
</p>

  [Box modellerine]: http://www.fatihhayrioglu.com/?p=13
  [Kutu Modeli]: http://fatihhayrioglu.com/images/basit_boxmodel.gif
  [<uzunluk değeri >]: http://www.fatihhayrioglu.com/?p=95
  [<percentage>]: #
