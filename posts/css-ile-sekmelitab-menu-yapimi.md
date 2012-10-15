Title: CSS ile Sekmeli(Tab) Menü Yapımı 
Date: 2006-11-26 23:06
Category: CSS, Web Standartları, XHTML
Tags: CSS, menü, sekme, tab, Web Standartları, XHTML

Sekmeli menümüzü [Doug Bowman'ın][] [Sliding Doors][] tekniği ile
yapacağız. Bu teknik bize esnek yapılı, yuvarlak kenarlı sekmeli menü
yapma olanağı sağlar. Adım adım gidersek <!--more-->

**1.Adım** Başlangıç olarak her zamanki gibi XHTML kodumuzu yazalım:

[sourcecode language="html"]\<ul\> \<li\>\<a href="\#"\>Ana
Sayfa\</a\>\</li\> \<li\>\<a href="\#"\>Haberler\</a\>\</li\> \<li\>\<a
href="\#"\>Ürünler\</a\>\</li\> \</ul\>[/sourcecode]

<div class="class=" ekstrabilgi"">
Tekniğin özeti şu menü oluşturmak için hazırlanan XHTML kodunda sırasız
listeler(li) bir zemin resmi(sekme\_sag\_resim.gif) ve link
elementine(a) bir zemin resmi(sekme\_sol\_resim.gif) atayarak esneklik
sağlamak.

</div>
**2. Adım** Daha önceki menü örneklerinden de alışkın olduğumuz
margin,padding ve liste imgelerini kaldırma işlemini yapalım:

[sourcecode language="css"] ul { margin: 0; padding: 0; list-style:
none; width: 600px; float: left; border-bottom: 1px solid gray; }
[/sourcecode]

**3. Adım** Yukarıda bahsettiğimiz metodu uygulamak için iki adet resim
hazırlamalıyız.

![][] ![][1]

Bu resimlerin yüksekliklerinin uzun olmasının nedeni font boyutunun
arttırılması(yakınlaştırma) durumunda iki satır olabilecek menülerde
menü görünümünün bozulmaması içindir.

**4. Adım** Menüyü yatayda sıralamak için **float:left** tanımlaması
yapıyoruz ve sağ zemin
resmini(<span class="alternatifard">sekme\_sag\_resim.gif</span>)
uyguluyoruz:

[sourcecode language="css"] ul li { float: left; background:
url(images/sekme\_sag\_resim.gif) no-repeat top right; } [/sourcecode]

**5. Adım** Daha önceki örneklerde gördüğümüz gibi tüm sekmeye link
vermek için **display:block** tanımlaması yapıyoruz, sekmenin sol
kısmını tamamlamak için zemin resmi olarak(sekme\_sol\_resim.gif)
ekliyoruz, tüm sekmelerde aynı yüksekliği yakalamak için
**line-height**tanımlamasını yapıyoruz,
<span class="alternatifard">**text-decoration: none**</span> ile link
alt çizgilerini kaldırıyoruz ve IE Mac ortamında sorun çıkarmaması için
**float:left** ekliyoruz:

[sourcecode language="css"]\<ol\> li a {
background:url(images/sekme\_sol\_resim.gif) no-repeat left top;
display: block; padding: 0 2em; line-height: 2.5em; text-decoration:
none; float: left; color:\#000; } [/sourcecode]

**6. Adım** Güzel bir görünüm katmak için basit bir rollover efekti
verelim:

[sourcecode language="css"] ul a:hover { color: \#9D9C9C; }
[/sourcecode]

Örnek kodları indirmek için [tıklayınız.][]

Sonuç: Kodumuzu çalıştırdığımızda aşağıdaki sonucu elde edeceğiz. Tab
menüye bir çok örnek var resimli, resimsiz, resimli rollover gibi;
internette aratarak bir çok örnek bulabilirsiniz.

<iframe src="/dokumanlar/sekmeli_menu.html" width="350" height="80" frameborder="0" scrolling="no"></iframe>

</p>

  [Doug Bowman'ın]: http://stopdesign.com/
  [Sliding Doors]: http://alistapart.com/articles/slidingdoors/
  []: /pdf/sekme_sol_resim.gif
  [1]: /pdf/sekme_sag_resim.gif
  [tıklayınız.]: /dokumanlar/sekmeli_menu.zip
