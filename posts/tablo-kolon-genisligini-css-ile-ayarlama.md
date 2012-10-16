Title: Tablo kolon genişliğini css ile ayarlama
Date: 2007-08-23 09:40
Category: CSS, XHTML
Tags: CSS, gmail, tablo, tablo-hücre-genişliği, Tablolar, XHTML

Tablolarda bazen içeriğe göre tablonun genişlemesini istemeyiz veya
içeriği aşağı kaymasını engellemek isteriz. İşte çözüm hemde Gmail'den.

Google bize web hakkında örnekleri ile de yardım ediyor. Gmail'de tablo
genişliğini sabitlemenin daha doğrusu metinin tablo genişliğine göre
overflow:hiden uygulamasını gösteren güzel bir yöntem

[sourcecode language="css"] .grid { table-layout: fixed; } .grid * td {
empty-cells: show; overflow: hidden; width: 100%; } [/sourcecode]

![Gmail Tablo genişliği][]

Güzel bir ayrıntıyı yakalamışlar. table-layout: fixed; tanımı işin püf
noktası

Örnek sayfayı görmek için [tıklayınız.][]

Kayanak:
[http://blog.opencomponentry.com/2007/08/22/gmail-table-column-sizing-css-fun/][]

</p>

  [Gmail Tablo genişliği]: http://blog.opencomponentry.com/wp-content/uploads/2007/08/gmail-column-size.png
  [tıklayınız.]: http://blog.opencomponentry.com/grid.html
  [http://blog.opencomponentry.com/2007/08/22/gmail-table-column-sizing-css-fun/]:
    http://blog.opencomponentry.com/2007/08/22/gmail-table-column-sizing-css-fun/
