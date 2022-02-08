koordinatlar = dict()
sehirler = list()
maliyetler = dict()
mesafeler = dict()

kisa_yol = 0
kisa_yol_top = 1e10

ilk_sehir = 'a'
son_sehir = 'e'

def dosyaoku():
	with open('kordinat.txt','r') as f:
		for line in f:
			satir = line.strip().split(sep=' ')
			# print('satir:',satir)
			koordinatlar[satir[0]] = (int(satir[1]), int(satir[2]))

		print('koordinatlar:',koordinatlar)

	baslik = True
	with open('path.txt', 'r') as f:
		for line in f:
			satir = line.strip().split(sep=' ')
			# print('satir:', satir)

			if baslik:
				baslik = False
				for s in satir:
					sehirler.append(s)

				print('Sehirler:', sehirler)
				continue

			sehir = satir[0]
			for sira, maliyet in enumerate(satir[1:]):
				if int(maliyet) < 1:
					continue
				anahtar = (sehir, sehirler[sira])
				maliyetler[anahtar] = int(maliyet)

		print('Maliyetler:', maliyetler)

def mesafebul():
	# sehirlerin son_sehire olan mesafesini bulur.
	for sehir in sehirler:
		x1, y1 = koordinatlar[sehir]
		x2, y2 = koordinatlar[son_sehir]
		# print('sehir:', sehir, x1, y1, x2, y2)
		mesafe = ((x2 - x1)**2 + (y2 - y1)**2) ** .5
		mesafeler[sehir] = round(mesafe,2)

	print('Mesafeler:', mesafeler)
	print()
	print()


def komsu_sehirleri_bul(sehir):
	# gelen sehir icin, gidilebilecek sehirlerin listesini döndürür.
	bagli_sehirler = [shr2 for shr1, shr2 in maliyetler.keys() if sehir==shr1]
	print(sehir,' sehrine bagli sehirler:',bagli_sehirler)
	return bagli_sehirler

def toplam_maliyet_bul():
	for i in range(len(yollar)):
		yol = yollar[i]
		sehir_adedi = len(yol)
		toplambul = 0
		for j in range(sehir_adedi-1):
			ilk = yol[j]
			son = yol[j+1]
			anahtar = (ilk, son)
			toplambul += maliyetler[anahtar]
		# son şehrin kuş ucusu mesafesini de ekleyelim.
		toplambul += mesafeler[yol[-1]]
		toplam[i] = round(toplambul,2)

def kisa_yol_bul():
	kisa_yol = 0
	kisa_yol_top = 1e10

	for i in range(len(toplam)):
		if toplam[i] < kisa_yol_top:
			kisa_yol = i
			kisa_yol_top = toplam[i]
	return kisa_yol



def bas():
	print('Yollar:', yollar)
	print('Toplam:', toplam)
	print('Kısa yol', kisa_yol, toplam[kisa_yol])


dosyaoku()
mesafebul()

# Bağlı şehirleri test edelim
# for sehir in sehirler: komsu_sehirleri_bul(sehir)

yollar = list()
toplam = list()

komsu_sehirler = komsu_sehirleri_bul(ilk_sehir)
adet = len(komsu_sehirler)

kisa_yol = 0
kisa_yol_top = 1e10

for yol in range(adet):
	yollar.append([ilk_sehir, komsu_sehirler[yol]])
	anahtar = tuple(yollar[yol])
	top = round(maliyetler[anahtar] + mesafeler[komsu_sehirler[yol]])
	toplam.append([top])
	if top < kisa_yol_top:
		kisa_yol = yol
		kisa_yol_top = top


bas()

bitti = False
while not bitti:
	# kisa_yol için yeni şehri bulalım.
	sehir = yollar[kisa_yol][-1]
	komsu_sehirler = komsu_sehirleri_bul(sehir)
	for komsu_sehir in komsu_sehirler:
		if komsu_sehir in yollar[kisa_yol]:
			continue
		elif komsu_sehir == son_sehir:
			bitti = True
			yollar[kisa_yol].append(komsu_sehir)
			toplam_maliyet_bul()
			continue
		else:
			yollar[kisa_yol].append(komsu_sehir)
			toplam_maliyet_bul()
			kisa_yol = kisa_yol_bul()
			bas()
			break

print()
print('SONUÇ:')
print('En kısa yol:', yollar[kisa_yol])
print('En Kısa Mesafe:',toplam[kisa_yol])
