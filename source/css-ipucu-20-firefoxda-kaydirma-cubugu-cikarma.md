Title: CSS İpucu 20: Firefox&#039;da Kaydırma Çubuğu Çıkarma
Date: 2009-04-16 10:21
Category: CSS
Tags: Firefox, ipucu, kaydırma-çubuğu, mozilla, overflow

Firefox İnternet Explorer'un tersine eğer sayfa yüksekliği kaydırma
çubuğu çıkarmayacak kadar yüksekliğe sahip değilse kaydırma çubuğu
çıkarmıyor. Bu özellikle çerçeveli sayfalarda sorun çıkarabilir. Bunun
için bir çözüm.

	:::css
	html{
		overflow:-moz-scrollbars-vertical;
	} 
