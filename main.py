import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
       return
    if message.content.startswith('hello'):
       await message.channel.send(f'Merhaba {client.user}! ben bir botum!')
    elif  message.content.startswith("selam"):
       await message.channel.send("merhaba")
    elif  message.content.startswith("komutlar"):
       await message.channel.send("1-)iklim değişiklği nedenleri nedir 1 \n2-)iklim değişiklği nedenleri nedir 2 \n3-)iklim değişiklği nedenleri nedir 3 \n4-)kaynakça \n5-)iklim değişikliğinin sonuçları nedir 1 \n6-)iklim değişikliğinin sonuçları nedir 2 \n7-)iklim değişikliğinin sonuçları nedir 3 \n8-)iklim değişikliğinin sonuçları nedir 4 \n9-)iklim değişikliğinin sonuçları nedir 5 \n10-)iklim değişikliğinin sonuçları nedir 6 \n11-)iklim değişikliğinin sonuçları nedir 7 \n12-)iklim değişikliğinin sonuçları nedir 8 \n13-)bununla ilgili bir video atar mısın 1 \n14-)bununla ilgili bir video atar mısın 2 \n15-)bununla ilgili bir video atar mısın 3 \n16-)iklim değişiklğini bulan kişi kim? /evet/hayır/ \n17-)iklim değişikliği ile bir web sitesi atar mısın 1 \n18-)iklim değişikliği ile bir web sitesi atar mısın 2 \n19-)iklim değişikliği ile bir web sitesi atar mısın 3 \n20-)iklim değişikliği ile bir web sitesi atar mısın 4 \n21-) iklim değişikliği ile bir web sitesi atar mısın 5\n22-)iklim değişikliği ile bir web sitesi atar mısın 6 \n23-)iklim değişikliği ile ilgili bir görsel atar mısın 1 \n24-)iklim değişikliği ile ilgili bir görsel atar mısın 2 \n25-)iklim değişikliği ile ilgili bir görsel atar mısın 3 \n26-)iklim değişikliği ile ilgili bir görsel atar mısın 4 \n27-)iklim değişikliği ile ilgili bir görsel atar mısın 5 \n28-)iklim değişikliği ile ilgili bir görsel atar mısın 6 \n29-)iklim değişikliği ile ilgili bir görsel atar mısın 7 \n30-)iklim değişikliği ile ilgili bir görsel atar mısın 8 ")
      
    elif  message.content.startswith("nasılsın"):
       await message.channel.send("robotların duyguları olmaz :) şaka bir yana iyiyim :)")
    elif  message.content.startswith("iklim değişiklği nedenleri nedir 1"):
       await message.channel.send("Gelen güneş radyasyonundaki değişiklikler (Güneşin kendisindeki ya da Yerkürenin yörüngesindeki değişikliklere bağlı olarak)")
    elif  message.content.startswith("iklim değişiklği nedenleri nedir 2"):
       await message.channel.send("Güneş radyasyonunun yansıtılan kısmındaki değişiklikler (bu kısım albedo olarak adlandırılmaktadır ve bulut örtüsü, aerosoller denilen küçük parçacıklar ya da arazi örtüsündeki değişikliklere bağlı olarak değişebilmektedir)")
    elif  message.content.startswith("iklim değişiklği nedenleri nedir 3"):
       await message.channel.send("Yerküreden uzaya geri gönderilen uzun dalgalı radyasyondaki değişiklikler (sera gazı salımlarının atmosferdeki birikimlerine bağlı olarak). Bunların yanı sıra, rüzgarlar ve okyanus akıntılarının, Yerküre yüzeyi üzerindeki ısı dağılımında oynadıkları rol nedeniyle, iklim üzerinde önemli etkileri bulunmaktadır.")
    elif  message.content.startswith("kaynakça"):
       await message.channel.send("MGM(meteroloji genel müdürlüğü),vikipedia,youtube.nasa,TUA,iklim,world bank,iklim portal.")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 1"):
       await message.channel.send("İklim değişikliği nedeniyle çöller genişlerken, sıcak hava dalgaları ve orman yangınları daha yaygın hale gelmektedir.Kuzey Kutbu'nda artan ısınma donmuş toprakların erimesine, buzulların geri çekilmesine ve deniz buzu kaybına katkıda bulundu.")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 2"):
       await message.channel.send("Daha yüksek sıcaklıklar aynı zamanda daha yoğun fırtınalara, kuraklıklara ve diğer aşırı hava koşullarına neden olmaktadır")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 3"):
       await message.channel.send(" Dağlarda, mercan resiflerinde ve Kuzey Kutbu'nda yaşanan hızlı çevresel değişim, birçok canlı türünün yer değiştirmesine ya da neslinin tükenmesine neden olmaktadır")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 4"):
       await message.channel.send("İklim değişikliği insanları gıda ve su kıtlığı, artan seller, aşırı sıcaklar, daha fazla hastalık ve ekonomik kayıplarla tehdit etmektedir. İnsan göçü ve çatışmalar da bunun bir sonucu olabilir")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 5"):
       await message.channel.send(" Toplumlar, kıyı şeridinin korunması veya klimaya erişimin genişletilmesi gibi çabalarla iklim değişikliğine uyum sağlayabilir, ancak bazı etkiler kaçınılmazdır")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 6"):
       await message.channel.send("Yoksul ülkeler küresel emisyonların küçük bir kısmından sorumludur, ancak uyum sağlama konusunda en az yeteneğe sahiptirler ve iklim değişikliğine karşı en savunmasız durumdadırlar.")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 7"):
       await message.channel.send("Emisyonların azaltılması, fosil yakıtların yakılması yerine düşük karbonlu kaynaklardan elektrik üretilmesini gerektirmektedir")
    elif  message.content.startswith("iklim değişikliğinin sonuçları nedir 8"):
       await message.channel.send(" 2000'li yıllardan bu yana iklim değişikliği sözcüğünün kullanımı artmıştır")
    elif  message.content.startswith("bununla ilgili bir video atar mısın 1"):
       await message.channel.send("https://www.youtube.com/watch?v=aGYjEyHBUTA")
    elif  message.content.startswith("bununla ilgili bir video atar mısın 2"):
       await message.channel.send("https://www.youtube.com/watch?v=NIa68XXtYik")
    elif  message.content.startswith("bununla ilgili bir video atar mısın 3"):
       await message.channel.send("https://www.youtube.com/watch?v=sgIi3E7MzqA")
    elif  message.content.startswith("iklim değişikliğini bulan kişi kim?"):
       await message.channel.send("söyleyeyim mi")
       def check(m):
            return m.author == message.author and m.channel == message.channel and m.content.lower() in ["evet", "hayır"]
       try:
            reply = await client.wait_for("message", check=check, timeout=10.0)
            if reply.content.lower() == ("evet"):
                await message.channel.send("Jean-Pierre Perraudin'dir.")
            elif reply.content.lower() == ("hayır"):
                await message.channel.send("Tamam, söylemiyorum.")
       except Exception:
            await message.channel.send("Cevap vermedin, sonra tekrar sorarsın.")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 1"):
       await message.channel.send("https://iklim.gov.tr/")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 2"):
       await message.channel.send("https://science.nasa.gov › climate-change")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 3"):
       await message.channel.send("https://tua.gov.tr/tr/blog/dunya/iklim-degisikligi")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 4"):
       await message.channel.send("https://climateknowledgeportal.worldbank.org")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 5"):
       await message.channel.send("https://tr.wikipedia.org/wiki/%C4%B0klim_de%C4%9Fi%C5%9Fikli%C4%9Fi")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 6"):
       await message.channel.send("https://iklimportal.gov.tr")
    elif  message.content.startswith("iklim değişikliği ile bir web sitesi atar mısın 6"):
       await message.channel.send("https://iklimportal.gov.tr")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 1"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=http%3A%2F%2Ftektiklabilgielinde.saglik.gov.tr%2Fdepo%2Fsagligimyeni%2Fcevrevesaglik%2Ficerikbanner%2Fkucuk_resimler%2Fhsgm_resim_13.jpg&imgrefurl=https%3A%2F%2Ftektiklabilgielinde.saglik.gov.tr%2Fiklim-degisikligi-ve-etkileri.html&docid=Sn_87hPX8PNUtM&tbnid=8Ui6ju9lJ76CHM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECBcQAA..i&w=1140&h=760&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECBcQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 2"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fsurdurulebilirevren.com%2Fwp-content%2Fuploads%2F2024%2F05%2Fiklim-degisikligi-nedir.webp&imgrefurl=https%3A%2F%2Fsurdurulebilirevren.com%2Fiklim-degisikligi-nedir%2F&docid=U37NqOeLvzLHbM&tbnid=SdjkkWWwc5C6aM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECGcQAA..i&w=1280&h=769&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECGcQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 3"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fwww.ekolcevre.com%2Fuploads%2Fblog%2Fbig%2Fkuresel-iklim-degisikligi-nedir.webp&imgrefurl=https%3A%2F%2Fwww.ekolcevre.com%2Fblog%2Fkuresel-iklim-degisikligi-nedir&docid=HdIHMvD3kMh73M&tbnid=flxVsswCcoaUaM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECBQQAA..i&w=1280&h=800&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECBQQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 4"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fwww.ozguroner.dr.tr%2Fwp-content%2Fuploads%2F2021%2F08%2Fiklim-degisikligi.jpg&imgrefurl=https%3A%2F%2Fwww.ozguroner.dr.tr%2Fguncel-yazilar%2Fiklim-degisikligi.html&docid=lkmUAjYMylT_EM&tbnid=YdRdYuBLepqnZM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECEsQAA..i&w=775&h=516&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECEsQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 5"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fwww.ekolcevre.com%2Fuploads%2Fblog%2Fbig%2Fkuresel-iklim-degisikligi.webp&imgrefurl=https%3A%2F%2Fwww.ekolcevre.com%2Fblog%2Fkuresel-iklim-degisikliginin-nedenleri&docid=hgZtwgFrdZueNM&tbnid=zPchHOeuOZAy1M&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECGYQAA..i&w=1280&h=800&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECGYQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 6"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fgundemebakiscom.teimg.com%2Fcrop%2F1280x720%2Fgundemebakis-com%2Fuploads%2F2025%2F05%2Fiklim-5.jpg&imgrefurl=https%3A%2F%2Fwww.gundemebakis.com%2Fiklim-degisikligi-kuresel-dag-cayiri-ekosistemini-tehdit-ediyor&docid=O18DyOGJVh2OAM&tbnid=2wqvdYlnEzXvLM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECDsQAA..i&w=1280&h=720&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECDsQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 7"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fsupolitikalaridernegi.org%2Fwp-content%2Fuploads%2F2024%2F04%2Fiklim-degisikligi.jpeg&imgrefurl=https%3A%2F%2Fsupolitikalaridernegi.org%2F2024%2F04%2F19%2Fiklim-degisikligi-dunya-ekonomisini-fena-vuracak%2F&docid=Cs8S_8UOXvSCyM&tbnid=5j4R9Wn39jlpBM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECBEQAA..i&w=800&h=533&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECBEQAA")
    elif  message.content.startswith("iklim değişikliği ile ilgili bir görsel atar mısın 8"):
       await message.channel.send("https://www.google.com/imgres?q=iklim%20de%C4%9Fi%C5%9Fikli%C4%9Fi&imgurl=https%3A%2F%2Fwww.petroturk.com%2Fwp-content%2Fuploads%2F2023%2F11%2Fiklim-degisikligi.jpg&imgrefurl=https%3A%2F%2Fwww.petroturk.com%2Fyenilenebilir-enerji-haberleri%2Fturkiyede-iklim-degisikligi-algisi-raporu-yayinlandi&docid=WLgUcAJZnQvSmM&tbnid=Wj0A6UnHT4NdkM&vet=12ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECG0QAA..i&w=1394&h=628&hcb=2&ved=2ahUKEwj1o-_Dh7CNAxW-Q_EDHYTFMN4QM3oECG0QAA")
            
       






client.run("")