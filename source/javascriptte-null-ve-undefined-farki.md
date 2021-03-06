Title: Javascript’te “null” ve “undefined” farkı
Date: 2011-08-18 14:19
Category: Javascript
Tags: boş, null, tanımsız, typeof, undefined

Javascript diğer birçok dilden farklı olarak **null** ve **undefined**
iki ayrı durum olarak kabul eder.

**null;** boş değer anlamına gelen özel bir değerdir. **typeof null**
bize nesne döndürür.

	:::javascript
	<script>
		var testDegiskeni = null;
		alert(testDegiskeni); //null 
		alert(typeof testDegiskeni); //object
	</script> 

**undefined** değişken bildirilmiş ama henüz değeri atanmamış demektir.

	:::javascript
	<script>
		var testDegiskeni;
		alert(testDegiskeni); // undefined 
		alert(typeof testDegiskeni); //undefined
	</script>


Yukarıdaki örneklerde gördüğümüz gibi **null** özel bir nesne iken
**undefined** tip olarak **undefiend** döndürür.

Atanmamış değişkenlerin değeri javascript tarafında otomatik olarak
**undefined** olarak atanır.

Javascript asla **null** değeri atamaz. Eğer bir elemanın değeri
**null** ise bu javascript tarafından değil, program tarafından atanmış
demektir.

## undefined ve null kontrolü

	:::javascript
	if(typeof(test) !== 'undefined' && test != null) {
		//test değişkenin kullanabiliriz
	} 

## Kaynak

-   [http://stackoverflow.com/questions/27509/detecting-an-undefined-object-property-in-javascript][]
-   [http://snipplr.com/view.php?codeview&id=14618][]
-   [http://www.bloggingdeveloper.com/post/JavaScript-null-vs-undefined-The-Difference-between-null-and-undefined.aspx][]
-   [http://www.joeyjavas.com/2007/04/25/javascript-difference-between-null-and-undefined/][]
-   [http://bonsaiden.github.com/JavaScript-Garden/#core.undefined][]

  [http://stackoverflow.com/questions/27509/detecting-an-undefined-object-property-in-javascript]: http://stackoverflow.com/questions/27509/detecting-an-undefined-object-property-in-javascript
  [http://snipplr.com/view.php?codeview&id=14618]: http://snipplr.com/view.php?codeview&id=14618
  [http://www.bloggingdeveloper.com/post/JavaScript-null-vs-undefined-The-Difference-between-null-and-undefined.aspx]: http://www.bloggingdeveloper.com/post/JavaScript-null-vs-undefined-The-Difference-between-null-and-undefined.aspx
  [http://www.joeyjavas.com/2007/04/25/javascript-difference-between-null-and-undefined/]: http://www.joeyjavas.com/2007/04/25/javascript-difference-between-null-and-undefined/
  [http://bonsaiden.github.com/JavaScript-Garden/#core.undefined]: http://bonsaiden.github.com/JavaScript-Garden/#core.undefined
