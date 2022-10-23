import qrcode, time
qr = qrcode.QRCode(1, border = 0, box_size = 1)
qr.add_data(input('Data: '))
qr.make(fit = 1)
img = qr.make_image()
w, h = img.size
data = list(img.getdata())
data = [[data[i+h*j] for i in range(w)] for j in range(h)]
res = []
blocks = ' ▀▄█'
for i in range(len(data)//2):
    res.append('')
    for j in range(len(data[i])):
        res[-1] += blocks[3-(data[i*2][j]//255+data[i*2+1][j]//255*2)]
if(not len(res)%2):
    res.append(''.join([blocks[0] if data[-1][i] else blocks[1] for i in range(len(data[-1]))]))
open(f'output-{time.time()}.txt', 'x', encoding = 'utf8').write('\n'.join(res))
input('Done')