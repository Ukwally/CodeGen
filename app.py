import qrcode

nome = 'Beatriz paula'
sobrenome = 'Mafuta'
telefone = '941487430'
email = 'beatriz@gmail.com'
empresa = 'eatrlma'
cargo = 'CEO'
site = 'https://www.instagram.com/beatrizpaula'

#PHOTO;VALUE=uri:https://pegarFotoNoUploadQueUserFezNaNuvem.com
vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{sobrenome};{nome};;;
FN:{nome} {sobrenome}
ORG:{empresa}
TITLE:{cargo}
TEL;TYPE=CELL:{telefone}
EMAIL:{email}
URL:{site}
END:VCARD"""

qr = qrcode.make(vcard)
qr.save("qrVcard.png")


print('QR criado com sucesso')