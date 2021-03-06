Title: z-index
Date: 2008-01-14 23:10
Category: CSS, Web Standartları, XHTML
Tags: CSS, Göreceli-Konumlandırma, Haberler, Mutlak-Konumlandırma, Sabit-Konumlandırma, Web Standartları, XHTML, z-ekseni, z-index

z-index, konumlandırma elementleri uygulanmış katmanların z-eksenindeki
konumu belirlemek için kullanılır.

z-index tüm elementlere uygulanamaz sadece konumlandırma değeri atanmış
elementlere uygulanır. Bunun anlamı eğer bir elementi aynı z-ekseni
üzerinde üste veya alt sıraya atmak istiyorsanız ilk olarak
konumlandırma değeri atamalısınız.

z-index değeri dokümanımızdaki elementlerin istiflenme sıralarını
belirler. z-index elementleri z-ekseninde nerede duracağınız belirler,
üstte veya altta. z-indeks değeri küçük olan elementler altta büyük olan
elementler ise üstte görünecektir. Sitenizi kodlarken birçok yerde
z-index ihtiyaç duymayız çünkü normal sayfa akışında elementler yanyana
durduğu için böyle bir özelliğe ihtiyaç yoktur, ne zamanki elementlere
konumlandırma değeri tanımladığımızda elementler bir biri üzerine
bindiğinde z-index değerine ihtiyaç duyarız. z-index mutlak, göreceli ve
sabit konumlandırma atandığı veya elemente eksi değer verilerek konumu
değiştirildiğinde uygulanır.

![][]

**Yapısı:**z-index: <deger\>    
**Aldığı Değerler:**<[sayısal değer][] \> | auto | inherit  
**Başlangıç değeri:**auto   
**Uygulanabilen elementler:**postion uygulanan elementlere   
**Kalıtsallık:**Yok
{: .cssozelliktanimi}

**Tarayıcı Uyumu **   
Firefox   
Chrome   
Safari  
Opera   
İnternet Explorer   
**Mobil Tarayıcılar**  
iOS Safari  
Opera Mobile   
Android Browser
{: .tarayiciuyum}

Konumlandırma değeri relative, absolute ve fixed uygulanmış katmanların
görünürlüğünü z-index ile ayarlayabiliriz.

	:::css
	div{ 
		position:absolute; 
		width:150px;
		height:150px; 
	} 
	
	div.bir { 
		background: #FEB3BE; 
		border:2px solid #CC8B94; 
		top: 0; 
		left: 0; 
	} 
	
	div.iki { 
		background: #E5ECF9; 
		border:2px solid #BCCCEB; 
		top: 10px; 
		left: 10px; 
	} 

Yukarıda örnekte görüldüğü gibi katmanlar üst üste sıralanmıştır.
Birbirinden 10px üst ve 10px soldan mesafe bırakılmıştır. Üstte kalan
katman alttakileri gizlemiştir. Tüm katmanların z-index değeri
atanmamıştır bu nedenle başlangıç değeri olan z-index:auto değerini
almışlardır.

	:::html
	<body> 
		<div class='kapsul'> 
			<div class='bir'></div>
			<div class='iki'></div> 
		</div>
	</body>


z-index değeri otomatik olduğu için her katman html'deki sırasına göre
yerleşmiştir. İlk başta yazılmış olanlar altta sonrakiler üstte olacak
şekilde sıralanmıştır.

![][1]

Eğer katmanları istediğimiz sıra ile göstermek istiyor isek her katmana
sırasına göre sayısal değer atamalıyız. Yüksek değer alan katmanlar
üstte düşük değer alan katmanlar ise altta kalacaktır. Buna göre
istediğimiz görüntüyü elde etmek için z-index değerleri vermeliyiz.

Yukarıda yaptığımız örnekte alttaki kırmızı katmanı üste çıkarmak için
z-index değerini 2 versek. Mavi katmanın z-index değerini 1 verirsek
katman görünümünü tersine dönecektir.

	:::css
	div{ 
		position:absolute;
		width:150px; 
		height:150px; 
	} 
	
	div.bir { 
		background: #FEB3BE; 
		border:2px solid #CC8B94; 
		top: 0; 
		left: 0; 
		z-index:2 
	} 
	
	div.iki { 
		background: #E5ECF9; 
		border:2px solid #BCCCEB; 
		top: 10px; 
		left: 10px; 
		z-index:1 
	}


![][2]

İçiçe girmiş katmanlarda z-index davranışları farklıdır. İçiçe geçmiş
katmanlardaki z-index:auto değeri gibi davranır ve sayısal atamaları
dikkate almaz.

	:::html
	<body> 
		<div class='kapsul'>
			<div class='bir'><div class='iki'></div></div>
		</div>
	</body>


z-index değeri yüksek olmasına rağmen bir sınıfını alan katmana altta
kalacaktır. Çünkü iç içe geçmiş elementlerde z-index'e atanan sayısal
değerler geçersizdir. Sıralama z-index:auto ya göre yapılır.


**Not**
z-index eksi değerlerinde Firefox sorun çıkarıyor. Firefox 3'da sorun
giderilmiş.

## Sonuç

Sonuç olarak z-index özelliğinin çok kullanışlı ancak sorunları çok bir
özellik olduğunu düşünüyorum. Birçok makalede istediğim manada detaylı
bir z-index anlatımı bulamadığımı itiraf etmeliyim. Ancak kodlama
yaparken aklımızda olması gereken kuralları kavrarsak z-index özelliğini
daha bilinçli kullanacağımız kesin:  

-   z-index değeri; aynı z-ekseninde bulunan(kapsayan elementler hariç)
    katmanların altta mı üstte mi kalacağınız belirlemek için
    kullanılır.  
-   z-index sadece position değeri **relative**, **absolute** ve
    **fixed** olan nesnelere uygulanır.
-   Saydamlık değeri(opacity) 1'den küçük verilen nesnelerde z-index
    kullanımı daha kolay anlaşılır.
-	Konumlandırma uygulanmış elementlerde z-index etkileri  
-   Mevcut sıralama durumunda elementin sırasını belirler
-   Elementin kendi kısmındaki durumun belirler
-   Eğer z-index değeri atanmamış ise z-eksenindeki arkadan öne doğru
sıralama aşağıdaki gibidir:  
-   Normal akıştaki kutular koddaki sıraya göre sıralanır
-   float uygulanmış kutular
-   Konumlandırma uygulanmış elementlerde ise kodlamadaki sıraya göre   

z-indeks ile ilgi bazı problemler ve çözüm önerileri var bunları aşağıda
listeledik bu linklerdeki çözümleri incelemenizi tavsiye ederiz. Karşıma
çıkan bazı problem ve çözümleri sitede yayınlamaya devam edeceğim.

## Kaynaklar

-   [http://www.search-this.com/2007/08/15/give-me-some-zzzzzs/][]
-   [http://www.brainjar.com/css/positioning/default5.asp][]
-   [http://joshuaink2006.johnoxton.co.uk/blog/82/flash-content-and-z-index][]
    (flash ve html elemtnleri)
-   [http://www.blooberry.com/indexdot/css/properties/position/zindex.htm][]
    (tarayıcı destek)
-   [http://www.westciv.com/style_master/academy/css_tutorial/properties/page_layout.html#z-index][]
-   [http://developer.mozilla.org/en/docs/Understanding_CSS_z-index][]
-   [http://css-discuss.incutio.com/?page=OverlappingAndZIndex][]
-   [http://csscreator.com/blog/z-index][]
-   [http://www.fatihhayrioglu.com/?p=151][]
-   CSS Mastery Advanced Web Standards Solutions
-   Cascading Style Sheets The Definitive Guide
-   Wrox Beginning CSS 2nd.Edition

## Sorunlar ve çözümler

-   [http://brandonaaron.net/docs/bgiframe/][]
-   [http://www.askapache.com/css/getting-flash-to-show-up-in-front-of-content.html][]
-   [http://www.last-child.com/conflicting-z-index-in-ie6/][]
-   [http://therealcrisp.xs4all.nl/meuk/IE-zindexbug.html][]
-   [http://www.hedgerwow.com/360/bugs/css-select-free.html][]
-   [http://blogs.msdn.com/ie/archive/2006/01/17/514076.aspx][]
-   [http://randsco.com/index.php/2005/09/11/changing_z_index_on_hover][]

  []: /images/z-ekseni.gif
  [sayısal değer]: http://www.fatihhayrioglu.com/?p=95
  [1]: /images/zindeks_otomatik.gif
  [2]: /images/zindeks_sayi.gif
  [http://www.search-this.com/2007/08/15/give-me-some-zzzzzs/]: http://www.search-this.com/2007/08/15/give-me-some-zzzzzs/
  [http://www.brainjar.com/css/positioning/default5.asp]: http://www.brainjar.com/css/positioning/default5.asp
  [http://joshuaink2006.johnoxton.co.uk/blog/82/flash-content-and-z-index]: http://joshuaink2006.johnoxton.co.uk/blog/82/flash-content-and-z-index
  [http://www.blooberry.com/indexdot/css/properties/position/zindex.htm]: http://www.blooberry.com/indexdot/css/properties/position/zindex.htm
  [http://www.westciv.com/style_master/academy/css_tutorial/properties/page_layout.html#z-index]: http://www.westciv.com/style_master/academy/css_tutorial/properties/page_layout.html#z-index
  [http://developer.mozilla.org/en/docs/Understanding_CSS_z-index]: http://developer.mozilla.org/en/docs/Understanding_CSS_z-index
  [http://css-discuss.incutio.com/?page=OverlappingAndZIndex]: http://css-discuss.incutio.com/?page=OverlappingAndZIndex
  [http://csscreator.com/blog/z-index]: http://csscreator.com/blog/z-index
  [http://www.fatihhayrioglu.com/?p=151]: http://www.fatihhayrioglu.com/?p=151
  [http://brandonaaron.net/docs/bgiframe/]: http://brandonaaron.net/docs/bgiframe/
  [http://www.askapache.com/css/getting-flash-to-show-up-in-front-of-content.html]: http://www.askapache.com/css/getting-flash-to-show-up-in-front-of-content.html
  [http://www.last-child.com/conflicting-z-index-in-ie6/]: http://www.last-child.com/conflicting-z-index-in-ie6/
  [http://therealcrisp.xs4all.nl/meuk/IE-zindexbug.html]: http://therealcrisp.xs4all.nl/meuk/IE-zindexbug.html
  [http://www.hedgerwow.com/360/bugs/css-select-free.html]: http://www.hedgerwow.com/360/bugs/css-select-free.html
  [http://blogs.msdn.com/ie/archive/2006/01/17/514076.aspx]: http://blogs.msdn.com/ie/archive/2006/01/17/514076.aspx
  [http://randsco.com/index.php/2005/09/11/changing_z_index_on_hover]: http://randsco.com/index.php/2005/09/11/changing_z_index_on_hover
