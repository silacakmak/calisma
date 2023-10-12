a=str(input("kelime gir:"))
unlu={"a","e","ı","i","o","ö","u","ü"}
index=0
for i in range(len(a)):
    if a[i] in unlu:
        index=index+1
    i=i+1
print(index,"tane ünlü var")
