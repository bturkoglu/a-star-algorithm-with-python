metin = "kara kara kartallar karlara kanat açarlara"
x = "ar"

boy = len(metin) - len(x) + 1
yer = 0
adet = 0
while yer < boy:
	for i in range(len(x)):
		if metin[yer + i] != x[i]:
			yer += i+1
			break
	else:
		adet += 1
		print(yer,'.karakterde bulundu.')
		yer += i + 1
print("Toplam: %i adet '%s' var." % (adet,x))
