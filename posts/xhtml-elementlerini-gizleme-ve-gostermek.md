Title: (X)Html Elementlerini gizleme ve göstermek
Date: 2006-09-07 19:11
Category: Javascript
Tags: eleman gizle, fonksiyon, göster-gizle, Javascript

[sourcecode language="javascript"] function gostergizle(elementid){
document.getElementById(elementid).style.display=
(document.getElementById(elementid).style.display!="block")? "block" :
"none" } [/sourcecode]

kod kısmında da

[sourcecode language="html"] <a
href="javascript:gostergizle('haber')">haber</a> <div
id="haber">haberler .......</div> [/sourcecode]

Bu hem elementlerimizi göstermeye hemde gizlemeye yarayan bir fonksiyon.
Basit ve kullanışlı bir fonksiyon

</p>

