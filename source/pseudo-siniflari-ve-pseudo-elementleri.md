Title: Sözde-sınıflar(Pseudo-class) ve Sözde-elementler(Pseudo-elements)
Slug: pseudo-siniflari-ve-pseudo-elementleri
Date: 2006-07-22 20:36
Category: CSS
Tags: CSS, link, Pseudo-elementleri, Pseudo-sınıfı, sözde-elementler, sözde-sınıflar

Pseudo sınıf ve elementleri CSS'i destekleyen web tarayıcıları
tarafından otomatik olarak tanınan özel sınıf ve elementlerdir. Bu sınıf
ve elementler (x)html hiyerarşisi ile erişemediğimiz element ve
sınıflara erişmemizi sağlar. **Pseudo sınıfı** bir elementi farklı
sınıflara böler(örn: link elementini active, visited vd. sınıflarına
böler) **Pseudo elementi** ise bir elementi alt kısımlara böler (örneğin
bir paragrafın ilk harfi, bir paragrafın ilk satırı gibi.)
Pseudo sınıfına örnek: 	

	:::css
	a:visited { 
		color: red; 
	}  

Pseudo elementine örnek: 	

	:::css
	p:first-line { 
		font-weight: bold; 
	}  
	
Pseudo sınıf ve elemtleri HTML class özelliği olarak belirtilmemiştir. Normal
sınıflar pseudo sınıf ve elementleri ile kullanılabilir. 	

	:::css
	a.disariyalinkller:link, 
	a.disariyalinkller:visited {
		color: maroon; 
	}
	
Aynı şekilde id seçicileri ile birlikte de kullanılabilirler 	

	:::css
	a#altkisim:link{
		font-weight: bold; 
	}

Pseudo sınıflarını da ikiye ayıra biliriz. **Link Pseduo Sınıfıları** ve **Dinamik Pseudo Sınıfları**

## Link Pseudo sınıfı

Yanlızca linklere uygulanan iki Link Pseduo sınıfı vardır. **:link** ve
**:visited** **:link -**Ziyaret edilmemiş sayfanın linkine stil
tanımlaması yapmak için kullanılır. Ancak bir çok web tarayıcısı yapılan
stil tanımlarını ziyaret edilmiş sayfa linklerine de uygular. **:visited
-** Henüz ziyaret edilmiş sayfa linklerine stil tanımlaması yapmak için
kullanılır. 	

	:::css
	a:link { 
		color: blue; 
	}
	
	a:visited { 
		color: red; 
	}  
	
Bunun yerine genelde aşağıdaki gibi bir kod da kullanılır 	

	:::css
	a { 
		color: blue;
	} 
	
	a:visited { 
		color: red; 
	} 

Bu kodlama ile kullanıcaya ziyaret ettiği sayfa linkleri farklı renkte gösterilerek içeriksel bir
bilgi görsel olarak verilebilir.

**Tarayıcı Uyumu**   
Firefox    
Chrome   
Safari   
Opera   
İnternet Explorer 
{: .tarayiciuyum}

## Dinamik Pseudo Sınıfları

**Dinamik Pseudo Sınıfları** sayfa görünümüne çok büyük katkılar
yapabilir. Bu sınıflar genelde linklere uygulanır ancak bir çok kullanım
alanları vardır. tanedir **:focus**, **:active** ve **:hover**

**Not**
Pseudo sınıflarında sıralama önemlidir. Genel kullanımda
**"link-visited-hover-active,"**sıralaması yapılmalıdır. Tüm sınıflar
içinse **"link-visited- focus-hover-active."** sıralaması yapılmalıdır.

**:focus -** Odaklanan elemente stil tanımlası yapmak için kullanılır
Örn: input alanına içerik girerken **:active** - Aktif olan elemente
stil atamak için kullanılır. **:hover -** Bir elementin üzerine Farenin
imleci geldiğinde yapılacak tanımlama için Örn: bir linkin üzerine fare
ile geldiğimizde renk değiştirmesini sağlamak için Linkler için genel
kullanım 	

	:::css
	a:link { 
		color: navy; 
	}
	
	a:visited {
		color: gray; 
	}
	
	a:hover { 
		color: red; 
	}
	
	a:active { 
		color: yellow; 
	}

**:focus** için bir örnek verecek olursak 	

	:::css
	input:focus { 
		background: silver; 
		font-weight: bold; 
	}


**Tarayıcı Uyumu**  
Firefox   
Chrome   
Safari   
Opera   
İnternet Explorer 
{: .tarayiciuyum}
	
## İlk Çocuk Elementi seçmek

Diğer bir pseudo sınıfımız **:first-child**'dır. **first:child:**
Belirtilen elementin ilk Çocuk Elementine stil atamak için kullanılır.
	
	:::css
	p:first-child {
		font-weight: bold;
	}
	
	li:first-child {
		color:#f00;
	}  	

HTML;

	:::html
	<div>
	    <p>Bu paragraf ilk çocuk elementidir ve sonuç olarak kalın olacaktır</p>
	    <ul>
	        <li>Bu liste ilk çocuk elementidir ve font rengi kırmızı olacak</li>
	        <li>Bu <strong>çocuk element </strong>değil</li>
	        <li>Bu da değil</li>
	    </ul>
	    <p>Bu pragraf <em>bir</em> çocuk element değil.</p>
	</div>

**Tarayıcı Uyumu**  
Firefox   
Chrome   
Safari   
Opera    
İnternet Explorer 
{: .tarayiciuyum}

## :lang Pseudo Sınıfı

Lang pseudo sınıfı içerikteki bir elemente farklı bir dil de yazmamızı
sağlar. Atanabilecek dil listesi ve kullanılacak kısaltmalara [ISO 639 and RFC 1776 standards][] erişebilirsiniz. 	

	:::html
	<html>
	<head>
	<title>lang test</title>
	<style type="text/css">
	p:lang(fr) {
		color: red;
	}
	</style>
	</head><body>
	<p lang="fr">Bonjour le monde!</p>
	</body>
	</html>

**Tarayıcı Uyumu**   
Firefox   
Chrome   
Safari   
Opera   
İnternet Explorer 8+
{: .tarayiciuyum}

## Pseudo Sınıflarını birleştirmek

CSS2.1 ile birlikte aynı seçiciye ait pseudo elemntlerini birleştirme
özelliği de gelmiştir. Örneğin ziyaret edilmiş linklerin hover özelliği
ile ziyaret edilmemiş linklerin hover özelliğini farklı atamak istesek
	
	:::css
	a:link:hover { 
		color: red; 
	}
	
	a:visited:hover{ 
		color: pink; 
	}  
	
Sıralama önemli değildir.

**Tarayıcı Uyumu**  
Firefox   
Chrome   
Safari   
Opera   
İnternet Explorer 8+
{: .tarayiciuyum}

## Pseudo Element Seçicileri

Bu elementler hayali elementlerdir. (X)HTML hiyerarşisi içinde bu
elemntlere yoktur. CSS2.1 de Dört adet Pseudo Element Seçicisi vardır:
**first-letter**, **first-line**, **before** ve **after**

## first-letter (ilk harf)

Bir blok-level elementin ilk harfine stil tanımlması yapmak için
kullanılır. Örnek verecek olursak h1 elementinin baş harfinin büyük
olması için : 	

	:::css
	h1:first-letter { 
		font-size:200%; 
	}  	
	
	:::html
	<h1>Bu büyük bir başlık</h1> 

**Tarayıcı Uyumu**    
Firefox   
Chrome   
Safari   
Opera   
İnternet Explorer 7+
{: .tarayiciuyum}

## first-line (ilk satır)

Bir metnin ilk elementine stil atamak için kullanılır. Örneğin
paragraflarınızın ilk satırlarını renklendirmek isitiyorsunuz.
	
	:::css
	p:first-line { 
		color: red; 
	} 

**Tarayıcı Uyumu**  
Firefox   
Chrome   
Safari   
Opera   
İnternet Explorer
{: .tarayiciuyum}


## before ve after elementleri

Bir elementin öncesine ve sonrasına bir içerik veya özellik eklemek için
kullanılır. Notlarımızın başına otomatik oalrak Not yazmak için
	
	:::css
	P.not:before { 
		content: "Not." 
	}

kodu yeterlidir. Aynı şekilde paragraflarımzın sonuna
otomatik bitti yazıp nokta koymak istersek 	

	:::css
	body:after { 
		content: " Bitti."; 
	} 

yeterlidir.

**Tarayıcı Uyumu**  
Firefox    
Chrome   
Safari    
Opera   
İnternet Explorer 8+
{: .tarayiciuyum}




  [ISO 639 and RFC 1776 standards]: http://www.dsv.su.se/~jpalme/ietf/language-codes.html
