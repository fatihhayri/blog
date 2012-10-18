Title: CSS ile Erişilebilir Formlar Yapmak - II
Date: 2007-03-06 00:10
Category: CSS, Web Standartları, XHTML
Tags: CSS, Web Standartları, XHTML

![][] [sayfanın çıktısını al][] || ![][1] [pdf olarak indir][]

###### Gelişmiş Form Yapıları

Gelişmiş yapılı formlarda tablo kullanmak daha kolayımıza geliyor. Ancak
burada bir sorunumuz varki formlar veri içeren tablolar değildir ve
doğru kodlama için form yapılarını oluştururken tablo kullanmak web
standartlarına uygun değildir.

Biz burada daha karışık yapılı bir formu nasıl tablo kullanmadan planlar
ve güzelleştiririz onu anlatmaya çalışacağız. Tabi bu kodlamanın bazı
zorlukları olacaktır ama genel yapı anlaşılırsa yapılamayacak form
kodlaması yoktur. Aşağıda kodlayacağımız formun resmini görüyoruz.
<!--more-->

[![CSS ile Form][]][]

Kodlamayı yaparken dikkat edeceğiz konu kullanıcıyı yormayan güzel
görünümlü ve erişilebilirliği yüksek formlar hazırlamaktır. [Bir önceki][] yazımızda **fieldset** ve **legend** ve **label**
etiketlerinden bahsettiğimiz için burada bu etiketler hakkında tekrar
bir bilgi vermeyeceğiz. Diğer makalelerden farklı olarak bu makalede tüm
kodları verip sonra açıklamalarını yapacağız, bunun nedeni form
alanlarına ait tanımların bir çoğunun genel tanımlama olması ve bir
tanımın bir çok etiketi etkilemesidir. XHTML Kodumuzu yazalım:

1.  <form action="gonder.html" method="post" id="formset">  
2.  <fieldset>   
3.  <legend>Genel Bilgiler</legend>  
4.  <label class="adAlani">Ad <em>&#42;</em>  
5.  <input name="ad" type="text" id="ad" value="" />  
6.  </label>  
7.  <label class="soyadAlani">Soyad <em>&#42;</em>  
8.  <input name="soyad" type="text" id="soyad" value="" />  
9.  </label>  
10. <label class="adresAlani">Ev Adresi <em>&#42;</em>  
11. <input name="adres" type="text" id="adres" value="" />  
12. </label>  
13. <label class="sehirAlani">Şehir <em>&#42;</em>  
14. <input name="sehir" type="text" id="sehir" value="" />  
15. </label>  
16. <label class="postakoduAlani">Posta Kodu <em>&#42;</em>  
17. <input name="postakodu" type="text" id="postakodu" value="" />
18. </label>   
19. <label class="epostaAlani hata">Eposta &#42;  
20. <input name="eposta" type="text" id="eposta" value="" class="hata"
    />  
21. </label>  
22. <label class="telAlani">Telefon<input name="tel" type="text"
    id="tel" value="" />  
23. </label>  
24. </fieldset>  
25. <fieldset>  
26. <legend>Konu <em>&#42;</em></legend>  
27. <input id="radiobutton_1" type="radio" name="radiobutton_type"
    value="" />  
28. <label class="konuRadyoButon" for="radiobutton_1">Lorem ipsum
    dolor sit amet, consectetuer adipiscing elit. </label>  
29. <input id="radiobutton_2" type="radio" name="radiobutton_type"
    value="" />  
30. <label class="konuRadyoButon" for="radiobutton_2">Cras diam.
    Suspendisse potenti. In dictum bibendum est. Aliquam semper. Sed vel
    massa. Praesent imperdiet nisi eget lacus. </label>  
31. <input id="radiobutton_3" type="radio" name="radiobutton_type"
    value="" />  
32. <label class="konuRadyoButon" for="radiobutton_3">Phasellus quis
    enim. </label>  
33. <input id="radiobutton_4" type="radio" name="radiobutton_type"
    value="" />  
34. <label class="konuRadyoButon" for="radiobutton_4">Vestibulum ut
    lectus ac leo luctus aliquam. </label>  
35. </fieldset>  
36. <fieldset>  
37. <legend>Düşünceleriniz</legend>   
38. <label class="aciklamaAlani">Düşüncelerinizi aşağıdaki alana
    yazınız.<br /><textarea name="describe" cols="35"
    rows="5"></textarea>  
39. </label>  
40. </fieldset>  
41. <fieldset>  
42. <legend>Onay Alanı</legend>  
43. <input id="checkbox_1" type="checkbox" name="kabul" value="y"
    /><label for="checkbox_1" class="onayAlaniIsaretKutusu">Site
    kurallarını kabul ediyorum.</label>  
44. <input id="checkbox_2" type="checkbox" name="kabul" value="y"
    /><label for="checkbox_2" class="onayAlaniIsaretKutusu">Site
    kurallarını kabul etmiyorum.</label>  
45. </fieldset>  
46. <blockquote><strong>Not:</strong> Yanında (<em>*</em>)
    işareti olanlar zorunlu alanlardır.</blockquote>  
47. <input type="submit" name="submit" value="GÖNDER"
    class="formbutton" />   
48. </form>

Yukarıdaki kodlama aslında bir çok açıdan basit yapılı formalara
benziyor. "Bir çok karmaşık yapı basit yapıların birleşiminden oluşur"
genel kabulü tam durumumuzu açıklayan cümle. Bu kodlamanın farkı normal
akış dışına çıkacak(yani iki kolonlu olacak yerlerde) elementlere id
tanımı yaparak konumlandırma işlemi yapmaktır. Şimdi sıra CSS kodunu
yazmaya geldi.

1.  /* genel stiller */
2.  * {  
3.  margin: 0;  
4.  padding: 0;  
5.  }
6.  body {  
7.  font: 12px/14px Arial, Helvetica, sans-serif;  
8.  background-color:#07A;  
9.  text-align: center;  
10. margin:20px 0;
11. }
12. /* form stilleri */
13. form#formset {  
14. width: 360px;  
15. margin: 0 auto;  
16. text-align: left;  
17. color:#fff;
18. }
19. form#formset fieldset {  
20. margin: 0 0 1em 0;  
21. padding: 1.5em 1.5em 0 1.5em;
22. border: #DDD 1px solid;  
23. }
24. form#formset fieldset legend {  
25. font-weight: bold;  
26. color: #fff;  
27. padding:0 0.5em;  
28. }
29. form#formset label {  
30. display: block;  
31. width: 290px;  
32. font-size: 12px;  
33. line-height: 14px;  
34. padding: 0px 0px 12px 0px;  
35. }
36. form#formset fieldset input {  
37. display: block;  
38. margin-top: 3px;  
39. border:1px solid #fff;  
40. border-left:5px solid #fff;  
41. background-color:#09c;  
42. color:#ffc;  
43. }
44. form#formset label.adAlani, form#formset label.adresAlani,
    form#formset label.sehirAlani, form#formset label.epostaAlani {  
45. clear: left;  
46. }
47. form#formset label.adAlani, form#formset label.soyadAlani,
    form#formset label.sehirAlani, form#formset label.epostaAlani,
    form#formset label.telAlani {  
48. float: left;  
49. margin: 0px 10px 0px 0px;  
50. width: 150px;  
51. }
52. form#formset label.adAlani input, form#formset label.soyadAlani
    input, form#formset label.epostaAlani input, form#formset
    label.sehirAlani input, form#formset label.telAlani input {  
53. float: left;  
54. width: 150px;  
55. padding: 0px;  
56. }
57. form#formset label.postakoduAlani {  
58. float: left;  
59. width: 80px;  
60. }
61. form#formset label.postakoduAlani input {  
62. float: left;  
63. width: 80px;  
64. }
65. form#formset label.adresAlani {  
66. float: left;  
67. width: 310px;  
68. margin: 0px 0px 0px 0px;  
69. }
70. form#formset label.adresAlani input {  
71. float: left;  
72. width: 310px;  
73. padding: 0px;  
74. }
75. form#formset fieldset input#radiobutton_1, form#formset fieldset
    input#radiobutton_2, form#formset fieldset input#radiobutton_3,
    form#formset fieldset input#radiobutton_4 {  
76. clear: left;  
77. float: left;  
78. padding: 0px;  
79. border:0;  
80. margin: 0px 0px 0px 0px;  
81. background-color:#07a;  
82. }
83. form#formset label.konuRadyoButon {  
84. clear: none;  
85. margin: 0px 0px 0px 25px;  
86. padding: 0px 0px 15px 0px;  
87. }
88. form#formset fieldset input#checkbox_1, form#formset fieldset
    input#checkbox_2, form#formset fieldset input#checkbox_3 {  
89. clear: both;  
90. float: left;  
91. padding: 0px;  
92. margin: 0px;  
93. border:0;  
94. background-color:#07a;  
95. }
96. form#formset label.onayAlaniIsaretKutusu {  
97. clear: none;  
98. margin: 0px 0px 0px 25px;  
99. padding: 0px 0px 15px 0px;  
100. }
101. form#formset textarea {  
102. display: block;  
103. margin-top: 3px;  
104. border:1px solid #fff;  
105. border-left:5px solid #fff;  
106. background-color:#09c;  
107. color:#ffc;  
108. }
109. form#formset blockquote{  
110. margin-bottom:10px;  
111. }
112. form#formset fieldset em, form#formset blockquote em{  
113. color:#ff0;  
114. }

Yukarıdaki kodlamada önemli görülen tanımları biraz daha açıklamaya
çalışalım:

-   Genel Seçicisi (***{}**) kullanarak tüm elementlerin margin ve
    padding'lerini sıfırlıyoruz, böylece tüm elementler için ayrıca bu
    tanımı yapmaya gerek duymuyoruz(özel durumlar hariç.)
-   **body** seçicisine atadığımız özelikler sayfayı ortalamak için
    **text-align** tanımı yapıldı.
-   **form#formset** şeklinde forma id vermemizin nedeni sayfa içinde
    eğer birden fazla form olursa veya sitede genel bir css dosyası
    kullanıyorsak diğer formları etkilememek. Burada yapılan tanımlar
    genel tanımlardır.
-   <span class="alternatifard">**form#formset fieldset**</span>
    tanımında form alanlarını bir çerçeve içine aldık ve içerikle
    kenarlık arasına boşluk koyduk. Her bölümü ayrı çerçeveye almamızın
    nedeni bölümler arasındaki farka vurgu yapmaktır.
-   **form#formset fieldset legend** genel tanımı ile form bölümlerinin
    başlıklarına genel tanımlama yaptık.
-   <span class="alternatifard">**form#formset label**</span>
    tanımlaması ile formdaki tüm label'lar düşünülerek genişlik ve
    mesafe tanımları yapılmıştır.
-   **form#formset fieldset input** tanımlaması ile genel kullanıcı
    girişi(input) görünüm yerine kendi görünümümüze uygun tanımlar
    yapılmıştır.
-   **form#formset label.adAlani, form#formset label.adresAlani,
    form#formset label.sehirAlani, form#formset label.epostaAlani**
    seçicilerine **clear:left** tanımı yapılarak bu sınıflara ait
    alanları formun soluna yerleştiriyoruz.
-   Daha sonra Formun **Genel Bilgiler** kısmı içindeki form
    elementlerine genişlik ve float tanımı yapılıyor. Aynı şekilde
    kullanıcı girişlerinede(input) aynı tanımlar yapılıyor.
-   **57 - 74** satırları arasında Genel Bilgi Alanındaki diğer
    alanlardan farklı olan Ev adresi ve Posta Kodu alanlarına özel
    tanımlamalar yapılıyor. Genelde css kodlarken başta genel tanımalar
    yapılır sonra genelden farklı olan özel tanımlamalar yapılır.
-   **75 - 87** satırları arasında Form alanının **Konu** kısmı
    içeriğindeki radyo butonları ve içerik kısımlarına ait konumlandırma
    ve mesafe değerleri tanımlanmıştır.
-   **88 - 99** satırları arasında Form alanının **Onay** kısmı
    içeriğindeki işaret kutuları ve içerik kısımlarına ait konumlandırma
    ve mesafe değerleri tanımlanmıştır.
-   <span class="alternatifard">**form#formset textarea**</span>
    tanımlaması ile düşüncelerimiz alanı içindeki metin alanı tanımları
    girilmiştir.
-   Genelde forumlar oluşturulurken kullanıcıdan bazı alanların zorunlu
    doldurulması istenir. Bunu için
    <span class="alternatifard">**form#formset blockquote**</span>
    tanımlaması yapılmıştır.

Yukarıda gelişmiş form kodlamasını gördük son olarak formda doldurulması
gereken bir alanın doldurulmaması halinde çıkacak uyarı mesajı ve
bilginin girilmesi gereken alanın kullanıcının daha kolay görmesi için
stil tanımını yapalım. XHTML kodunu başına

1.  <div class="hata">
2.  Dikkat aşağıda sarı renk ile belirtilen yerlerde hata var.
3.  </div>

tanımlaması ve hataya neden olan alana(mesela e-posta girilmemiş olsun)
sınıf tanımlaması ekleyelim.

1.  <label class="epostaAlani **hata**">Eposta &#42;
2.  <input name="eposta" type="text" id="eposta" value=""
    **class="hata"** />

CSS kodunu ekleyelim

1.  form#formset fieldset input.hata {  
2.  display: block;  
3.  margin-top: 3px;  
4.  border:1px solid #ff0;  
5.  border-left:5px solid #ff0;  
6.  background-color:#ccc;  
7.  color:#ffc;  
8.  }
9.  form#formset fieldset label.hata {  
10. color:#ff0;  
11. font-weight:bold;  
12. }
13. div.hata {
14. background:#FFFFCC url(images/hata.png) no-repeat scroll 5px;
15. border:1px solid #FFCC66;
16. margin:0pt 0pt 10px;
17. padding:5px 10px 5px 35px;
18. color:#000;
19. }

Hata mesajının yanına bir ünlem ikonu koyduk ve farklı zemin rengi ve
kenarlığı ile kullanıcının dikkatini buraya çektik. Ayrıca hatanın
meydana geldiği alanı sarı renk ile tanımlayarak daha dikkat çekici
yaptık. Dikkat ederseniz amaç devamlı kullanıcıya formumuzu daha
anlaşılabilir ve kolay erişilebilir yapmak.

En son gönder butonunun css kodunu yazalım.

1.  .formbutton{  
2.  cursor:pointer;  
3.  border:0;
4.  background:#999;  
5.  color:#666;  
6.  font-weight:bold;  
7.  padding: 1px 2px;  
8.  background:url(images/buton_bg2.gif) repeat-x left top;  
9.  }

Buton zeminine degrade 1px genişliğinde bir resim koyarak hoş görünümlü
bir buton elde ettik.

Sonuç sayfasını görmek için [tıklayınız.][]

Aşağıda kaynaklar kısmında da erişebileceğiniz bir çok form stilleri ve
tasarımları mevcut göz atmanızı öneririm. Amaç web standartlarına uygun
ve kullanıcı taraflı formlar yapmak. Kodlama aşağıdaki web
tarayıcılarında test edilmiştir.

-   Firefox 1.0 +
-   Internet Explorer 5.5 +
-   Opera 7.54 +

<div class="ekstrabilgi">
**Not:** Görünümde Firefox ve Internet Explorer arasında ufak
farklılıklar mevcut, bu farklılıkların çok ufak olması nedeni ile bir
düzeltme kodu(fix) yazma gereği duymadık.

</div>
###### Kaynaklar

-   [http://www.webcredible.co.uk][]
-   [http://www.websiteoptimization.com/][]
-   [http://www.picment.com/][]
-   [http://www.dynamicdrive.com/][]
-   [http://www.cssplay.co.uk/][]
-   [http://www.456bereastreet.com/][]
-   [http://www.smashingmagazine.com/][]
-   [http://www.skyrocket.be/][]
-   [http://www.subtraction.com/][]
-   [http://www.stuffandnonsense.co.uk/][]
-   [http://paularmstrongdesigns.com/][]
-   [http://nidahas.com/][]
-   [http://www.alistapart.com/][]
-   [http://www.roscripts.com/][]

</p>

  []: /images/yazici_ikon.gif
  [sayfanın çıktısını al]: javascript:print()
  [1]: /images/pdf_ikon.gif
  [pdf olarak indir]: /pdf/CSS_ile_Erisilebilir_Formlar_Yapmak_II.pdf
  [CSS ile Form]: http://www.fatihhayrioglu.com/wp-content/sonuc_sayfasi.kucukresim.gif
  [![CSS ile Form][]]: http://www.fatihhayrioglu.com/wp-content/sonuc_sayfasi.gif
    "CSS ile Form"
  [Bir önceki]: http://www.fatihhayrioglu.com/?p=276
  [tıklayınız.]: /dokumanlar/css_ile_form_2.html
  [http://www.webcredible.co.uk]: http://www.webcredible.co.uk/user-friendly-resources/css/css-forms.shtml
  [http://www.websiteoptimization.com/]: http://www.websiteoptimization.com/speed/tweak/forms/
  [http://www.picment.com/]: http://www.picment.com/articles/css/funwithforms/
  [http://www.dynamicdrive.com/]: http://www.dynamicdrive.com/style/csslibrary/category/C6/
  [http://www.cssplay.co.uk/]: http://www.cssplay.co.uk/menu/form.html
  [http://www.456bereastreet.com/]: http://www.456bereastreet.com/archive/200701/styling_form_controls_with_css_revisited/
  [http://www.smashingmagazine.com/]: http://www.smashingmagazine.com/2006/11/11/css-based-forms-modern-solutions/
  [http://www.skyrocket.be/]: http://www.skyrocket.be/2006/01/09/semantic-horizontal-forms/
  [http://www.subtraction.com/]: http://www.subtraction.com/archives/2005/0822_free_form_fo.php
  [http://www.stuffandnonsense.co.uk/]: http://www.stuffandnonsense.co.uk/archives/trimming_form_fields.html
  [http://paularmstrongdesigns.com/]: http://paularmstrongdesigns.com/projects/awesomeform//
  [http://nidahas.com/]: http://nidahas.com/2006/01/12/forms-markup-and-css/
  [http://www.alistapart.com/]: http://www.alistapart.com/articles/prettyaccessibleforms
  [http://www.roscripts.com/]: http://www.roscripts.com/Tableless_forms-112.html
