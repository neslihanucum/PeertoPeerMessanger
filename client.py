import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.11.214', 5555))
client.send("I am nesli too :')\n".encode())
from_server = client.recv(1024)
client.close()
print (from_server.decode())

"""
İlk olarak, socket.socket fonksiyonu ile bir soket nesnesi (client) oluşturulur. 
AF_INET parametresi, IPv4 adreslerini kullanacağımızı belirtirken, 
SOCK_STREAM parametresi TCP/IP protokolünü kullanacağımızı belirtir.
connect yöntemi ile belirtilen IP adresi ve port numarasına bağlantı isteği gönderilir. 
Bu örnekte, '192.168.11.214' IP adresine ve 5555 port numarasına bağlanır.
send yöntemi ile sunucuya "I am nesli too :')\n" mesajı gönderilir. 
Mesaj öncesinde encode yöntemiyle UTF-8 formatına dönüştürülmesi gerekmektedir.
recv yöntemi ile sunucudan gelen veri from_server değişkenine okunur. 
1024 parametresi, maksimum 1024 byte'lık bir veri alacağımızı belirtir.
Bağlantı close yöntemi ile kapatılır.
Son olarak, sunucudan gelen veri decode yöntemiyle UTF-8 formatından çıkarılır ve ekrana yazdırılır.
Bu kod, belirtilen sunucuya bağlanır, sunucuya bir mesaj gönderir ve sunucudan gelen yanıtı alır.
"""