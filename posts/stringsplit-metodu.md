Title: String.split() Metodu
Date: 2006-12-22 14:34
Category: Javascript
Tags: Javascript, regular-expression, split, String.split()-Metodu

Split metodu, uygulandığı string'i parçalara böler ve bu parçaları bir
diziye(array) atar. <!--more-->

<div class="cssozelliktanimi">
**Web Tarayıcı Uyumu :** ECMAScript 2, JavaScript 1.1, JScript 3.0,
Internet Explorer 4.0, Netscape 3.0, Opera 3.0  
**Değer Tipi :** Dizi nesnesi   
**Javascript Sözdizimi:** ilkDeyim.**split**(aKalip)  
                                 ilkDeyim.**split**(aAyrac)  
                                 ilkDeyim.**split**(aAyrac, aSay)  
**Tanımlar:** aKalip - string'i bölmek için kullanılan regular
expression kalıbı   
                aAyrac - string'i bölmek için kullanılan ayraç  
                aSay - bölümlerin limitini belirler

</div>
  
Bu metod **join()** metodu ile birlikte tamamlayıcı bir unsur olarak
kullanılabilir.

Javascript 1.2 ile birlikte regular expression kullanımı da eklenmiştir.

![][]

[sourcecode language="css"] ilkDeyim = " Merhaba dünya ben geldim. ";
bolme = ilkDeyim.split(" ", 3); document.write(bolme) [/sourcecode]

sonuç aşağıdaki gibi olacaktır.

[sourcecode language="css"] ["Merhaba", "dünya", "ben"] [/sourcecode]

Bir tane de regular expression kullanarak örnek yaparsak.

[sourcecode language="html"] <html> <head> </head> <body>
<script> sayiRegExp = new RegExp("[0-9]", "g"); ilkDeyim =
"A0B1C2D3E4F5G"; harfDizi = ilkDeyim.split(sayiRegExp); for(i=0; i <
harfDizi.length; i++) { document.write(harfDizi[i]);
document.write("<br/>"); } </script> </body> </html>
[/sourcecode]

Yukarıdaki kodun sonucunda aşağıdaki gibi olacaktır.

[sourcecode language="html"] A B C D E F G [/sourcecode]

</p>

  []: /dokumanlar/split.gif
