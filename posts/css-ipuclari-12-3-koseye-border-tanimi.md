Title: CSS İpuçları - 12 : 3 köşeye border tanımı
Date: 2007-04-24 16:26
Category: CSS, XHTML
Tags: CSS, XHTML

Normalde tüm köşelere kenarlık(border) tanımlarken:

[sourcecode language="css"] border: 1px solid \#333; [/sourcecode]

kullanılır. Tek köşeye kenarlık vermek içinse:

[sourcecode language="css"] border-[top-right-bottom-left]: 1px solid
\#333; [/sourcecode]

kullanılır. köşeye kenarlık vermek için her birini ayrı ayrı
tanımlamamız gerekir.

[sourcecode language="css"] border-top: 1px solid \#333; border-right:
1px solid \#333; border-left: 1px solid \#333; [/sourcecode]

Bunun yerine olmayan kenarı(örn: alt kenar) görünmez yaparak hallede
biliriz.

[sourcecode language="css"] border: 1px solid \#333; border-bottom: 1px
solid \#fff; [/sourcecode]

</p>

