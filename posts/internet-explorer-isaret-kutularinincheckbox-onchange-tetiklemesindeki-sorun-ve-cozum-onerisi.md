Title: Internet Explorer İşaret kutularının(checkbox) onchange tetiklemesindeki sorun ve çözüm önerisi
Date: 2007-08-09 09:45
Category: Javascript
Tags: hata, Hata ayıklama, ie, ie-hata, ie6, işaret-kutucuğu, Javascript

Aslında konuyu başlıkta anlattım. İşaret kutularına **onchange** ekleyip
tetiklemeye çalışınca çalışmıyor. Firefox'da çalışıyor sorunun çözümü

	:::javascript
	 <p> <input type="checkbox"
onchange="document.getElementById('spDegistir').innerHTML = 'Checked: '
+ this.checked;" id="change"> <label for="change">Using
onchange</label> <span id="spDegistir"></span> </p>


Bu kod Internet Explorer'da çalışmayacaktır. Bizde bunun yerine
**onclick** tetiklemesini kullanacağız.

	:::javascript
	 <p> <input type="checkbox"
onclick="document.getElementById('spDegistir').innerHTML = 'Checked: ' +
this.checked;" id="change"> <label for="change">Using
<code>onchange</code></label> <span id="spDegistir"></span>
</p> 

kaynak: [http://krijnhoetmer.nl/stuff/javascript/checkbox-onchange/][]

</p>

  [http://krijnhoetmer.nl/stuff/javascript/checkbox-onchange/]: http://krijnhoetmer.nl/stuff/javascript/checkbox-onchange/
