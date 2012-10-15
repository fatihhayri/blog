Title: PSD&#039;den HTML&#039;e – fanatikmarslar.com Sitesinin Kodlaması III
Date: 2010-02-09 00:14
Category: CSS, Javascript, Web Standartları, XHTML
Tags: adım adım kodlama, alt sayfa, css-kodlama-düzeni, CSS-Layout, farklı tarayıcılara göre kod yazmak, psdtohtml, site-kodlama, tezahürat dinle, tezahürat ekle

### Alt Sayfaların Kodlanması

Genelde siteler yapılırken ana sayfa ve alt sayfa olarak kodlanır. Bunun
sebebi ana sayfalar tekildir, alt sayfalar ise birbirine benzeyen
yapılardan oluşur. Bu nedenle alt sayfaların bir tanesi kodlanınca diğer
sayfaların kodlanması daha az zaman alır. Bir çok freelance işinde ana
sayfa farklı alt sayfalar farklı olarak ücretlendirilir. Neyse işin bu
kısmına girmeyelim.

Eksiden sadece bir alt sayfa şablonu hazırlayıp diğer sayfa içeriklerini
o şablondaki içerik kısmına girerek tüm siteyi oluştururduk. Şimdilerde
ise neredeyse her sayfa için bir tasarım çıkıyor ve her birini ayrı ayrı
kodluyoruz.

Fanatikmarslar.com sitesini düşünürsek; bana gönderilen alt sayfa
tasarımlarından 4 tane farklı tasarıma sahip sayfa vardı. Diğerleri
bunların kopyası gibi olduğu için ben burada sizlere bu 4 alt sayfayı
nasıl kodladığımı anlatacağım.

![Marşlar][]

![Tezahürat Ekle][]

![Tezahürat İzle Dinle][]

![Genel Şablon][]

Yukarıdaki 4 sayfada gördüğümüzü özetlersek; ilk olarak üst kısım ve alt
kısmın ana sayfa ile aynı olduğunu görüyoruz. Orta kısım ise tüm alt
sayfalarda aynı. İki kolonlu bir yapı ve sağ kolon sabit. Sol içerik
kolonu içeriği değişiyor.

### Kategori Listeleme Sayfasının Kodlanması

![Marşlar][]

Orta kısmı iki kolona ayırıyorum. solOrtaAlan ve icerikalaniSag adını
verdim. İki kolonu yan yana koymak için float ve genişlik tanımlarını
yapıyoruz.

[sourcecode language="html"] \<div id="solOrtaAlan"\> ... \</div\> \<div
id="icerikalaniSag"\> ... \</div\> [/sourcecode]

CSS kodunu yazalım

[sourcecode language="css"] \#solOrtaAlan{float:left; width:650px;
margin:0 20px 0 10px; font:14px Arial, Helvetica, sans-serif;
display:inline} \#icerikalaniSag {float:left; width:300px} [/sourcecode]

**Sol Orta Alan**

\#solOrtaAlan tanımına margin tanımlarını yapıyorum. Burada "[IE'da
İkikat görülen Margin Problemi ve Çözümü][]" sorunu ile karşılaştığım
için display:inline tanımı atadım.

Kodlamaya sol orta alandan devam ediyorum.

**Başlık**

[sourcecode language="html"]\<h1\>Marşlar\</h1\>[/sourcecode]

Başlığımızı h1 ile tanımlıyoruz. Hem anlamlı kodlama hemde arama
motorlarına uygun kodlama açısından sayfa başlığını h1 ile tanımlıyoruz.
Diğer başlıklarıda sırası ile h2, h3, vd. şeklinde tanımlamalıyız. Şimdi
burada gerekmediği için tanımları yapmadık.

**Sıralama Alanı**

Sıralama kısmına yaparken bu alanı sırasız listeler ile yapmayı
düşündüm.

[sourcecode language="html"] \<div id="siralamAlani"\> \<ul\>
\<li\>\<strong\>Sıralama:\</strong\>\</li\> \<li\>\<a
href=""\>Karışık\</a\>\</li\> \<li\>\<a href=""\>Popüler\</a\>\</li\>
\<li\>\<a href=""\>Oley!\</a\>\</li\> \<li\>\<a href=""
class="secili"\>Alfabetik\</a\>\</li\> \<li\>\<a href=""\>En Çok
Tıklanan\</a\>\</li\> \<li\>\<a href=""\>En Son Eklenen\</a\>\</li\>
\</ul\> \</div\> [/sourcecode]

Dışına bir katman atamamın nedeni ardalan resmi ve diğer öğeler ile olan
ilişkileri ayarlamak içindir. Sıralama öğelerinden bir tanesine göre
sıralama yapılacak ve başındaki ok ikonu aşağı bakacağı için bu öğeye
bir sınıf tanımlıyorum diğerlerinden ayırmak için

[sourcecode language="css"] div\#siralamAlani{
background:url(../images/siralama\_ard.gif) 0 0 no-repeat; height:38px;}
div\#siralamAlani ul{padding:10px 0 0 10px} div\#siralamAlani ul
li{display:inline;} div\#siralamAlani ul li strong{display:block;
float:left; color:\#828282; font:bold 14px Arial, Helvetica, sans-serif;
margin-right:3px} div\#siralamAlani ul li a{display:block;
background:url(../images/genel\_resim.gif) right -388px no-repeat;
float:left; font:bold 14px Arial, Helvetica, sans-serif; color:\#0c2b90;
padding-right:15px; margin-right:10px} div\#siralamAlani ul li
a.secili{background:url(../images/genel\_resim.gif) right -354px
no-repeat;} [/sourcecode]

**Listeleme Tablosu**

Listeleme tablosunun bir kaç kolonu hariç ana sayfadaki tablodan bir
farkı yoktur. Benzer bir anlayış ile burayı kodlayalım.

[sourcecode language="css"] table.genelTablo{border-collapse:collapse; }
table.genelTablo th{font:bold 14px Arial, Helvetica, sans-serif;
color:\#000; padding:5px 2px; text-align:left} table.genelTablo
th.ortala{text-align:center} table.genelTablo tr.enAlt td{border:0}
table.genelTablo td{padding:1px 2px; font:14px Arial, Helvetica,
sans-serif; color:\#828282; border-bottom:1px solid \#d5d5d5;}
[/sourcecode]

Listeleme tablosunun ana sayfadan farklı olan kısmı en sağdaki oylama
gösterme alanı

[sourcecode language="html"]\<td\>\<p class="oley"\>\<strong
class="ucKupa"\>3 Kupa\</strong\>\</p\>\</td\>[/sourcecode]

Sadece oyu göstereceğimiz için bu şekilde kodladık.

[sourcecode language="css"] \#solOrtaAlan table td
p.oley{background:url(../images/genel\_resim.gif) 0 -483px no-repeat;
width:93px; height:21px; margin:0} table td p.oley strong{display:block;
background:url(../images/genel\_resim.gif) 0 -459px no-repeat;
text-indent:-9999px; height:21px} table td p.oley strong.birKupa{
width:18px;} table td p.oley strong.ikiKupa{ width:37px;} table td
p.oley strong.ucKupa{ width:56px;} table td p.oley strong.dortKupa{
width:75px;} table td p.oley strong.besKupa{ width:95px;} [/sourcecode]

\#solOrtaAlan table td p.oley tanımını niye p.oley şeklinde yapmıyoruzda
bu kadar uzun yapıyoruz derseniz, üstten gelen kalıtsal tanımlar alt
elemanları da etkiliyor bu etkiyi kaldırmak için bu şekilde tanımını
uzatarak bu tanımı daha etkin yapıyoruz. Konu hakkında detaylı bilgi
almak için [tıklayınız.][]

Ana sayfadaki tablo ile yapının aynısı olduğu için bu kadar anlatarak
tablo faslını geçiyorum ve sayfalama kısmının kodlamasını anlatmaya
başlıyorum.

**Sayfalama**

[Sayfalama kodlamalarını bir kaç tipi][] var ben burada daha önce
kodladığım bir kodu kopyalıyorum. Bu yöntemi seçmemde programcı
arkadaşım Mustafa'nın etkiside var.

[sourcecode language="html"] \<div class="sayfalama"\> \<ul\>
\<li\>\<span\>|&lt;\</span\>\</li\> \<li\>\<span\>Önceki\</span\>\</li\>
\<li\>\<span\>1\</span\>\</li\> \<li\>\<a href="\#"\>2\</a\>\</li\> \<li
\>\<a href="\#"\>3\</a\>\</li\> \<li \>\<a href="\#"\>4\</a\>\</li\>
\<li \>\<a href="\#"\>5\</a\>\</li\> \<li \>\<a
href="\#"\>6\</a\>\</li\> \<li \>\<a href="\#"\>7\</a\>\</li\> \<li
\>\<a href="\#"\>8\</a\>\</li\> \<li \>\<a href="\#"\>9\</a\>\</li\>
\<li \>\<a href="\#"\>10\</a\>\</li\> \<li \>\<a
href="\#"\>Sonraki\</a\>\</li\> \<li class="sayfalmaSonu"\>\<a
href="\#"\>&gt;|\</a\>\</li\> \</ul\> \</div\> [/sourcecode]

Sayısız listeler ile listelediğimiz sayfa sayılarının farklı bölümlerini
belirlemek için \<li\>\<span\>1\</span\>\</li\> şeklinde tanımlama
yapıyoruz. Normal bağlantılarıda \<li\>\<a href=""\>2\</a\>\</li\>
şeklinde tanımlıyoruz. CSS kodunu yazalım.

[sourcecode language="css"] /\* sayfalama \*/ div.sayfalama ul{margin:0
auto; width:530px; padding:10px 0 0 0; clear:left} div.sayfalama ul
li{font:bold 12px Tahoma, Geneva, sans-serif; color:\#fff; float:left;
list-style:none; margin:0 2px; background:\#80a3b7;} div.sayfalama ul li
span{padding:5px 8px; display:block} div.sayfalama ul li a{font:bold
12px Tahoma, Geneva, sans-serif ; color:\#80a3b7; text-decoration:none;
background-color:\#f0f0f0; padding:5px 8px; display:block} div.sayfalama
ul li a:hover{background-color:\#80a3b7; color:\#f0f0f0;} [/sourcecode]

**İçerik Alanı Sağ**

İçerik alanının sağ kısmı aslında pek bir şey içermiyor bir banner alanı
ve kategori listesi. Her iki alanda ana sayfada mevcut olduğu için aynı
kodları buraya taşıyoruz.

[sourcecode language="html"]\<div id="sagBannerAlani"\>\<img
src="images/band\_website\_banner.jpg" width="300" height="250"
alt="Web" /\>\</div\>[/sourcecode]

Sağ banner alanı diye ayrı bir isim vermemin nedeni, kodlaması aynı olsa
da site yayına girdikten sonra ana sayfa ve alt sayfaya farklı bannerlar
atanma ihtimali olduğu için buraya farklı bir isim veriyorum ve
tanımlamamı yapıyorum.

**Kategori Listeleme Alanı**

Kategori listeleme alanı da ana sayfa ile birebir aynıdır. Kodu aynen
taşıyorum. Bu tip modülleri kodlarken eğer esnek kodlar isek modül
nereye konursa konsun sorun çıkarmaz. Site kodlamaya başlanmadan önce bu
tip modülleri belirleyip sabit bir genişlik vermekten kaçınmalıyız.
Burada genişlikleri aynı olduğu için sorun çıkarmazdı zaten ama farklı
projeler için söylüyorum bunu, aklınızın bir kenarında bulunsun.

### Tezahürat Ekle Sayfasının Kodlanması

![Tezahürat Ekle][]

Sayfamızı incelediğimizde sol içerik alanında bir tezahürat ekleme
formunun diğer sayfadan farklı olduğunu görüyoruz.

Eskiden form alanlarını kodlarken tabloları kullanırdım daha rahat
gelirdi. Ancak listeler(ul) ve tanımlayıcı listeleri(dl dd dt)
kullanmaya başladıktan sonra artık tabloları kullanmıyorum.

Bu sayfadaki form yapıları iki kolonlu bir yapı olduğu için listeler ile
sayfa form yapısını oluşturabiliriz. Başlık ve altındaki paragrafı
ekliyoruz.

**Tezahürat Ekle Formunun Kodlanması**

Her satırın altında bir çizgi olduğu için her satırı bir katman içine
alıp bu katmanada bir sınıf tanılayarak bu işi çözebiliriz.

[sourcecode language="css"].formAlani{border-top:1px solid \#e0e0e0;
border-bottom:1px solid \#e0e0e0; padding:10px; margin:10px 0;
clear:left;}[/sourcecode]

clear:left; tanımı her satırın soldan başlaması için yapıldı.

İlk form alanı için bir label ve birde select alanımız var

[sourcecode language="html"]\<div class="formAlani"\>\<label\>Lig
Seçiniz:\</label\>\<select\>\<option\>--------------\</option\>\<option\>Turkcell
Süper Lig\</option\>\</select\>\</div\>[/sourcecode]

CSS kodunu yazalım

[sourcecode language="css"] .formAlani label{margin-right:10px;
width:135px; display:block; float:left;} .formAlani select{width:180px;
font:12px Arial, Helvetica, sans-serif;} [/sourcecode]

**Seçilen Ligdeki Takımlar Alanı**

Bu alanı kodlarken sayısız listeleri kullandım. Listelere bir genişlik
ve float tanımı yaparak yan yana dize bilirim. Genişlikleri verirken 3
tanesini yan yana duracak şekilde ayarladım.

[sourcecode language="html"] \<ul class="secilenLigler"\> \<li\> \<input
type="radio" name="takimSec" /\>\<div
class="logoTrabzon"\>Trabzon\</div\> \<label\>Trabzon Spor Klubü
Tesisleri\</label\>\</li\> \<li\> \<input type="radio" name="takimSec"
/\>\<div class="logoFenerbahce"\>Fenerbahçe\</div\>
\<label\>Fenerbahçe\</label\>\</li\> \<li\> \<input type="radio"
name="takimSec" /\>\<div class="logoAnkara"\>Ankaraspor\</div\>
\<label\>Ankaraspor\</label\>\</li\> ....... \</ul\> [/sourcecode]

CSS kodları

[sourcecode language="css"] ul.secilenLigler{width:575px; margin:0 auto}
ul.secilenLigler li{float:left; width:170px; margin:0 20px 10px 0;
color:\#828282;} ul.secilenLigler li div{float:left} ul.secilenLigler li
label{position:relative; top:8px} ul.secilenLigler li input{float:left;
position:relative; top:8px; margin-right:10px} [/sourcecode]

Her takım alanı için radyo butonu, logo için bir katman, takım adı için
bir label tanımladım ve bunları yan yana dizmek için float:left tanımı
kullandım. label ve input için kullandığım postion:relative tanımı ve
top değerleri bu öğeleri diğer öğeler ile yatayda aynı hizaya getirmek
içindir.

Yukarıda bahsettiğim gibi form alanlarını kodlarken sayısız
listeleri(ul) kullanıyorum burada da

[sourcecode language="html"] \<div class="formAlani"\> \<ul\>
\<li\>\<label\>Kategori
Seçiniz:\</label\>\<select\>\<option\>--------------\</option\>\<option\>Turkcell
Süper Lig\</option\>\</select\>\</li\> \<li\>\<label\>Tezahüratın
Adı:\</label\>\<input type="text" /\>\</li\> \<li\>\<label\>Youtube
linki:\</label\>\<input type="text" /\>\</li\>
\<li\>\<label\>Tezahüratın sözleri:\</label\>\</li\>
\<li\>\<textarea\>\</textarea\>\</li\> \<li\>\<label\>Kısa
tanıtım:\</label\>\<input type="text" /\>\</li\> \<li\>\<label
class="genisEtiket"\>Kayıtlı bir tezahüratınız varsa buradan
yükleyiniz:\</label\> \<input type="file" /\>\</li\> \</ul\> \</div\>
[/sourcecode]

CSS kodu

[sourcecode language="css"] .formAlani p{margin-bottom:10px} .formAlani
label{margin-right:10px; width:135px; display:block; float:left;}
.formAlani label.genisEtiket{width:310px} .formAlani
textarea{width:625px; height:210px; border:1px solid \#e8e8e8;
margin-top:8px; font:12px Arial, Helvetica, sans-serif; padding:3px;}
.formAlani ul li{margin-bottom:10px} .formAlani input{border:1px solid
\#e8e8e8; font:12px Arial, Helvetica, sans-serif; padding:3px;
width:300px} .formAlani select{width:180px; font:12px Arial, Helvetica,
sans-serif;} .formAlani select.darSelect{width:75px;} [/sourcecode]

Son olarakta gönder düğmesini koyuyorum.

[sourcecode language="html"]\<input type="button" value="Gönder"
class="gonderBut" /\>[/sourcecode]

CSS kodu

[sourcecode language="css"]input.gonderBut{width:170px; height:45px;
float:right; font:bold italic 24px Arial, Helvetica, sans-serif;
color:\#434343; cursor:pointer}[/sourcecode]

Böylece Tezahürat Ekle sayfamızı bitirmiş oluyoruz.

### Tezahürat Dinle Sayfasının Kodlaması

![Tezahürat İzle Dinle][]

Tezahürat dinle sayfası iki sekmeli bir yapıdan oluşuyor ve dinleme ve
izleme seçenekleri iki ayrı sekme içinde yer alıyor.

Başlık ve açıklama kısmını kodluyoruz. Başlık ve ilk paragraf bir önceki
sayfa ile aynı. Başlık yanındaki logo ve takım ismi kısmına biraz
değinelim.

[sourcecode language="html"]\<div id="dinleTakimi"\>\<div
class="logoTrabzon"\>Trabzon\</div\>
\<span\>Trabzon\</span\>[/sourcecode]

Logo için iki ayrı katman oluşturuyorum. Bunun nedeni logoların geneli
için bir sınıf tanımlıyorum. Ayrıca ikinci katmanda her bir takım için
tanımlanacak özellikler için. CSS kodunu yazarsak;

[sourcecode language="css"] div\#dinleTakimi{float:left; width:180px;
margin-left:20px; position:relative; top:-4px} div\#dinleTakimi
div{float:left;} div\#dinleTakimi span{ position:relative; bottom:-10px;
font:14px Arial, Helvetica, sans-serif; color:\#828282;
padding-left:6px} [/sourcecode]

Burada şöyle bir şey var. Başlığın uzunluğu belli olmadığı için sadece
logo ve takım adına float tanımı ve genişlik tanımı yaptık. Böylece
başlık uzunluğu ne olursa olsun başlık ve logo kısmı devamlı yan yana
duracaktır.

Sekmeleri kodlarken daha önce yazdığım [jquery ile sekme yapımını][]
anlattığım makaledeki gibi yapacağız.

[sourcecode language="javascript"] \<script type="text/javascript"
src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"\>\</script\>
\<script type="text/javascript"\> \$(document).ready(function() {
\$('div.sekmeAlani ul\#tezahuratSekme li a').not("div.sekmeAlani
ul\#tezahuratSekme li\#favEkle a, div.sekmeAlani ul\#tezahuratSekme
li.pasif a").click(function(){
\$(this).parent('li').addClass('normal').siblings().removeClass('normal');
var mevcutSinif = this.className.slice(0,2); \$('div.sekmeAlani \>
div').hide().filter('div.'+mevcutSinif).show(); }); \$('.sekmeAlani
ul\#tezahuratSekme li a:first').click(); }); \</script\> [/sourcecode]

Buradaki tek fark favoriler kısmını sekmeli yapının dışında tutmak için.
jquery'nin :not() fonksiyonunu kullandık. Bu fonksiyonun anlamı bu
elementlere uygula not fonksiyonu ile belirtilen elemana uygulamadır.

[sourcecode language="html"] \<div class="sekmeAlani"\> \<ul
id="tezahuratSekme" class="kapsayamamaSorunu"\> \<li class="s1
normal"\>\<a href="javascript:void(0);" class="s1 dinle"\>Tezahürat
Dinle\</a\>\</li\> \<li class="s2 pasif"\>\<a href="javascript:void(0);"
class="s2 izle"\>Tezahürat İzle\</a\>\</li\> \<li id="favEkle"\>\<a
href="javascript:void(0);" id="favorimedenCikar"\>Favorilerine
Ekle\</a\>\</li\> \</ul\> \<div class="s1"\> \<div
id="sesOynatici"\>\<img src="images/ses\_oynatici.gif" width="333"
height="50" alt="ses" /\>\</div\> \</div\> \<div class="s2"\> \<div
id="videoOynatici"\>\<img src="images/video\_player.gif" width="320"
height="260" alt="video" /\>\</div\> \</div\> \</div\> [/sourcecode]

CSS kodlarını yazarsak;

[sourcecode language="css"] ul\#tezahuratSekme{border-bottom:1px solid
\#ccc; padding-left:30px} ul\#tezahuratSekme li{float:left;
height:39px;} ul\#tezahuratSekme li a{display:block; padding:15px 45px 0
50px; color:\#000; font-size:14px} ul\#tezahuratSekme
li.normal{background:url(../images/normal\_seme\_ard.gif) 0 0 no-repeat;
} ul\#tezahuratSekme li.pasif{background:url(../images/sekme\_pasif.gif)
0 0 no-repeat; } ul\#tezahuratSekme li.pasif a{ cursor:default;}
ul\#tezahuratSekme li.normal a.dinle{
background:url(../images/tez\_din\_ikon.gif) 15px -220px no-repeat; }
ul\#tezahuratSekme li.normal a.izle{
background:url(../images/tez\_din\_ikon.gif) 15px -270px no-repeat;}
ul\#tezahuratSekme li{background:url(../images/kapali\_sekme.gif) 0 0
no-repeat;} ul\#tezahuratSekme li a.dinle{
background:url(../images/tez\_din\_ikon.gif) 15px -220px no-repeat;}
ul\#tezahuratSekme li a.izle{
background:url(../images/tez\_din\_ikon.gif) 15px -268px no-repeat;}
ul\#tezahuratSekme li\#favEkle{float:left; height:39px; background:none}
ul\#tezahuratSekme li\#favEkle
a{background:url(../images/tez\_din\_ikon.gif) 18px -318px no-repeat;}
ul\#tezahuratSekme li\#favEkle
a:hover{background:url(../images/tez\_din\_ikon.gif) 18px -419px
no-repeat;} ul\#tezahuratSekme li\#favEkle a\#favorimedenCikar,
ul\#tezahuratSekme li\#favEkle
a\#favorimedenCikar:hover{background:url(../images/tez\_din\_ikon.gif)
18px -368px no-repeat;} [/sourcecode]

**Tezahürat Bilgi Alanı**

Tezahürat bilgi alanında; ekleyen, kaç kez dinlendiği veya izlendiği,
paylaşım linki ve kaç kişinin oley çektiği bilgileri yan yana yer
alıyor.

Bu alanı bir katman içine alıp ardalan rengini bu katman veriyoruz.
İçine sol ve sağ kolonlar için iki katman oluşturup içerikleri buraya
koyuyoruz. İçerikleride bir paragraf içinde kodluyoruz.

[sourcecode language="html"] \<div id="tezahuratBilgi"
class="kapsayamamaSorunu"\> \<div id="tezahuratBilgiSol"\> \<p\>Ekleyen:
\<a href=""\>Hasan\</a\> \<span\>27 Ağustos 2009'da
Eklendi\</span\>\</p\> \<p\>Link Paylaş: \<input type="text"
value="htpp:www..ewrwerwerwerewrra" /\>\</p\> \</div\> \<div
id="tezahuratBilgiSag"\> \<p\>123.288 kez dinlendi\</p\>
\<p\>\<span\>16.258 kişi Oley! çekti!\</span\> \<ul
class='oleyCek'\>\<li class='mevcutOy' style="width:54px"\>3/5
Yıldız\</li\>\<li\>\<a href='\#' title='1 puan'
class='birYildiz'\>1\</a\>\</li\>\<li\>\<a href='\#' title='2 puan'
class='ikiYildiz'\>2\</a\>\</li\>\<li\>\<a href='\#' title='3 puan'
class='ucYildiz'\>3\</a\>\</li\>\<li\>\<a href='\#' title='4 puan'
class='dortYildiz'\>4\</a\>\</li\>\<li\>\<a href='\#' title='5puan'
class='besYildiz'\>5\</a\>\</li\>\</ul\>\</p\> \</div\> \</div\>
[/sourcecode]

CSS koduda şöyle olacak;

[sourcecode language="css"] \#tezahuratBilgi{margin:1px 0;
background-color:\#eee; padding:13px 10px 0 10px}
\#tezahuratBilgiSol{float:left; width:390px} \#tezahuratBilgiSol a{
color:\#0c2b90} \#tezahuratBilgiSol p{margin-bottom:10px}
\#tezahuratBilgiSol input{border:1px solid \#cbcbcb; font:14px Arial,
Helvetica, sans-serif; color:\#cccccc; width:200px}
\#tezahuratBilgiSag{float:left; width:240px} \#tezahuratBilgiSag
p{margin:0 0 15px 0} \#tezahuratBilgiSag p span{float:left;}
[/sourcecode]

Etiketler, Önce Söyle, Sonra Yorumla vb. başlıkların ikonlarını sprite
tekniği ile resimlerini hazırlayıp başlıkların başına ardalan resmi ile
koyuyoruz.

Etiketler için padding ve ardalan rengi tanımlıyoruz. hover hallerini
hazırlıyoruz.

[sourcecode language="css"] div\#etiketler a{padding:2px 4px;
background-color:\#eee; color:\#666; font-size:14px} div\#etiketler
a:hover{background-color:\#666; color:\#eee;} [/sourcecode]

**Önce Söyle**

Önce söyle başlığınıda diğer başlıklar gibi hazırlıyoruz. İçeriği
blockquote içine koydum. Aslında bunun için de bir katman açıp
koyabilirdik, tercih meselesi. Ardalan resmini sağ alta sabitliyoruz.

[sourcecode language="css"] blockquote.tezahuratMetni{ background:\#eee
url(../images/tezahurat\_zem.gif) right bottom no-repeat; padding:20px
50px 20px 30px; margin-bottom:1px; font-style:italic} [/sourcecode]

**Yorum Alanı**

Yorum alanın solda avatar'ın(küçük resim) ve sağda alt alta içeriklerin
bulunduğu iki kolonlu bir yapıya sahip .

float ve genişlik tanımlarını yaparak öğeleri yerleştiriyoruz. Burada
farklı durumda olan kısım yorum oylama kısmıdır. Yorum oylama kısmını
ayrı bir katman içine alıp yorum yazanın yanında durması için
position:relative ve float:left tanımı ile ile ayırıyoruz. Artı, eksi ve
puan kısmını bir liste şeklinde kodluyoruz.

Son olarakta "Sende Yaz" kısmını kodluyoruz. Başlığı yukarıdaki
başlıklar gibi yazıyoruz. Yorum yazma kısmına bir textarea yapıp
genişlik, yükseklik ve kenar çizgisi tanımlarını yapıyoruz.

[sourcecode language="css"] div.yorumalani{border-bottom:1px solid
\#e0e0e0; margin-bottom:12px} div.yAvatar{float:left; width:60px}
div.yorumAlaniSag{float:left; width:590px} div.yorumAlaniSag
strong{color:\#a1a1a1; display:block; clear:left; margin:10px 0 5px 0}
\#solOrtaAlan div.yorumAlaniSag p{margin-bottom:10px}
div.yorumYazari{float:left; font-weight:bold;} div.yorumYazari
a{color:\#2a459d} div.comment-rate{float:left; width:75px;
margin-left:20px; position:relative;} div.comment-rate-num{float: left;
padding-right: 5px; color:\#088f02; font-weight:bold;}
ul.yorumOyla{float:left; width:75px; margin-left:20px;
position:relative; top:-5px;} ul.yorumOyla li{float:left;} li.yorumArti
a{ background:url(../images/genel\_resim.gif) -15px -530px no-repeat;
display:block; text-indent:-9999px; width:16px; height:20px}
li.yorumEksi a{ background:url(../images/genel\_resim.gif) 0 -530px
no-repeat; display:block; text-indent:-9999px; width:16px; height:20px}
li.olumlu{color:\#088f02; font-weight:bold;} li.olumsuz{color:\#c00;
font-weight:bold;} li.notr{color:\#000; font-weight:bold;}
h3.senYaz{background:url(../images/tez\_din\_ikon.gif) 0 -168px
no-repeat; padding:15px 0 3px 32px} \#solOrtaAlan textarea{border:1px
solid \#e1e1e1; width:642px; margin-bottom:20px; height:100px}
[/sourcecode]

Tezahürat Dinle/İzle sayfasınıda tamamlamış oluyoruz.

### Site Genel Şablonu Sayfasının Kodlanması

![Genel Şablon][]

Site kodlarken site içerisinde genelde bir şablon sayfası oluşturulur.
Bu sayfa site içinde olabilmesi mümkün elemanların bulunduğu bir
sayfadır. Tasarımcı bu sayfayı daha sonra eklenmesi durumunda
hazırlayarak sitenin gelişmesi durumlarınıda düşünmüş olur. Böyle site
yapısından kopmamış oluruz.

Fanatikmarşlar.com'un şablon sayfası biraz daha sade oldu. Normalde
paragraflar, tablo yapısı, resimler, listeler, vb. yapıları içerir.

Fanatikmarşlar.com'un şablon sayfasına baktığımızda başlık, paragraf ve
uyarı mesajları şeklinde oluşmaktadır.

[sourcecode language="css"] \#anaKapsul h1.hata{color:\#e40000}
\#anaKapsul h1.onay{color:\#1f6600} [/sourcecode]

Bilgi kutusunu oluştururken yuvarlak kenarlı olduğu için, iki elamana
ihtiyaç var. Bunun için kapsayıcı div ve içine paragrafa koyduk.

[sourcecode language="html"] \<div class="bilgiKutusu"\>
\<p\>\<strong\>Bu kullanıcı adı zaten alınmış, başka bir tane deneyin.
\</strong\>\</p\> \</div\> [/sourcecode]

CSS Kodları

[sourcecode language="css"] div.bilgiKutusu{ background:\#2d2d2d
url(../images/bilgi\_kutusu.gif) 0 0 no-repeat; margin-bottom:20px;
font:bold 14px Arial, Helvetica, sans-serif; color:\#fff}
div.bilgiKutusu p{background:url(../images/bilgi\_kutusu.gif) -650px
bottom no-repeat; padding:10px;} div.bilgiKutusu p
strong{color:\#ffc000} [/sourcecode]

Alt sayfaların kodlamasını böylelikle bitirdik. Site kodlarken değişik
tasarımlarda olsa genelde benzer yapılar olduğu için yaklaşık olarak
kodlarımız bu şekilde olacaktır.

### Sonuç

Site kodlarken kodlarımı Adobe Dreamweaver ile yazıyorum. Kodlamanın bir
çok yerinde FireBug kullanıyorum, daha doğrusu firebug'ı kapatmıyorum.
Ayrıca test amaçlı ietester programını kullandım. Daima ie6'da test
ettim.

Site kodlarken bir çok yöntem kullanılabilir. Ben kodlarımı yazarken
devamlı bu alanı kodlarken nasıl daha iyi kodlarım, ileriye yönelik
değişikliklerde nasıl sorun yaşamam, arama motorları standartlarına
nasıl uyarım düşüncesi ile kodluyorum. Yazdığım kodlara genellikle daha
sonra baktığımda beğenmiyorum. Devamlı en iyi hedefleyince eski
kodlarımı beğenmiyorum. Bence olması gereken bu çünkü sektör daima
kendini yeniliyor ve yeni özellikler çıkıyor biz devamlı bunları takip
edip yeni projelerimizde kullanmalıyız.

Çok uzun süredir tasarladığım ama ancak nasip olan bir işi bitirmenin
sevinci ile bu makalemide bitiriyorum. Daha güzel makalelerde buluşmak
dileğiyle kendinize iyi bakın.

Projede yer alan tüm dosyaları sıkıştırıp attım. [Tüm dosyaları indirmek
için tıklayınız.][]

</p>

  [Marşlar]: http://www.fatihhayrioglu.com/images/marslar_kucuk.jpg
  [Tezahürat Ekle]: http://www.fatihhayrioglu.com/images/tezahurat_ekle_kucuk.jpg
  [Tezahürat İzle Dinle]: http://www.fatihhayrioglu.com/images/tezahurat_izle_dinle_kucuk.jpg
  [Genel Şablon]: http://www.fatihhayrioglu.com/images/genel_sablon_kucuk.jpg
  [IE'da İkikat görülen Margin Problemi ve Çözümü]: http://www.fatihhayrioglu.com/ieda-ikikat-gorulen-margin-problemi-ve-cozumu/
  [tıklayınız.]: http://www.fatihhayrioglu.com/cssde-tanimlamalar-ve-etkinliklerispecificity/
  [Sayfalama kodlamalarını bir kaç tipi]: http://www.fatihhayrioglu.com/css-ile-sayfalama-gorselligini-ayarlama/
  [jquery ile sekme yapımını]: http://www.fatihhayrioglu.com/jquery-ile-basit-sekme-yapimi/
  [Tüm dosyaları indirmek için tıklayınız.]: http://www.fatihhayrioglu.com/dokumanlar/fm_htmlleri_son.rar
