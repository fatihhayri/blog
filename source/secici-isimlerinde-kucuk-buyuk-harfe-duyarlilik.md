Title: CSS İpuçları  5 : CSS seçicilerini tanımlarken küçük-büyük harfe dikkat etmek
Slug: secici-isimlerinde-kucuk-buyuk-harfe-duyarlilik
Date: 2006-07-20 01:18
Category: CSS
Tags: CSS, html, küçük büyük harf, seçici, selector

Eğer XHTML ile CSS kullanıyorsak seçici(selector) olarak kullandığımız
XHTML elementlerinin küçük büyük harfe duyarlı olduğunu unutmamalıyız.
Küçük büyük harf farklılıklarından kaynaklanan sorunları aşmak için
XHTML elementi olarak kullandığımız seçicileri küçük harfle yazarak bu
sorunu bertaraf etmiş oluruz. HTML ve XHTML'in her ikisinde de
özellikler(attributes) küçük büyük harfe duyarlıdır. Eğer farklı harf
büyüklükleri kullanıyorsanız buna çok fazla dikkat etmelisiniz.
	
	:::css
	.DenemeYazisi{
		font:12px Arial, Verdan, serif
	}
	
HTML kodu;

	:::html
	<p class="DenemeYazisi">Dikkatli ol!</p> 
