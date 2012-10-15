Title: javascript ile kullanıcıdan teyit almak
Date: 2006-10-13 11:02
Category: Javascript
Tags: confirm, evet, Javascript, teyit-almak

Bazen kullanıcıdan bir iş için teyit almak durumunda kalırız, böyle
durumlarda **confirm** komutu işe yarar.

[sourcecode language="html"] \<a href="sil.aspx" onclick="return
window.confirm('Silmek istediğinize eminmisiniz?');"\>Bu kayıdı
Sil\</a\> [/sourcecode]

Yukarıdaki kod da kullanıcının karşısına evet/hayır seçeneklerinin
olduğu bir onay popup'ı gelecektir, kullanıcı burada evet'i seçerse bize
true değeri hayır'ı seçerse false değeri gelecektir. Örnekte eğer evet
seçilirse kayıt silme işleminin yapıalcağı sayfaya giderek kaydı
silecek, ama hayır seçilirse herhangibir işlem yapılmayacaktır.

</p>

