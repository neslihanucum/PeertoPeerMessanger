import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('192.168.11.205', 5555))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(1024)
    if not data: break
    from_client += data.decode('utf8')
    print (from_client)
    conn.send("I am nesli\n".encode())
  conn.close()
print ('nesli disconnected and shutdown')

"""
Bu kod, bir TCP/IP sunucusu oluşturmak için Python soket kütüphanesini kullanır. 
İstemci tarafından gelen bağlantıları kabul eder ve gelen verileri okurken istemciye yanıt gönderir.
İşleyişi şu şekildedir:
İlk olarak, socket.socket fonksiyonu ile bir soket nesnesi (serv) oluşturulur. 
AF_INET parametresi, IPv4 adreslerini kullanacağımızı belirtirken, 
SOCK_STREAM parametresi TCP/IP protokolünü kullanacağımızı belirtir.
Ardından, bind yöntemi ile soketin IP adresi ve port numarası atanır. 
'192.168.11.205' IP adresi ve 5555 port numarası kullanılarak bağlantılar dinlenecektir.
listen yöntemi ile gelen bağlantıları dinlemeye başlar. 
5 parametresi, eşzamanlı olarak kabul edilebilecek bağlantı sayısını belirtir.
Sonsuz bir döngü başlar ve accept yöntemi ile istemciden gelen bağlantıyı kabul eder. 
Bağlantı başarıyla kabul edildiğinde, conn ve addr değişkenlerine bağlantı nesnesi 
ve istemcinin IP adresi atanır.
İkinci bir sonsuz döngü başlar ve recv yöntemi ile 
istemciden gelen veriyi data değişkenine okur. Eğer veri yoksa döngüden çıkılır.
Gelen veri utf8 formatında from_client değişkenine eklenir ve ekrana yazdırılır.
conn üzerinden send yöntemi ile istemciye "I am nesli" mesajı gönderilir. 
Mesaj öncesinde encode yöntemiyle UTF-8 formatına dönüştürülmesi gerekmektedir.
İç içe bulunan sonsuz döngülerden çıkıldığında, bağlantı kapatılır (close yöntemi ile).
Dıştaki sonsuz döngü devam eder ve tekrar bağlantılar dinlenmeye devam eder.
Sonsuz döngüden çıkıldığında "nesli disconnected and shutdown" mesajı ekrana yazdırılır
"""