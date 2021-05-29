arquivo = open("etapa4-2.txt","r")
lines = arquivo.readlines()
arquivo.close()
#print(lines)
somaTestes = 0
for i in lines:
    somaTestes+=float(i.replace("\n",""))
print(somaTestes)

