Title: Statik sayfalarda yönlendirme
Date: 2006-10-10 15:04
Category: Javascript, XHTML
Tags: Javascript, location.href, meta, XHTML, yönlendirme

Statik sayfalarda yönlendirme için javascript ve xhtml kullanırız.
Javascript'in **location.href** özelliği bize mevcut sayfa URL'sine
yazma ve okuma izni verir. Bir çok uygulamada kullanılabileceğimiz güzel
bir özelliktir bu. Örneğin yönlendirme için kullanalıbilir. Kodumuzu
yazarsak:

[sourcecode language="javascript"]<script>location.href =
"DigerSayfa.html";</script>[/sourcecode]

Ayrıca xhtml ile de bu işi yapabiliriz.

[sourcecode language="html"] <head> <meta http-equiv="Refresh"
content="5; URL=DigerSayfa.html" /> </head> [/sourcecode]

Burdaki **5** değeri web tarayıcısının yönlendirmeden önceki beklediği
değeri gösterir. Değer saniye cinsindendir.

Eğer yönlendirme yapayım ama geri tuşuna basınca önceki sayfaya gitmesin
diyorsak **location.replace** özelliğini kullanmalıyız.

[sourcecode
language="javascript"]<script>location.replace("DigerSayfa.html");</script>[/sourcecode]

</p>

