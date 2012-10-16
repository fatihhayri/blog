Title: CSS Kutu Modeli Özellikleri -4
Date: 2006-08-05 13:17
Category: CSS
Tags: clear, CSS, float, height, width

Kutu modeli özelliklerine devam ediyoruz. Sırasıyla aşağıdaki
özellikleri inceleyeceğiz: <!--more-->

-   Width
-   Height
-   Float
-   Clear

![Kutu Modeli][]

### width<a name="01"></a>

**Yapısı :** width: <deger> **Aldığı Değerler :** [<uzunluk değeri
>][] | [<yüzde>][<uzunluk değeri >] | auto | inherit **Başlnagıç
değeri:** auto **Uygulanabilen elementler:** [Block-level ve replaced
elementler][] **Kalıtsallık:** Yok

[Blok-level ve replaced elementlerin][Block-level ve replaced
elementler](örn: img, input, textarea vd.) tümü bir genişlik(width)
değeri alır. Elementlerin başlangıçtaki genişlik değeri **auto** yani
kendi asıl genişliğidir. (Örneğin bir resmin genişliği gibi) Yüzde
değeri [ebveyn elementi][] kıstas alarak uygulanır. Negatif değeri
almaz.

	:::css
	 p { width: 200px; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer 4+ Netscape 4+ Opera 3.6+ W3C's
CSS Level 1+ CSS Profile 1.0

</div>
### height <a name="02"></a>

**Yapısı :** height: <deger> **Aldığı Değerler :** [<uzunluk değeri
>][] | auto | inherit **Başlangıç değeri:** auto **Uygulanabilen
elementler:** [Block-level ve replaced elementler][] **Kalıtsallık:**
Yok

[Blok-level ve replaced elementlerin][Block-level ve replaced
elementler](örn: img, input, textarea vd.) tümü bir yükseklik(height)
değeri alır. Elementlerin başlangıçtaki yükseklik değeri **auto** yani
kendi asıl yüksekliğidir. (Örneğin bir resmin yüksekliği gibi) Negatif
değeri almaz.

	:::css
	 h2 { height: 0.25in; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer 4+ Netscape 6+ Opera 3.6+ W3C's
CSS Level 1+ CSS Profile 1.0

</div>
### float<a name="03"></a>

**Yapısı :** float: <deger> **Aldığı Değerler :** left | right | none
|inherit **Başlnagıç değeri:** none **Uygulanabilen elementler:** tüm
elementler **Kalıtsallık:** Yok

**float** **özelliği** bir elementi(img, table, div vd.) konumuNu
belirlemek(sağa veya sola ) için kullanılır. Siz bir elemente
**flaot=left** değeri verirseniz diğer elementler o elementin sağından
akar. Bu HTML3,2 deki resime(**img**) uygulanan **align="left"** ve
**align="right"** ile özdeş bir özelliktir. Ancak CSS 1 tüm elementlere
**float** özelliği vermemizi sağlıyor. HTML 3,2 sadece **img** ve
**table** için bu özelliği kullanmamıza izin veriyordu. **float**
özelliği sonraki derslerde daha ayrıntılı gösterilecektir. **float**
özelliği CSS ile tablosuz web sitesi oluşturma metodunun en önemli
öğelerinden biridir. 	:::css
	 p img { float: left;
margin: 25px; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer 4+ Netscape 4+ Opera 3.6+ W3C's
CSS Level 1+ CSS Profile 1.0

</div>
### clear<a name="04"></a>

**Yapısı :** clear: <deger> **Aldığı Değerler :** none | left | right
| both **Başlnagıç değeri:** tanımsız **Uygulanabilen elementler:** tüm
elementler **Kalıtsallık:** Yok

Resim ve metin elementleri diğer elementlere göre floting element olarak
tanımlanır. **clear** özelliği **floating** uygulanmayan elemente köşe
tanımı yapar. **left** değeri uygulandığı elementi floating elementin
bir alt soluna atar, **right** özelliği benzer şekilde sağa atar,
**none** özelliği elementin başlangıç değerini geri döndürür ve **both**
değeride iki floating elementin aşağısına atar. **clear** özelliği
sonraki derslerde daha ayrıntılı gösterilecektir. **clear** özelliği CSS
ile tablosuz web sitesi oluşturma metodunun en önemli öğelerinden
biridir.

	:::css
	 h3 { clear: left; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer 3+ Netscape 4+ Opera 4+ W3C's CSS
Level 1+ CSS Profile 1.0

</div>
</p>

  [Kutu Modeli]: http://fatihhayrioglu.com/images/basit_boxmodel.gif
  [<uzunluk değeri >]: http://www.fatihhayrioglu.com/?p=95
  [Block-level ve replaced elementler]: http://www.fatihhayrioglu.com/?p=13
  [ebveyn elementi]: http://www.fatihhayrioglu.com/?p=62
