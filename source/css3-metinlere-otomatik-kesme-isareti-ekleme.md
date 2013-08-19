Title: CSS3 ile Kısa Çizgi(tire) Ekleme
Date: 2013-08-13 15:00
Category: CSS
Tags: kısa-çizgi, tire, css3

Kısa çizginin(-) tanımına internette baktığımızda kullanım alanlarının başında ilk sırada 

"Satır sonunda, yer kalmadığı için yarım kalan kelimelerin bölünmüş olduğunu, yani devamının altta olduğunu göstermek için satır sonunda kullanılır. Bu görevde kullanılınca birleştirme çizgisi denir."

Bilgisi yer alır. Bu işi web mecrasında yapmak için CSS3 ile gelen hyphens(kısa çizgi) özelliği kullanılır. Şimdi bu makalede bu özelliği inceleyeceğiz.

CSS kısa çizgi özelliği bir satıra sığmayan kelimenin nasıl bölüneceğini belirler. Bu bölme işini HTML’de tanımlana **lang** özniteliğinde belirtilen dile göre yapar. 

**Yapısı:** hyphens: &lt;deger&gt;   
**Aldığı Değerler:** none | manual | auto   
**Başlangıç Değeri:** manual   
**Uygulanabilen Elementler:** Tüm elementler   
**Kalıtsallık:** var
{: .cssozelliktanimi}

Değerlerini inceleyelim.

* **none:** Satır sonuna sığmayan kelime tire ile ayrılmaz. Sadece boşluk olan bölümlerden satır başı yaptırılır.
* **manual:** Kelimeler satıra sığmadığında sadece kelime içinde tire geçiyorsa ise tireli olan kısımdan kesilir. &shy; karakterini tire konacak yere koymamız gerekiyor. Normalde gözükmüyor ama kelime kesildiğinde tire gözüküyor.
* **auto:** Kelimeler satırsa sığmadığında tarayıcı tarafından otomatik olarak HTML’de belirtilen dile göre bölünür. 

Bir örnek yapalım.

<iframe scrolling="no" height="150" frameborder="0" style="width: 100%; overflow: hidden;" allowtransparency="true" data-height="150" src="http://codepen.io/fatihhayri/embed/DEHAm?type=result&amp;height=250" id="cp_embed_hgplm"></iframe>

![kesik çizgi](https://lh5.googleusercontent.com/dLphRC85oPKym9mntIkeU3TRd98fz7oKiq-M1IRVHtPp3u3-OjKHKfuBttoH8gq0NCEqnBxUhBR_ge5rdaKA9gKJXpglfkzdHbMHbTd6GK4tGOuK8qc923bL2A)

Firefox’da denedim çalışıyor. Gayetde güzel çalışıyor. Unutulmaması gereken şey dil tanımının yapılması. Chrome’da auto çalışmıyor.

**Tarayıcı Desteği**   
Google Chrome 29+ (-webkit öneki ile **auto** hariç)   
Safari 5.1+ (-webkit öneki ile)   
Firefox6+ (-moz öneki ile)   
Opera desteklemiyor   
İnternet Explorer10+ (-ms öneki ile)   
**Mobil Tarayıcılar**   
Android desteklemiyor   
Opera Mobile desteklemiyor   
Safari Mobile 4.2(-webkit öneki ile)
{: .tarayiciuyum}

## Kaynaklar

* [https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens](https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens)
* [http://drublic.de/blog/css3-auto-hyphenation-for-text-elements/](http://drublic.de/blog/css3-auto-hyphenation-for-text-elements/)
* [http://www.hongkiat.com/blog/css3-hyphenation/](http://www.hongkiat.com/blog/css3-hyphenation/)
* [http://www.turkceciler.com/kisa-cizgi.html](http://www.turkceciler.com/kisa-cizgi.html) 
* [http://caniuse.com/#search=hyphens](http://caniuse.com/#search=hyphens)
