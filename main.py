import qrcode
dados = "https://ukwally.github.io/Elisabeth"
qr = qrcode.make(dados)
qr.save("qrcode.png")

print('QR criado com sucesso')