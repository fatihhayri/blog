Title: javascript ile resimlerin ön belleğe alınmasını engellemek
Date: 2006-10-12 11:12
Category: Javascript
Tags: Caching, Javascript, math, Ön-bellek, radom, resimler

[sourcecode language="javascript"] document.write("\<img
src=\\"resim.gif?" + Math.random() + "\\" /\>"); [/sourcecode] Bu kodu
uyguladığımız resimler web tarayıcısının ön belleğine alınmayacaktır.
Çünkü Math.radom ile elde ettiğimiz değer devamlı değişecektir ve
resmimiz ön belleğe alınmayacaktır. Bu kodu ön belleğe eklenmesini
istemediğimiz resimler için kullanabiliriz.
