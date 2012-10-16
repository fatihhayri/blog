Title: CSS ile Menü Yapmak II - Yatay Menüler
Date: 2006-11-06 11:47
Category: CSS, Web Standartları, XHTML
Tags: CSS, link, menü, örnek, Web Standartları, XHTML, yatay-menüler

###### Yatay Menüler

[Bir önceki makalede][] dikey menüye bir örnek yapmıştık. şimdi de yatay
menülere bir örnek vereceğiz. Önceki makalede bahsettiğimiz gibi yatay
ve dikey menüler belli bir yere kadar kodlaması aynıdır. Biz aynı olan
kısmı geçip sonrasına devam ediyoruz. <!--more-->

Kaldığımız yerden devam edersek. Linkleri yatay olarak dizmek için
**display:inline** özelliğini kullanıyoruz:

[sourcecode language='css'] ul.menu { list-style-type: none; padding: 0;
margin: 0; } ul.menu li { display: inline; } 

![][]

Linklerin altındaki çizgileri kaldırıyoruz:

[sourcecode language='css'] ul.menu { list-style-type: none; padding: 0;
margin: 0; } ul.menu li { display: inline; } ul.menu li a {
text-decoration: none; } 

![][1]

Linkler arasına biraz boşluk veriyoruz:

[sourcecode language='css'] ul.menu { list-style-type: none; padding: 0;
margin: 0; } ul.menu li { display: inline; } ul.menu li a {
text-decoration: none; padding: .2em 1em; } 

![][2]

Menüyü biraz renklendiriyoruz:

[sourcecode language='css']ul.menu { list-style-type: none; padding: 0;
margin: 0; } ul.menu li { display: inline; } ul.menu li a {
text-decoration: none; padding: .2em 1em; color: #1B1B1B;
background-color: #E2E2E2; } 

![][3]

Son olarakta rollover efekti vermek için **a:hover** özelliğine renk
atıyoruz:

[sourcecode language='css'] ul.menu { list-style-type: none; padding: 0;
margin: 0; } ul.menu li { display: inline; } ul.menu li a {
text-decoration: none; padding: .2em 1em; color: #1B1B1B;
background-color: #E2E2E2; } ul.menu li a:hover { background-color:
#999; } 

Sonuç işte:

<iframe src="/dokumanlar/menuy.html" width="300" height="50" frameborder="0" scrolling="auto"></iframe>

Biz burada temel menü örnekleri verdik. Mesele işin yapılışını öğrenmek.
Daha ayrıntılı ve güzel örnekler internette bir çok yerde mevcut. Gerek
aşağıda verdiğimiz Kaynaklar kısmında ve gerekse İnternette aratarak bir
çok menüye ulaşabilrisiniz.

###### Kaynaklar

-   [http://css.maxdesign.com.au/][]
-   [http://www.cssplay.co.uk/menus/index.html][]
-   [http://www.alvit.de/handbook/#navmenus][]
-   [http://exploding-boy.com/images/EBmenus/menus.html][]

</p>

  [Bir önceki makalede]: http://www.fatihhayrioglu.com/?p=209
  []: /images/menu_resim1.gif
  [1]: /images/menu_resim2.gif
  [2]: /images/menu_resim3.gif
  [3]: /images/menu_resim4.gif
  [http://css.maxdesign.com.au/]: http://css.maxdesign.com.au/
  [http://www.cssplay.co.uk/menus/index.html]: http://www.cssplay.co.uk/menus/index.html
  [http://www.alvit.de/handbook/#navmenus]: http://www.alvit.de/handbook/#navmenus
  [http://exploding-boy.com/images/EBmenus/menus.html]: http://exploding-boy.com/images/EBmenus/menus.html
