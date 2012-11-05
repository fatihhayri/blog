Title: CSS Sınıflandırma-Liste Özellikleri
Date: 2006-08-03 00:07
Category: CSS
Tags: CSS, display, list-style, list-style-image, list-style-position, list-style-type, white-space

Liste özelliği ilk olarak listeleme amaçlı kullanılsa da şimdilerde menü
yapımında kullanımı revaçtadır. Burada liste özellikleri yanısıra
display ve white-space özelliklerinden de bahsedilecektir. <!--more-->

-   list-style
-   list-style-type
-   list-style-image
-   list-style-position
-   white-space
-   display

## list-style-type <a name="02"></a>

**Yapısı :** list-style-type: <deger> **Aldığı Değerler :** disc |
circle | square | decimal | lower-roman | upper-roman | lower-alpha |
upper-alpha | none **Başlangıç değeri:** disc **Uygulanabilen
elementler:** [display][] değeri list-item alan elementler
**Kalıtsallık:** Var

**list-style-type** özelliği list-item işaretinin tipini belirler.
list-style-images özelliği **none** değeri aldığında veya resim
görüntülenemediğinde kullanılır.

	:::css
	 ul.arabalar { list-style-type: none } ol ol
ol { list-style-type: lower-roman /* i ii iii iv v gibi. */ }


<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 2+

</div>
## list-style-image<a name="03"></a>

**Yapısı :** list-style-image: <deger> **Aldığı Değerler :**
<[url][]> | none **Başlangıç değeri:** none **Uygulanabilen
elementler:** [display][] değeri list-item alan elementler
**Kalıtsallık:** Var

**list-style-image** özelliği list-style işaretinin yerine resim koymak
için kullanılır. 	:::css
	 ul{ list-style-image:
url(mavitop.gif) } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 2+

</div>
## list-style-position<a name="04"></a>

**Yapısı :** list-style-position: <deger> **Aldığı Değerler :** inside
| outside **Başlangıç değeri:** outside **Uygulanabilen elementler:**
tüm elementler **Kalıtsallık:** Yok

**list-style-position** özelliği **list-item** işaretlerin metinin
içinden(inside) veya soldan dışında(outside) mı olacağını belirler.

	:::css
	 ul{ list-style-position: inside }


<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 2+

</div>
## list-style<a name="01"></a>

<div class="cssozelliktanimi" id="ozelliktanim">
**Yapısı :** list-style: <deger> **Aldığı Değerler :**
<list-style-type> |<list-style-position> | <[url][]> **Başlangıç
değeri:**0 **Uygulanabilen elementler:** display değeri list-item alan
elementler **Kalıtsallık:** Var

</div>
**list-style** özelliği list-style-type, list-style-position ve
list-style-image özelliklerinin kısayoludur.

	:::css
	 ul{ list-style: disc outside } ol{
list-style: decimal inside } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 2+

</div>
## white-space<a name="05"></a>

**Yapısı :** white-space: <deger> **Aldığı Değerler :** normal | pre |
nowrap **Başlangıç değeri:** normal **Uygulanabilen elementler:**
[Block-level elementler][] **Kalıtsallık:** Var

**white-space**özelliği elemetlerin boşluklarının nasıl işlem göreceğini
belirler. değer alır. **normal:** birden fazla boşluğu tek boşluk gibi
sayar. **pre :** birden fazla boşluğu birleştirmez. **nowrap :** <br>
etiketi hariç alt satıra geçişe izin vermez.

	:::css
	 p { white-space: pre; } 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 2+

</div>
## display<a name="06" id="06"></a>

**Yapısı :** display: <deger> **Aldığı Değerler :** none | inline |
block | inline-block | list-item | run-in | table | inline-table |
table-row-group | table-header-group | table-footer-group | table-row |
table-column-group | table-column | table-cell | table-caption | inherit
**Başlangıç değeri:** inline **Uygulanabilen elementler:** tüm
elementler **Kalıtsallık:** Yok

**display**özelliği elemetlere aşağıdaki dört değerden birini atamak
için kullanılır: **block:** elementden önce ve sonra bir satır bırakır.
**inline :** elementden önce ve sonra bir satır bırakmaz. **nowrap :**
block gibidir tek fark list-item işareti eklemesidir.  
**none:** element görüntülenmez. Elementi gizler. Bir çok javascript
uygulmasında kullanılan bir özelliktir.

Bu dört özellik çok kullanıldıkları için üzerinde duruldu.

	:::css
	 p { display: inline; } em { display: block;
} 

<div class="tarayiciuyum">
**Tarayıcı Uyumu:** Internet Explorer+ Firefox+ Chrome+ Safari+ Opera+
W3C's CSS Level 2+

</div>
</p>

  [display]: #
  [url]: http://www.fatihhayrioglu.com/?p=95
  [Block-level elementler]: http://www.fatihhayrioglu.com/?p=13
