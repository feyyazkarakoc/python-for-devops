

names = ["Zehra", "Seda", "Zeynep", "Nur", "Züleyha"]
ages = [25, 28, 30, 27, 31]

zipped = zip(names, ages)
print(zipped) # <zip object at 0x000002114C6BBF00>  # zip, bir zip objesi döndürür, yazdırmak için list() kullanabiliriz
print(list(zipped)) # [('Zehra', 25), ('Seda', 28), ('Zeynep', 30), ('Nur', 27), ('Züleyha', 31)]

for i in zipped :
    print(i)

