Title: CSS İpuçları 14 - IE div yüksekliği sorunu
Date: 2008-01-10 22:32
Category: CSS, XHTML
Tags: CSS, div yüksekliği sorunu, ie, internet explorer, XHTML

[sourcecode language='css'] our\_style { height: 1px; width: 100px;
background-color: black; }[/sourcecode] [sourcecode language='html']

<div class="test">
</div>
[/sourcecode]

Bu kod Firefox'da sorunsuz çalışmasına karşın IE'de yükseklik 10px
görünecektir. Bir bakıma IE boş içeriğin yüksekliğini 10px kabul ediyor,
ancak bu bizim işimizi bozuyor. Çözüm ise çok basit.

[sourcecode language='css'].test { font-size: 0; height: 1px; width:
100px; background-color: black; }[/sourcecode]

Sadece font-size tanımını 0 atamamız yeterli.

Kaynak: [http://vaig.be/2007/04/07/div-styleheight-1px-bug-in-ie/][]

</p>

  [http://vaig.be/2007/04/07/div-styleheight-1px-bug-in-ie/]: http://vaig.be/2007/04/07/div-styleheight-1px-bug-in-ie/
