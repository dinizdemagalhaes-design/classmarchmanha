pesokg = float(input ("Digite o peso de Lucas: "))
meta_agua = (pesokg * 15) /250

if  type(meta_agua) != int:
    meta_agua += 1

 

print ("Digite copo de agua em  é ", round(meta_agua, 0)  )





outra respçosta

pesokg = float(input ("Digite o peso de Lucas: "))
meta_agua = (pesokg * 15) //250
copo = meta_agua +1



print ("Digite copo de agua em  é ", round(copo,0)  )
