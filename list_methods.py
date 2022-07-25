lando_2021_results = [4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]
#sort(), reverse() and count() methods
lando_2021_results.sort()
print(lando_2021_results)
print(lando_2021_results.count(5))
lando_2021_results.reverse()
print(lando_2021_results)
lando_2021_results.sort(reverse=False)
print(lando_2021_results)
print(id(lando_2021_results))

iplaring = ['sariq','zangor','qizil']
iplaring2 = ['qizil','sariq','zangor']
if iplaring == iplaring2:
    print("Ikkalasi ham teng")
else:
    print("Teng Emas")

if iplaring is iplaring2:
    print("IS ning bosimi Ikkalasi ham teng")
else:
    print("ISning bosimi Teng Emas")

iplaring3 = iplaring
if iplaring == iplaring3:
    print("Teng")
else:
    print("Teng Emas Dostim")