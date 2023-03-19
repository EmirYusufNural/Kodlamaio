# Kodlamaio
Odev

HTML Nedir Ne İşe Yarar?
Web dünyasının en önemli konularından biri olan ve bir anlamda vazgeçilmezi diyebileceğimiz bir konuyla karşınızdayız. Açılımı İngilizce olarak ‘ Hyper Text Markup Language’ olan ve ‘Hiper Metin İşaretleme Dili’ şeklinde Türkçe ifade edilen bir metin işaretleme dilidir. Yazımızın ilerleyen kısımlarında Html nedir kısaca bahsedeceğiz.

İnternet üzerinde kullanıcıların giriş yapmalarını sağlamak amacıyla web sayfaları oluşturmak için kullanılan bir betik dili olan Html sayfası bulunduğu sunucularda ‘.html‘ veya ‘.htm‘ uzantılarıyla tutulur.

Herhangi bir web sitesine giriş yapılınca sistemin bizi yönlendirdiği sayfa, siteye giriş sayfası olarak tanımlanır. Bahsedilen bu sayfanın ismi farklı farklı tanımlanabilmektedir. Aşağıda bu isimlere örnek olması açısından bazı giriş sayfası isimleri yazılmıştır.

html
htm
html
htm
aspx
php
Görüldüğü gibi farklı dosya isimleri ve farklı uzantılar kullanılarak giriş sayfaları belirlenebilmektedir. İlgili sunucuda mevcut web sitesi için hangisinin giriş sayfası olduğu belirlemek gerekecektir. Bu işlemden sonra artık giriş sayfası üzerinden siteye girişler sorunsuz bir şekilde sağlanabilir.

Html gerçek anlamda bir programlama dili olmamasına karşın yine de belli bir sözdizimi ve kullanımı bulunmaktadır. Bu kurallara uyarak Html kodları yazmak gerekir. Peki Html kodu nedir? Bir sonraki başlığa geçip Html’in sözdizimine göz atalım.

Html Kodu Nedir?
Html ile web sayfaları oluşturmak çok basittir. Bu dil ile web sayfaları oluşturmaya başlayınca günlük konuşma dilini kullanıyormuşçasına sayfalar geliştirebilirsiniz. Bu aşamada css nedir sorusu da cevaplanması gereken sorulardandır ama şu an konumuz dışında olduğu için değinilmeyecektir. Çünkü css başlı başına farklı bir teknolojidir.

Şimdi artık Html nasıl kullanılır sorusuna cevap verebiliriz. Bunun için ‘Notepad’ programını kullanmak oldukça pratik bir çözüm olacaktır. Zaten Html ile geliştirilen uygulamaların derlenmesine gerek olmaması bu konuda geliştiricilere büyük kolaylık ve avantajlar sağlamaktadır.

Html Sayfası Oluşturmak
Bir Html sayfası oluşturmak için küçük ve büyük (< >) işaretlerinden sıkça faydalanacağız. O zaman öncelikle < > işaretlerinin arasına ‘html’ yazmakla başlayalım. Ardından yine (< >) işaretlerini kullanarak html tag’inin içerisine ‘head’ ve ‘body’ tag’lerini yazıyoruz. Burada yazdığımız html, head ve body Html dilinde tag olarak isimlendirilmektedir.

Şimdi yukarıda bahsettiğimiz durumun kodlarını detaylı bir şekilde aşağıda inceleyelim.

<html>

<head>

<title> İlk HTML Sayfamız </title>

</head>

<body>

<font size = "5" face = "Tahoma" color = "gray"> İlk HTML Sayfamız </font>

</body>

</html>

Yukarıdaki kodları incelediğimiz zaman iç içe geçmiş bir yapı görmekteyiz. En dışta yukarıda belirttiğimiz <html> </html>tag’leri yer alıyor. Sonra gelen tag <head> </head> ve daha sonraki tag <body> </body>’dir. Head tag’i başlık olarak ifade edilirken, body tag’i gövdeyi temsil eder. Yani bir web sayfasının başlıkla ilgili verileri head tag’i içerisine, içerik ve görünümle ilgili olanları ise body tag’i içerisine yazıyoruz.

HTML Kodları ve Anlamları
Etiket(Tag) Açıklama
<!–…–> Yorum tanımlar
<!DOCTYPE> Belge türünü belirler
<a> Bir köprüyü tanımlar
<abbr> Bir kısaltma veya bir kısaltma tanımlar
<acronym> Bir kısaltma tanımlar (HTML5’te <abbr> kullanılır)
<address> Bir belgenin yazarı / sahibinin iletişim bilgilerini tanımlar
<applet> Gömülü bir uygulamasını tanımlar.(HTML5’te <Embed> veya <object> kullanılır)
<area> Bir görüntü haritası içinde bir alanı tanımlar
<article> Bir makale tanımlar
<aside> Sayfa içeriğini kenara tanımlar
<audio> Ses içeriğini tanımlar
<b> Kalın metin tanımlar
<base> Bir belgedeki tüm göreli URL’ler için taban URL / hedef belirler
<basefont> Bir belgedeki tüm metin için bir varsayılan renk, boyut ve yazı belirtir (HTML5 desteklenmez. Bunun yerine CSS kullanın)
<bdi> Bunun dışındaki diğer metinden farklı bir yöne biçimlendirilmiş olabilir metnin bir kısmını izole eder
<bdo> Geçerli metin yönünü geçersiz kılar
<big> Büyük metin tanımlar (HTML5 desteklenmiyor. CSS yerine kullanın)
<blockquote> Başka bir kaynaktan alıntı bölüm tanımlar
<body> Belgenin cesedini tanımlar
<br> Tek bir satır sonu tanımlar
<button> Tıklanabilir bir düğme tanımlar
<canvas> Scripting aracılığıyla anında, grafik çizmek için kullanılır (genellikle JavaScript)
<caption> Bir tablo başlığını tanımlar
<center> Merkezli metni tanımlar (HTML5 desteklenmiyor. CSS yerine kullanın)
<cite> Bir eserin başlığını tanımlar
<code> Bilgisayar kodunun bir parçasını tanımlar
<col> Bir <COLGROUP> elemanı içinde her sütun için sütun özelliklerini belirtir
<colgroup> Biçimlendirmek için bir tablo, bir veya daha fazla sütun grubu belirtir
<datalist> Giriş kontrolleri için önceden tanımlanmış seçenekler listesini belirtir
<dd> Bir açıklama listesindeki bir terimin açıklaması / değerini tanımlar
<del> Bir belgeden silindi metni tanımlar
<details> Kullanıcı görüntülemek veya gizlemek ek ayrıntılar tanımlar
<dfn> Bir terimin tanımlanması örneğini temsil
<dialog> Bir iletişim kutusu veya pencere tanımlar
<dir> Bir dizin listesini tanımlar(HTML5 desteklenmiyor.<ul> kullanın)
<div> Bir belgedeki bölüm tanımlar
<dl> Bir açıklama listesi tanımlar
<dt> Bir açıklama listesinde bir terim / isim tanımlar
<em> Vurguladı metni tanımlar
<embed> Harici (HTML olmayan) uygulama için bir kabı tanımlar
<fieldset> Gruplar bir form elemanları ile ilgili
<figcaption> Bir <rakam> öğesi için bir başlık tanımlar
<figure> Kendi kendine yeten içeriği belirtir
<font> Metin için yazı tipi, renk ve boyutunu tanımlar
<footer> Bir belgenin veya bölümün altbilgi tanımlar
<form> Kullanıcı girişi için bir HTML formu tanımlar
<frame> Kullanıcı girişi için bir HTML formu tanımlar…
<frameset> Kare seti tanımlar
<h1> to
<h6> HTML başlıkları tanımlar
<head> Belge ile ilgili bilgiler tanımlar
<header> Bir belgenin veya bölümün bir başlık tanımlar
<hr> Içerik tematik değişiklik tanımlar
<html> Defines the root of an HTML document
<i> Bir HTML belgesinin kök tanımlar
<iframe> Bir satır içi çerçeve tanımlar
<img> Bir görüntü tanımlar
<input> Bir giriş kontrolü tanımlar
<ins> Bir belgeye yerleştirilmiş olan bir metin tanımlar
<kbd> Klavye girişi tanımlar
<keygen> (Formlar için) bir anahtar çifti jeneratör alanını tanımlar
<label> Bir <input> öğesi için bir etiket tanımlar
<legend> Bir <fieldset> öğesi için bir başlık tanımlar
<li> Bir liste öğesini tanımlar
<link> Bir belge ve harici kaynak arasındaki ilişki (en stil sayfalarını bağlamak için kullanılır) tanımlar
<main> Bir belgenin ana içeriğini belirler
<map> Bir istemci tarafı görüntü haritası tanımlar
<mark> İşaretli / vurgulanan metni tanımlar
<menu> Komutların bir listesini / menü tanımlar
<menuitem> Kullanıcı açılır menüden çağırabilirsiniz bir komut / menü öğesi tanımlar
<meta> Bir HTML belgesi hakkında meta tanımlar
<meter> Bilinen bir aralık içinde bir sayıl ölçümünü tanımlar (bir ölçü)
<nav> Navigasyon bağlantıları tanımlar
<noframes> Çerçeveleri desteklemeyen kullanıcılar için alternatif bir içerik tanımlar
<noscript> Istemci tarafı komut desteği olmayan kullanıcılar için alternatif bir içerik tanımlar
<object> Katıştırılmış nesne tanımlar
<ol> Sıralı liste tanımlar
<optgroup> Bir açılan listesinde ilgili seçeneklerin bir grup tanımlar
<option> Bir açılır listeden bir seçenek tanımlar
<output> Bir hesaplamanın sonucunu tanımlar
<p> Bir paragraf tanımlar
<param> Bir nesne için bir parametre tanımlar
<pre> Önceden biçimlendirilmiş metni tanımlar
<progress> Bir görevin ilerlemesini temsil
<q> Kısa bir alıntı tanımlar
<rp> Yakut açıklamaları desteklemeyen tarayıcılarda göstermek ne tanımlar
<rt> (Doğu Asya tipografi için) karakter bir açıklama / telaffuz tanımlar
<ruby> (Doğu Asya tipografi için) bir yakut ek açıklama tanımlar
<s> Artık doğru metin tanımlar
<samp> Bir bilgisayar programı örnek çıktı tanımlar
<script> Bir istemci tarafı komut dosyası tanımlar
<section> Bir belgedeki bölüm tanımlar
<select> Bir açılır listeyi tanımlar
<small> Daha küçük metin tanımlar
<source> (<Video> ve <audio>) medya unsurları için birden fazla medya kaynakları tanımlar
<span> Bir belgedeki bölüm tanımlar
<strike> Çizili metni tanımlar(HTML5 desteklenmiyor. <del> veya <s> kullan)
<strong> Önemli metni tanımlar
<style> Bir belge için stil bilgilerini tanımlar
<sub> Indisli metni tanımlar
<summary> Bir <detay> elemanı için görünür bir başlık tanımlar
<sup> Üstsimge metni tanımlar
<table> Tablo tanımlar
<tbody> Gruplar bir tablo vücut içeriği
<td> Bir tablodaki bir hücreyi tanımlar
<textarea> Çok satırlı giriş kontrolünü tanımlar (metin alanı)
<tfoot> Gruplar bir tablo altbilgi içeriği
<th> Bir tablodaki bir başlık hücreyi tanımlar
<thead> Bir tablodaki bir başlık hücreyi tanımlar
<time> Bir tarih / saat tanımlar
<title> Belge için bir başlık tanımlar
<tr> Bir tablodaki bir satır tanımlar
<track> (<Video> ve <audio>) medya unsurları için metin parçalarını tanımlar
<tt> Teletype metni tanımlar
<u> Normal metinden üslup farklı olmalıdır metni tanımlar
<ul> Sırasız liste tanımlar
<var> Bir değişken tanımlar
<video> Bir video veya film tanımlar
<wbr> Olası bir çizgi-break tanımlar

Selenium Locators(Konum Belirleyici) Nedir?
Tarayıcıyı açtık ve bir siteye girdik şimdi bu sitede neler yapabiliriz düşünelim. Belirli bir alana tıklayabilir, inputların veya text elemanlarının içerisini doldurabiliriz. Locators(Konumlandırıcı), Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur. Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur. Site üzerindeki bir elemente örneğin giriş butonuna selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi locator’lar aracılığıyla yaparız. Selenium ile geliştirmek istediğimiz test otomasyonlarında locator’ları kullanarak ilgili alanlara veri gönderebilir, tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz. Bunlar ‘By’ objesi olarak oluşturulur. En yaygın locator çeşitleri;

ID
Name
ClassName
TagName
LinkText
CssSelector
XPath
Web sitelerinde tagname’ler bulunur. Bu tagname’lerin sahip olduğu stil, name, id gibi attribute’ler vardır. Selenium’un anlayacağı şekilde nesneleri web elementlere çevirirken ilk önce id’si ve name’i var mı diye bakılır yok ise CssSelector ve Xpath ile nesneyi bulmaya çalışırız.

ID
Öğeyi bulmak için 3 bileşen kullanırız.

(Html etiketi) # (ID’nin değeri)


Giriş yap alanını Css selector ile Tag ve ID ile bulmak için;

driver.findElement(By.cssSelector(“a#login”))

2. Class

Bu locatorda ID gibi çalışır tek farkı # yerine nokta kullanılır.

(Html etiketi) . (Class’ın değeri)


Bu alanı Tag ve Class ile bulmak için;

driver.findElement(By.cssSelector(“div.SearchBoxOld-buttonContainer”))

3. Attribute Values

Bu yöntemde de elementin tag name’i ve elemente özel olan bir özelliği(type, name vb.) kullanılarak css selector yazılır.

(Html Tag)[Attribute=Value]


XPATH:

Xpath kısaca xml yolu olarak tanımlanır.

Xpath=//tagname[@Attribute=‘Value’]

tagname= Hedeflediğiniz elementin etiketi, örneğin bir giriş(input) etiketini ve ya bağlantı(anchor) etiketini, vb. belirtir.

attribute= ‘@‘ ön eki ve karşılık gelen değerleri ile tanımlanır. Name, ID, Class vb.olabilir.

1.Temel Xpath

Xpath’in standart syntax’ı ile kullanımıdır.


Xpath ile bulmak için;

driver.findElement(By.xpath(“//a[@id=‘login’]”))


Bu örnekte attribute olarak ID kullanılmıştır.

2. Contains()

Herhangi bir özelliğin değeri dinamik olarak değiştiğinde kullanılır.

Contains kullanarak xpath’ini yazarsak;

driver.findElement(By.xpath(“//input[contains(@class, ‘search-global’)]”))

3. AND ve OR Kullanımı ile Xpath

OR ifadesinde 1.koşulun ya da 2. Koşulun doğru olması yeterlidir. Her iki koşulun doğru olması durumunda da geçerlidir. AND ifadesinde iki koşul kullanılır, öğeyi bulmak için iki koşul da doğru olmalıdır. Herhangi bir koşul yanlışsa öne bulunamaz.

//input[@id=‘value of id’ OR @name=‘value of name’]


//input[@id=‘value of id’ AND @name=‘value of name’]

driver.findElement(By.xpath(“//input[@name=‘q’ AND @type=‘text’]”))

driver.findElement(By.xpath(“//input[@name=‘q’ OR @type=‘text’]”))

4.Starts — with fonksiyonu

Yenilenen veya web sayfasındaki diğer dinamik işlemlerle değiştirilen web öğesini bulmak için kullanılan bir işlevdir.


//input[@id=‘value of id’ AND @name=‘value of name’]

driver.findElement(By.xpath(“//input[starts-with(@name,’q’)]”))

5.Text()

Metin eşleşmesini kullanarak elementi bulmak için kullanılan bir yöntemdir.


//div[text()=‘value of text’]

driver.findElement(By.xpath(“//h2[text()=’Öne çıkanlar’]”))
Selenium’da Elementler
Selenium’da elementleri bulmak ve seçmek için birçok yöntem var bunlar :
Xpath Yöntemi : find_element_by_xpath()
ID Yöntemi : find_element_by_id()
Name Yöntemi : find_element_by_name()
Link Text Yöntemi : find_element_by_link_text()
TagName Yöntemi : find_element_by_tag_name()
Class Name Yöntemi : find_element_by_class_name()
CSS Selector Yöntemi : find_element_by_css_selector()
Partial Link Text Yöntemi : find_element_by_partial_link_text()
Eğer çoklu olarak uygulamak istiyorsak “element” yerine “elements” yazmamız yeterlidir örneğin : find_by_elements_by_name()

Xpath Nasıl Alınır Kullanılır?
Webdriverımız bize tarayıcıda “find_element_by_YÖNTEMADI”  yöntemlerink kullanarak veri almamızı sağlar.
Biz şimdi bu yöntemlerden biri olan xpath yöntemini göreceğiz.
Tarayıcıda belli bir bölgenin (arama butonu , giriş yap tuşu vs.) xpath’ini almak için şu adımları sırasıyla uygulamalıyız.
Öncelikle faremizi xpathini almak istediğimiz yerin üstüne getiriyoruz.
Daha sonra sağ tık yapıyoruz.
Ve en altta incele diyoruz.
Açılan elementler sekmesinde xpathini alacağımız metnin kodlarına gelip sağ tık yaptıktan sonra  “Copy” bölümünden “Copy Xpath” seçeneğini tıklatıyoruz.
Xpath Nasıl Kullanılır?
Xpath aldıktan sonra onu kullanmak için şu yöntemleri uyguluyoruz. Ben  instagrama girmek için giriş butonunun xpathini aldım.
Siz istediğiniz sitenin xpathini alabilirsiniz.
Kodları baştan itibaren yazacak olursak:
from selenium import webdriver

from selenium.webdriver.commons.keys import Keys

browser = webdriver.Chrome()

url = “https://instagram.com/”

browser.get(url)
usernameinput = browser_find_element_by_name(“username”)
usernameinput = browser_find_element_by_name(“password”)
//bu iki kodda “name” metodunu kullandık onuda birazdan göreceğiz.

usernameinput.send_keys(“instagrama giriş yapılacak hesabın k.adı”)
passwordinput.send_keys(“instagrana giriş yapılacak hesabın şifresi”)

login = browser.find_element_by_xpath(“//*[@id=’loginForm’]/div/div[3]“)

//Büyük fontla yazılan bizim xpathimiz.

login.click()
Yukarıdaki kodlarda sırasıyla şöyle yaptık:
Öncelikle seleniumu import ettik.
Sonrasında “browser” isimli değişkene driverımızı belirttik.
Daha sonra “url” isimli değişken bir tanımladık ve bu değişkenin içine gitmek istediğimiz sitenin linkini yazdık.
Ve “get” metodu kullanarak tarayıcımızda url değişkeninin içindeki link olan instagram sayfasını açtırdık.
Sonrasında name metodu kullanarak username ve password input yapacağımız kutucuklara eriştik.
Sonrasında send_keys metodu kullanarak bilgilerimizi kutucuklara yazdık.
Daha sonra “login” isimli değişken tanımladık ve değişkene giriş yap butonunun xpathini yazdık.
Xpathini yazdığımızda faremiz oranın üstüne gelmiş varsayılır. Bize kalan tıklatmak bunun içinde
login.click() kod bloğunu yazdık.
Böylece instagrama giriş yapmış olduk.
ID Yöntemi Nedir ? Nasıl Kullanılır?
Örnek olarak bir formumuz var ve bu formun id değerinin “kodakademisi” olduğunu biliyoruz eğer bilmiyorsak şöyle anlayabiliriz.
Formumuzun HTML kodları şu şekilde:
<html>
<body>
<form id=”kodakademisi”>
</form>
</body>
</html>
Gördüğünüz gibi yukarıdaki kodda sadece form tanımladık fakat input kısmı vs. yok.
ID değerini bulmak için <form> etiketleri arasında id=”herhangi bir id” şeklinde kod görmeliyiz. Eğer bu şekilde bir kod yok ise o sayfada ID yöntemini kullanamayız.
Yukardaki kodlarda yazdığımız “kodakademisi” id değerine sahip olan forma erişmek için şu kodları kullanırız : 

browser.find_element_by_id(“kodakademisi”)
şeklinde kod yazarsak form kısmına erişmiş oluruz.
Name Yöntemi Nedir? Nasıl Kullanılır?
Yazdığımız name değeri ile tanımlanmış ilk kod bloğuna erişir. Yine bir formumuz olduğunu varsayalım.

<html>
<body>
<form id=”kodakademisi”>
<input name=”username” type=”text”/>
<input name=”password” type=”text”/>
</form>
</body>
</html>
Yukardaki formumuza bu sefer kullanıcıdan iki değer isteyen input bölümü ekledik.
Birisi username birisi password.
Yukarıdaki username bölümüne erişmek için şu kodları kullanabiliriz :
browser.find_element_by_name(“username”)
şeklinde kod yazarsak name değeri “username” olan input bölümüne erişmiş oluruz.
Link Text Yöntemi Kullanımı?
Bir sayfada belirli bir bağlantıyı butonu vs. bulmak için kullanılır.
Yazdığımız link text ile tanımlanmış ilk kod bloğuna erişmemizi sağlar.
<a> etiketi yardımıyla bulunabilir.
Örneğin : 
<html>
<body>
  <p>18 yaşından büyük müsün?</p>
  <a href=”yes.html”>EVET</a>
  <a href=”no.html”>HAYIR</a>
</body>
</html>
Şeklinde bir sayfamız olduğunu varsayarsak  biz buradaki yes.html bçlümüne erişmek için şu kodları yazabiliriz.:

find_by_element_link_text(“EVET”)
kodumuzu yazarsak link text yöntemini kullanarak yes.html’e ulaşmış oluruz.
Tag Name Yöntemi Nedir? Nasıl Kullanılır?
Şu şekilde bir HTML sayfamız olduğunu varsayarsak :
<html>
<body>
  <h1> Python – Selenium Modülü Kullanımı</h1>
  <h2> Selenium Kullanımı</p>
  <p> Kod Akademisi </p>
</body>
</html>
Başlığa yani<h1> etiketine ulaşmak için şu kodları yazarız:
find_element_by_tag_name(“h1”)
şekinde kod yazarsak “h1” etiketinin olduğu kod bloğuna erişiriz.
Eğer şu şekilde yazsaydık :
find_element_by_tag_name(“p”)
paragrafa yani <p> etiketine erişmiş olurduk.
 Class Name Yöntemi Kullanımı
Şu şekilde bir HTML sayfamız olduğunu düşünürsek : 
<html>
<body>
  <h1>Selenium Nedir</h1>
  <p class=”kodakademisi”>Python – Selenium Kullanımı</p>
</body>
</html>
Yukarıda <p> etiketi içindeki paragrafa erişmek için class name yöntemini kullanabiliriz.
Şu kodları yazmamız yeterli olacaktır.

find_element_by_class_name(“kodakademisi”)
Bu şekilde içerigi “Python – Selenium Kullanımı”
olan paragrafa erişmiş olacağız.
Css Selector Yöntemi ve Kullanımı
Örnek olarak şöyle bir HTML sayfamız var :

<html>
<body>
  <h1>Selenium Nedir</h1>
  <p class=”kodakademisi”>Python – Selenium Kullanımı</p>
</body>
</html>
Bi yukardaki <p> etiketi içindeki paragrafa erişmek için css selector yöntemini kullanabiliriz. Şöyle :
find_element_by_css_selector(“p.kodakademisi”)
Yazarsak içeriği “Python – Selenium Kullanımı” olan kod bloğuna erişmiş oluruz.
Time Modülü Nedir ? Nasıl Kullanılır?
Bazı web sayfalarının açılması zaman alabilir bu nedenle projemizde birkaç saniyelik aralar vermemiz gerekir , programın sağlığı ve kullanıcı deneyimi için time modülünü kullanmamızın faydası olacaktır
Time modülünu projemize dahil etmek için kodlarımızın en başına gelip şunu yazıyoruz :

from time import sleep
Time modülünu import ettik. Kullanımı ise şöyle:
Mesela bir sayfaya gittik sayfanın açılması için 10saniye beklemek istiyoruz bunun için şu kodları yazabiliriz.

browser.get(“https://kod-akademisi.blogspot.com”)
sleep(10)
yazarsak 10 saniye duraklamış oluruz.

driver.get(url): Belirtilen URL'yi açar.

driver.find_element_by_*: Bir elementi bulmak için kullanılır. * yerine elementin hangi özelliği ile aranacağı yazılabilir. Örneğin, driver.find_element_by_name("username") gibi bir kod, sayfadaki "username" adlı bir form alanını bulur.

element.click(): Bir elementi tıklamak için kullanılır.

element.send_keys(value): Bir elemente metin girmek için kullanılır.

driver.back(): Önceki sayfaya gitmek için kullanılır.

driver.forward(): İleri gitmek için kullanılır.

driver.refresh(): Sayfayı yenilemek için kullanılır.

driver.quit(): Tarayıcıyı kapatmak için kullanılır.

driver.current_url: Geçerli sayfanın URL'sini döndürür.

driver.title: Geçerli sayfanın başlığını döndürür.

driver.maximize_window(): Tarayıcı penceresini tam boyutuna getirmek için kullanılır.

driver.minimize_window(): Tarayıcı penceresini küçültmek için kullanılır.

driver.set_window_size(width, height): Tarayıcı penceresinin boyutunu ayarlamak için kullanılır.

driver.execute_script(script): JavaScript kodunu çalıştırmak için kullanılır.

driver.find_elements_by_*: Bir element grubu bulmak için kullanılır. * yerine elementin hangi özelliği ile aranacağı yazılabilir.

element.clear(): Bir form alanını temizlemek için kullanılır.

element.get_attribute(name): Bir elementin belirtilen özelliğinin değerini döndürür.

element.is_enabled(): Bir elementin etkin olup olmadığını kontrol etmek için kullanılır.

element.is_selected(): Bir seçim kutusunun veya radyo düğmesinin seçili olup olmadığını kontrol etmek için kullanılır.

element.is_displayed(): Bir elementin görünür olup olmadığını kontrol etmek için kullanılır.

element.submit(): Bir formu göndermek için kullanılır.

Select(element): Bir açılır menüyü veya çoklu seçim kutusunu seçmek için kullanılır.

select.select_by_*: Bir açılır menüde veya çoklu seçim kutusunda bir öğe seçmek için kullanılır. * yerine seçilecek öğenin hangi özelliği ile aranacağı yazılabilir.

select.deselect_all(): Tüm seçimleri kaldırmak için kullanılır.

select.deselect_by_*: Belirtilen özelliğe sahip tüm öğelerin seçim

select.deselect_by_*: Belirtilen özelliğe sahip tüm öğelerin seçimini kaldırmak için kullanılır. * yerine seçimleri kaldırılacak öğenin hangi özelliği ile aranacağı yazılabilir.

element.text: Bir elementin metin içeriğini döndürür.

driver.find_element_by_xpath(xpath): XPath ifadesi kullanarak bir elementi bulmak için kullanılır.

driver.find_element_by_css_selector(css_selector): CSS seçicileri kullanarak bir elementi bulmak için kullanılır.

driver.switch_to.frame(frame): Bir iframe'e geçmek için kullanılır.

driver.switch_to.default_content(): Anasayfaya geri dönmek için kullanılır.

driver.switch_to.alert(): Bir uyarı kutusuna geçmek için kullanılır.

alert.accept(): Bir uyarı kutusunu kabul etmek için kullanılır.

alert.dismiss(): Bir uyarı kutusunu reddetmek için kullanılır.

driver.get_cookies(): Geçerli sayfanın çerezlerini döndürür.

driver.delete_all_cookies(): Tüm çerezleri silmek için kullanılır.

driver.add_cookie(cookie): Bir çerez eklemek için kullanılır.

driver.window_handles: Açık tüm pencere tanımlayıcılarını döndürür.

driver.switch_to.window(window_handle): Belirtilen pencereye geçmek için kullanılır.

ActionChains(driver).move_to_element(element).perform(): Fare imleci belirtilen elemente taşımak için kullanılır.

ActionChains(driver).click(element).perform(): Bir elemente tıklamak için kullanılır.

ActionChains(driver).context_click(element).perform(): Bir elemente sağ tıklamak için kullanılır.

ActionChains(driver).drag_and_drop(source, target).perform(): Bir elementi başka bir elemente sürüklemek için kullanılır.

ActionChains(driver).send_keys(keys).perform(): Tuş kombinasyonlarını göndermek için kullanılır.

WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((By.*, value))): Belirtilen elementin belirtilen süre boyunca sayfada görünmesini bekler.

WebDriverWait(driver, timeout).until(expected_conditions.visibility_of(element)): Belirtilen elementin belirtilen süre boyunca görünür hale gelmesini bekler.

WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable((By.*, value))): Bir elementin belirtilen süre boyunca tıklanabilir hale gelmesini bekler.

WebDriverWait(driver, timeout).until(expected_conditions.alert_is_present()): Bir uyarı kutusunun belirtilen süre boyunca görünmesini bekler.

Select(element).options: Bir açılır menüde veya çoklu seçim kutusunda mevcut tüm seçenekleri döndürür.

Select(element).select_by_index(index): Belirtilen sıradaki seçeneği seçmek için kullanılır.

Select(element).select_by_value(value): Belirtilen değere sahip seçeneği seçmek için kullanılır.

Select(element).select_by_visible_text(text): Belirtilen görüntülenen metne sahip seçeneği seçmek için kullanılır.

Select(element).deselect_all(): Bir çoklu seçim kutusundaki tüm seçenekleri kaldırmak için kullanılır.

Select(element).deselect_by_index(index): Belirtilen sıradaki seçeneğin seçimini kaldırmak için kullanılır.

Select(element).deselect_by_value(value): Belirtilen değere sahip seçeneğin seçimini kaldırmak için kullanılır.

Select(element).deselect_by_visible_text(text): Belirtilen görüntülenen metne sahip seçeneğin seçimini kaldırmak için kullanılır.

driver.set_window_size(width, height): Tarayıcının pencere boyutunu ayarlamak için kullanılır.

driver.maximize_window(): Tarayıcının penceresini tam ekran yapmak için kullanılır.

driver.minimize_window(): Tarayıcının penceresini simge durumuna küçültmek için kullanılır.

driver.back(): Bir önceki sayfaya geri dönmek için kullanılır.

driver.forward(): Bir sonraki sayfaya gitmek için kullanılır.

driver.refresh(): Sayfayı yenilemek için kullanılır.

driver.execute_script(script): Belirtilen JavaScript kodunu çalıştırmak için kullanılır.

driver.get_screenshot_as_file(filename): Tarayıcının ekran görüntüsünü belirtilen dosya adına kaydetmek için kullanılır.

driver.get_screenshot_as_png(): Tarayıcının ekran görüntüsünü PNG formatında döndürür.

driver.current_url: Geçerli sayfanın URL'sini döndürür.

driver.title: Geçerli sayfanın başlığını döndürür.

driver.page_source: Geçerli sayfanın kaynak kodunu döndürür.

driver.quit(): Tarayıcıyı kapatmak için kullanılır.
