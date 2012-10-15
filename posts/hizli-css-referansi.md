Title: Hızlı CSS Referansı 
Date: 2006-07-30 14:41
Category: CSS
Tags: ardalan-özellikleri, background, background-attachment, background-color, background-image, background-position, background-repeat, CSS

CSS, web kodlayıcılarına (X)HTML dökümanlarına stil uygulamalarını
sağlar. (X)HTML kodu ile stil kodunu birbirinden ayırarak web
kodlayıcılara büyük kolaylıklar sağlar. Burada genel kullanılan CSS
özelliklerini hep beraber tek tek kısaca inceleyeceğiz.<!--more-->

Burada tanımlanacak CSS özellikleri 15 Haziran 2005'de yürürlüğe giren
CSS2.1 standartlarına göre yazılmıştır.

Sırası ile aşağıdaki özelliklere değinilecektir.

-   Zemin (Background) Özellikleri
-   Kenarlık (Border) Özellikleri
-   Font Özellikleri
-   Liste Özellikleri
-   Margin Özellikleri
-   Padding Özellikleri
-   Metin Özellikleri
-   Floating ve Positioning Özellikleri
-   Tablo Özellikleri

Burada standart bir özellik tanımı kullanılacaktır.

<div class="cssozelliktanimi">
**Yapısı :** özellik\_ismi: \<deger\>  
**Aldığı Değerler :** alınan\_deger1 | alınan\_deger2 {1,4}\*   
**Başlangıç değeri:** Özelliğin atama yapılmadığı zaman ki değeri   
**Uygulanabilen elementler:** özelliğin uygulanacağı elementlerin
isimleri   
**Kalıtsallık:** Bu özelliğin atanması halinde alt elementlerini(örn:
çocuk ve torun elementlerini) etkileyip etkilemeyeceği

</div>
\* Bu işaretin anlamı bu özelliğin 1'den 4'e kadar değer alabileceğini
gösterir. Örneğin:

[sourcecode language="css"] p.deneme { border-style: solid dashed dotted
solid; } [/sourcecode]

#### CSS - Zemin(BACKGROUND) Özellikleri

![Kutu Modeli][]

Zemin(Bacground) yukarıdaki resimde padding alanı ve içerik
alanını(paragraf) kapsar.

Zemin özellikleri ile elementlere tek bir renk atanabildiği gibi
**background-image** özelliği ile (X)HTML'in çok üzerinde eklemelerde
yapılabilir.

Zemin özelliklerini tek tek incelersek:

-   background-color
-   background-image
-   background-repeat
-   background-attachment
-   background-position
-   background

### background-color

Elementlerin zeminine bir renk atamak için kullanılır.

**Yapısı :** background-color: \<deger\>  
**Aldığı Değerler :** [renk][] | transparent  
**Başlangıç değeri:** transparent  
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

**Örnek:**

[sourcecode language="css"] p { background-color: \#ddd; } [/sourcecode]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### background-image

Elementlerin zeminine resim eklemek için kullanılır.

**Yapısı :** background-image: \<deger\>  
**Aldığı Değerler :** [url][renk] | none   
**Başlangıç değeri:** none   
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

**Örnek:**

[sourcecode language="css"] body { background-image:
url(/images/deneme.gif) } [/sourcecode]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### background-repeat

**background-repeat** özelliği **background-image** ile zemine eklenen
resmin tekrarı ile özellikleri belirler.

**Yapısı :** background-image: \<deger\>  
**Aldığı Değerler :** repeat | repeat-x | repeat-y | no-repeat   
**Başlangıç değeri:** repeat   
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

**Örnek:**

[sourcecode language="css"] body { background: white url(deneme.gif);
background-repeat: repeat-x; } [/sourcecode]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### background-attachment

**background-attachment** özelliği zemine eklenen resmin sayfa ile
scroll etmesini veya sayfanın zeminin de çakılı kalmasını sağlar.

**Yapısı :** background-attachment: \<deger\>  
**Aldığı Değerler :** scroll | fixed   
**Başlangıç değeri:** scroll   
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

**Örnek:**

[sourcecode language="css"] body { background: white url(deneme.gif);
background-attachment: fixed; } [/sourcecode]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### background-position

**background-position** özelliği **background-image** ile belirlenen
resmin başlangıç noktasını belirler. Bu özellik sadece [block-level][]
ve replaced(Bu elementler kendine özgü boyutları olan elementler olarak
tanımlanabilir. Örn: **IMG**, **INPUT**, **TEXTAREA**, **SELECT**, ve
**OBJECT**) elementlere uygulanır.

**Yapısı :** background-position: \<deger\>  
**Aldığı Değerler :** [[\<percentage\>][renk] | [\<length\>][renk]]{1,2}
| [top | center | bottom] || [left | center | right]  
**Başlangıç değeri:** 0% 0%   
**Uygulanabilen elementler:** [Block-level ve replaced
elementler][renk]  
**Kalıtsallık:** Yok

En kolay kullanım şekli;   
Yatay değerler için: left,center,right  
Dikey değerler için: top, center, bottom  
  
[Yüzde değerleri][renk] ve [uzunluk değerleri][renk] de kullanılır.
Yüzde değerleri elemtin boyuta bağlı olarak görecelidir. Uzunluk
değerleri de kullanılabilir. Ancak farklı ekran çözünürlklerinde farklı
görüntülere sebebiyet vermesi nedeni ile pek önerilmez.

Yüzde değerler ve uzunluk değerleri verildiğinde ilk değer yatay içindir
sonra gelen dikey değerdir. Örneğin %10 %60 değeri bir zemin resmi için
verilmiş ise %10 değeri yataydaki değeri %60 ise dikey olarak değerini
gösterir. 5px 10px gibi değerler verilmişse resmin sol üstden 5px sağa
ve 10px aşağıdan başlayacağını belirler.

Eğer yanlızca yatay değer verilmiş ise, dikey değer %50 olarak kabul
edilecektir. Yüzde değerler ve uzunluk değerleri eksi değerler alabilir.
Örn -2px %10 gibi. Aşağıdaki örnekler genel kullanım için yararlıdır:

-   **top left** = **left top** = **0% 0%**
-   **top** = **top center** = **center top** = **50% 0%**
-   **right top** = **top right** = **100% 0%**
-   **left** = **left center** = **center left** = **0% 50%**
-   **center** = **center center** = **50% 50%**
-   **right** = **right center** = **center right** = **100% 50%**
-   **bottom left** = **left bottom** = **0% 100%**
-   **bottom** = **bottom center** = **center bottom** = **50% 100%**
-   **bottom right** = **right bottom** = **100% 100%**

**Örnek:**

[sourcecode language="css"] body { background-image: url(deneme.gif);
background-repeat: no-repeat; background-position: center; }
[/sourcecode]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
### background

Bu özellik Zemin(background) ile ilgili tüm özelliklerin bir arada
kullanımı sağlar.

**Yapısı :** background: \<deger\>  
**Aldığı Değerler :** <background-color>\<background-color\> ||
\<background-image\> || \<background-repeat\> ||
\<background-attachment\> || \<background-position\>   
**Başlangıç değeri:** Tanımsız   
**Uygulanabilen elementler:** tüm elementler  
**Kalıtsallık:** Yok

**Örnek:**

[sourcecode language="css"] body{ background: white url(deneme.gif) }
blockquote { background: \#f00 } p { background:
url(../images/deneme.png) \#f00 fixed } table{ background: \#0c0
url(deneme.jpg) no-repeat bottom right } [/sourcecode]

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 1+

</div>
</p>

  [Kutu Modeli]: http://fatihhayrioglu.com/images/basit_boxmodel.gif
  [renk]: http://www.fatihhayrioglu.com/?p=95
  [block-level]: #