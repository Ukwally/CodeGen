import qrcode

nome = 'Compras & Encomendas'
sobrenome = ''
telefone = '937829410'
telefone2 = '955876577'
email = 'lucianondumbo@gmail.com'
empresa = 'Compras & Encomendas'
cargo = 'Empresa'
site = 'https://www.instagram.com/Compras&Encomendas'
site2 = 'https://www.facebook.com/Compras&Encomendas'

#PHOTO;VALUE=uri:https://pegarFotoNoUploadQueUserFezNaNuvem.com
vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{sobrenome};{nome};;;
FN:{nome} {sobrenome}
ORG:{empresa}
TITLE:{cargo}
TEL;TYPE=CELL:{telefone}
TEL;TYPE=CELL:{telefone2}
URL:{site}
URL:{site2}
END:VCARD"""

qr = qrcode.make(vcard)
qr.save("qrVcard.png")


print('QR criado com sucesso')