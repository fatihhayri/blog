Title: İE kalıtsal margin sorunu: form elementleri ve hasLayout
Date: 2010-04-28 23:58
Category: CSS, Web Standartları, XHTML
Tags: hasLayout, ie, ie6, ie7, kalıtsal margin sorunu, Margin

İnternet Explorer ile bir çok sorun yaşıyoruz genelde ie'nin boyut
taramalarında. Bu sorunların kaynağı "hasLayout" olarak adlandırılan ie
kabulü. hasLayout hakkında ayrıntılı bilgi için [bu siteye göz atın][].
Microsoft bu tanımlamadaki hatasını kabul etti ve ie8 de "hasLayout"
kabulunü bıraktı. Buna da şükür.

Ben genelde bu sorun ile özel textbox alanlarını kodlarken
karşılaşıyorum.<!--more-->

![][]

yukarıdaki gibi bir tasarımı koda çevirirken

[sourcecode language="html"] \<div class="dis"\> \<div
class="ic"\>\<input type="text" value="Arama" /\>\</div\> \</div\>
[/sourcecode]

CSS kodu

[sourcecode language="css"] div.dis{ margin-left:65px; } div.ic{
width:241px; height:25px; background:url(arama\_ardalan.gif) 0 0
no-repeat } div.ic input{ border:0; background:none; width:204px;
margin:4px 0 0 5px; font-size:11px; color:\#534013; } [/sourcecode]

Örneği görmek için [tıklayınız.][]

Böyle bir kod yazıyorum. Dıştaki div(div.dis) herhangi bir kapsayıcı div
olarak düşünün. Sayfanın diğer bir öğesi yani bu arama kısmı ile alakası
yok. Bu kapsayıcı katmandaki margin tanımı ie'de sorun çıkarıyor.

[![][1]][]

Firefox'da yukarıdaki gibi bir görüntü alırken

[![][2]][]

İnternet Explore 6 ve 7 sürümlerinde yukarıdaki gibi bir görüntü ile
karşılaşıyorum. En dıştaki katmana atadığım margin-left değeri içerideki
elemanımı etkiliyor. Kalıtsal olarak bu değeri alıyor. Sorunu ilk önce
"[IE'da İkikat görülen Margin Problemi ve Çözümü][]" anlattığım gibi bir
sorun olduğunu düşündüm ama değildi. Bu sefer ki farklı bir sorun.
positioniseverything.net sitesinde aynı sorunu görünce anca adını
koyabildim.

Sorun; input alanını kapsayan ebeveyn elemanda hasLayout ve margin
tanımı var ise oluyor. Kaynak kısmında verdiğim sitede bir kaç çözüm
önerisi var. Ancak ben hasLayout sorunlarının en kolay çözüm yolu olan
zoom:1 tanımı ile bu sorunu aştım. Margin tanımı olan elemana zoom:1
tanımı yapınca sorun çözüldü

[sourcecode language="css"] div.dis{ margin-left:65px; zoom:1}
[/sourcecode]

Örneği görmek için [tıklayınız.][3]

[![][4]][]

Bu sorun tüm input çeşitlerinde(text, checkbox, radyo buton ve resim)
meydana geliyor, ayrıca textarea'da yaşanıyor bu sorun, ancak select
elemanında bu sorun ile karşılaşılmıyor.

### Kaynak

-   [http://www.positioniseverything.net/explorer/inherited\_margin.html][]

</p>

  [bu siteye göz atın]: http://www.satzansatz.de/cssd/onhavinglayout.html
  []: http://www.fatihhayrioglu.com/wp-content/arama_ardalan1.gif
    "arama_ardalan1"
  [tıklayınız.]: http://fatihhayrioglu.com/dokumanlar/margin_inherit_form/inherit_margin_form_orn.html
  [1]: http://www.fatihhayrioglu.com/wp-content/margin_inherit_ff.gif
    "margin_inherit_ff"
  [![][1]]: http://www.fatihhayrioglu.com/wp-content/margin_inherit_ff.gif
  [2]: http://www.fatihhayrioglu.com/wp-content/margin_inherit_ie.gif
    "margin_inherit_ie"
  [![][2]]: http://www.fatihhayrioglu.com/wp-content/margin_inherit_ie.gif
  [IE'da İkikat görülen Margin Problemi ve Çözümü]: http://www.fatihhayrioglu.com/ieda-ikikat-gorulen-margin-problemi-ve-cozumu/
  [3]: http://fatihhayrioglu.com/dokumanlar/margin_inherit_form/inherit_margin_form_ornc.html
  [4]: http://www.fatihhayrioglu.com/wp-content/margin_inherit_ie_c.gif
    "margin_inherit_ie_c"
  [![][4]]: http://www.fatihhayrioglu.com/wp-content/margin_inherit_ie_c.gif
  [http://www.positioniseverything.net/explorer/inherited\_margin.html]:
    http://www.positioniseverything.net/explorer/inherited_margin.html