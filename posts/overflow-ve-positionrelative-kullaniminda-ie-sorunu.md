Title: overflow ve position:relative  kullanımında ie sorunu
Date: 2010-06-30 22:07
Category: CSS, XHTML
Tags: ie, ie6, ie7, overflow, position:relative, sorun

Bir sorun ile daha karşınızdayım. Evet yine ie ve yine sorun. Bir
projeye başladığımda kodlamayı yaparken devamlı ie6 ile test ediyorum,
ama bazı sorunları daha çözerim diye bırakıyorum, bunun güzel bir şey
olduğunu biliyorum ama sorunlardan gına gelince kendimi rahatlatmak için
böyle bir yola başvuruyorum. Daha sonra projenin sonlarına doğru bu
sorunların üzerine eğiliyorum. İlk baktığımda bana çok zor gibi gelen
bazı sorunları gidermek için bazen tek bir arama ile cevaba ulaşıyorum
ve seviniyorum, korktuğum kadar beni uğraştırmadığı için.

Sorunu şöyle tanımlayabilirim; overflow kullandığım bir eleman içindeki
bir elemana position:relative tanımladığımda relative verdiğim eleman
overflow uyguladığım elemanın dışına çıkıyor ve scroll olmuyor.
<!--more-->

Şöyle küçük bir örnek durumu daha iyi gösterecektir.

[sourcecode language="html"] \<div id="icerikAlani"\> \<p\>İlk
paragaraf\</p\> \<p class="relative"\>position:relative uygulanan
kısım\</p\> \</div\> [/sourcecode]

CSS kodu da şöyle

[sourcecode language="css"] \#icerikAlani{ height:80px; overflow:auto;
width:200px; height:80px; background-color:\#ccc } .relative{
position:relative; background-color:lightblue; width:150px; }
[/sourcecode]

Sonuca ie 6 ve 7 ile baktığımızda aşağıdaki gibi bir sorun ile
karşılaşacağız.

Örneği görmek içni [tıklayınız.][]

[![][]][]

Sorunun çözümü ise çok basit. overflow uyguladığımız elemana
position:relative tanımı yaparak sorunu giderebilirsiniz.

[sourcecode language="css" highlight="7"] \#icerikAlani{ height:80px;
overflow:auto; width:200px; height:80px; background-color:\#ccc;
position:relative; } .relative{ position:relative;
background-color:lightblue; width:150px; } [/sourcecode]

### Kaynaklar

-   [http://snook.ca/archives/html\_and\_css/position\_relative\_overflow\_ie/][]
-   [http://www.rowanw.com/bugs/overflow\_relative.htm][]
-   [http://dustyreagan.com/workaround-to-ies-overflow-auto-and/][]

</p>

  [tıklayınız.]: http://fatihhayrioglu.com/dokumanlar/position_relative_overflow.html
  []: http://www.fatihhayrioglu.com/wp-content/position_relative_overflow_ie.jpg
    "position_relative_overflow_ie"
  [![][]]: http://www.fatihhayrioglu.com/wp-content/position_relative_overflow_ie.jpg
  [http://snook.ca/archives/html\_and\_css/position\_relative\_overflow\_ie/]:
    http://snook.ca/archives/html_and_css/position_relative_overflow_ie/
  [http://www.rowanw.com/bugs/overflow\_relative.htm]: http://www.rowanw.com/bugs/overflow_relative.htm
  [http://dustyreagan.com/workaround-to-ies-overflow-auto-and/]: http://dustyreagan.com/workaround-to-ies-overflow-auto-and/
