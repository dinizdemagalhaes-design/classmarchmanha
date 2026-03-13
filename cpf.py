cpf = int(input("Digite seu CPF: "))
cpf = cpf.replace(".", " ", "-")
if len(cpf) != 11:
        print ("CPF inválido")
else:
  
  
    if cpf == cpf[0] * 11:
        print ("CPF inválido")
    else: 
        soma = 0
        peso = 10
        for numero in cpf_numeros [:9]:
            soma += int(numero) * peso
            peso -= 1
        resto = soma % 11
        if resto < 2:
            digito1 == 0
        else:
            digito1 = 11 - resto
        print ("Primeiro dígito verificador:", digito1)



        
        soma = 0
        peso = 11
        for numero in cpf_numeros [:9] +str (digito1):
             soma += int(numero) * peso
             peso += 1
        resto = soma % 11
        if resto <2:
             digito2 = 11- resto      



        if cpf_numeros [-2:] == str (digito1) + str(digito2):
             print ("CPF válido")
        else:
             print ("CPF inválido")     
    
    


