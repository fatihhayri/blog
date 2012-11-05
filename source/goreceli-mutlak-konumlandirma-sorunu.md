Title: Göreceli-Mutlak Konumlandırma Sorunu
Date: 2006-12-27 15:57
Category: CSS, XHTML
Tags: CSS, Göreceli-Konumlandırma, Mutlak-Konumlandırma, sorun, XHTML

Bu hata göreceli olarak konumlandırılmış(position:relative) bir
elementin içinde mutlak konumlandırılmış(position:absolute) elementlerin
bulunduğu durumlarda meydana gelir. Bu hata IE6 ve altı versiyonlarda
görülür.

![][]

Normal Görünüm - Firefox 2.0

![][1]

Hatalı Görünüm - IE6

Yukarıdaki ekran görüntülerinde de görüldüğü gibi göreceli
konumlandırma(position:relative) içerisinde kullanılan mutlak
konumlandırılmış(position:absolute) nesneler Internet Explorer'da hatalı
görünücektir. Bu hata ie'nin farklı versiyonlarında farklı şekilde tepki
verebilir, yani farklı şekilde görülebilir.

Bu sorunu çözmek için uygulanan yöntemlerden biri göreceli konumlandırma
uygulanmış kapsayıcı katmana genişlik ve yükseklik vermektir.

İkinci bir çözüm olarak yükseklik göreceli olduğu durumlar için
uygulanan bir yöntemdir.

	:::css
	 /* IE-mac den gizle */ * html
.container1 {height: 1%;} /* IE-mac den gizleme sonu */ 

## Kaynak

-   [http://www.positioniseverything.net/abs_relbugs.html][]

</p>

  []: /images/konumlandirma_hata_ff.gif
  [1]: /images/konumlandirma_hata_ie.gif
  [http://www.positioniseverything.net/abs_relbugs.html]: http://www.positioniseverything.net/abs_relbugs.html
