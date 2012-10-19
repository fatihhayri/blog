Title: CSS İpucu 16: Evrensel seçicilerde yazıtipi kısaltması kullanımında sorun
Date: 2008-05-30 16:15
Category: CSS, XHTML
Tags: CSS, Evrensel-Seçiciler, tüm-elemanlar

Evrensel seçicisi olan olan * ile yaptığımız font tanımları sorun
çıkarıyor. Örneğin 	:::css
	 * { font:10px/1.5em
Verdana, Arial, Helvetica, sans-serif; }  Tanımını
yaptığımızda sayfalarımızda tanımladığımız <strong> ile
kalınlaştırdığımız metinler normal görünüyor. Bunun sebebi yukarıda
yaptığımız tanım. Bunu yerine tek tek tanım yaparsak sorun kalmıyor.
	:::css
	 *{ font-family: Verdana, Arial, Helvetica,
sans-serif; font-size:10px; line-height:1.5em; } 
