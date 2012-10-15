Title: VMware Kurarken &quot;Setup failed to write data to the registry&quot; hatası aldım
Date: 2009-09-01 16:18
Category: Haberler
Tags: hata, sanal-makina, VMware

VMware güzel bir program. Bilgisayarıma kurarken bi yerde takılıyor ve
kuramıyorda ve kendini kaldırıyordu ve sonrada aşağıdaki hatayı veriyor.
"**Setup failed to write data to the registry**"
**C:\\Users\\Administrator\\AppData\\Local\\Temp** Bu yol sizin
bilgisayarınıza göre değişebilir. **vminst.log** dokümanında aşağıdaki
bilgiler vardı. [sourcecode] VMInst: 01/19/08 19:41:29 Setting up
registry VMInst: 01/19/08 19:41:29 Writing entries to
HKEY\_LOCAL\_MACHINE\\SOFTWARE\\VMware, Inc.\\VMware Workstation VMInst:
01/19/08 19:41:29 Getting Property CustomActionData = VMware
Player;C:\\Program Files\\VMware\\VMware Player\\ VMInst: 01/19/08
19:41:29 Failed to create key SOFTWARE\\VMware, Inc.\\VMware
Workstation: 5 VMInst: 01/19/08 19:41:29 Cannot add installation path to
registry. VMInst: 01/19/08 19:41:29 Attaching to window with title
"VMware Player" VMInst: 01/19/08 19:41:34 End Logging [/sourcecode]

### Çözüm

Sorunun çözümü ise Çalıştırı açıp(**ctrl + R** ) **regedit** Yazıyoruz
ve **HKEY\_LOCAL\_MACHINE\\SOFTWARE** de "VMware, Inc." ve daha sonrada
bunun altında "VMware Workstation" diye alanlar oluşturup. Kurulumu
yapalım. Kaynak: [http://communities.vmware.com/message/843711][]

</p>

  [http://communities.vmware.com/message/843711]: http://communities.vmware.com/message/843711
