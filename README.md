<h1>Telegram Python Bot</h1>

<p>Bu proje, Python kullanılarak geliştirilmiş basit bir <strong>Telegram Bot</strong> uygulamasıdır.<br>
Kullanıcıdan komutlar alır ve yanıt verir. Ayrıca görsel gönderme ve basit mesaj yönetimi gibi özellikler içerir.</p>

<h2>Özellikler</h2>

<ul>
<li><code>/start</code> komutu ile hoşgeldin mesajı ve fotoğraf gönderimi</li>
<li><code>/test</code> komutu için hazırlık (geliştirme aşamasında)</li>
<li><code>/bos</code> ve <code>/hakkinda</code> gibi ek komutlar</li>
<li>Zaman damgalı kayıt sistemi</li>
<li><code>token.txt</code> dosyasından gizli bot token okuma</li>
<li>Basit, geliştirilebilir bot yapısı</li>
</ul>

<h2>Gereksinimler</h2>

<ul>
<li>Python 3.7 veya üstü</li>
<li>python-telegram-bot kütüphanesi</li>
</ul>

<p>Kurmak için:</p>

<pre><code>pip install python-telegram-bot</code></pre>

<h2>Kullanım</h2>

<ol>
<li>Bot token'ınızı bir <code>token.txt</code> dosyasına kaydedin.</li>
<li>Aşağıdaki gibi dosya yapınız olsun:</li>
</ol>

<pre><code>Telegram-Python/
├── token.txt
├── hosgeldin.png
└── bot.py
</code></pre>

<p>Botu çalıştırmak için:</p>

<pre><code>python bot.py</code></pre>

<h2>Bot Komutları</h2>

<table>
<thead>
<tr>
<th>Komut</th>
<th>Açıklama</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/start</code></td>
<td>Hoşgeldin mesajı ve resim gönderir</td>
</tr>
<tr>
<td><code>/test</code></td>
<td>Test komutu (boş şablon)</td>
</tr>
<tr>
<td><code>/bos</code></td>
<td>(Geliştirme aşamasında)</td>
</tr>
<tr>
<td><code>/hakkinda</code></td>
<td>(Geliştirme aşamasında)</td>
</tr>
</tbody>
</table>

<h2>Açıklamalar</h2>

<ul>
<li><strong>start</strong> fonksiyonu, kullanıcıya bir "Merhaba" mesajı ve ardından <code>hosgeldin.png</code> resmini gönderir.</li>
<li><strong>test</strong>, <strong>content1</strong>, <strong>content</strong> ve <strong>inp</strong> fonksiyonları şablon olarak bırakılmıştır (geliştirmeye açık).</li>
<li><code>token.txt</code> dosyası içinde yalnızca Bot Token bulunmalıdır.</li>
</ul>

<p>Örnek <code>token.txt</code> içeriği:</p>

<pre><code>123456789:ABCDefGHIjklMNOpQRstUVwxyZ</code></pre>

<h2>Koddan Parçalar</h2>

<h3>Start Komutu:</h3>

<pre><code>
def start(update, context):
    update.message.reply_text("Merhaba hoşgeldiniz")
    tests = open('hosgeldin.png', 'rb')
    time.sleep(3)
    update.message.reply_photo(tests)
</code></pre>

<h3>Botu Başlatmak:</h3>

<pre><code>
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("test", test))
disp.add_handler(telegram.ext.CommandHandler("bos", content1))
disp.add_handler(telegram.ext.CommandHandler("hakkinda", content))

updater.start_polling()
updater.idle()
</code></pre>

<h2>Katkı Sağlama</h2>

<ol>
<li>Fork oluşturun</li>
<li>Yeni bir branch açın (<code>feature/özellik</code>)</li>
<li>Geliştirmenizi yapın</li>
<li>Pull Request gönderin</li>
</ol>

<h2>Lisans</h2>

<p>Bu proje açık kaynaklıdır. Herkes kullanabilir ve geliştirebilir.</p>
