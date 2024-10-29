print("="*30)
print(" Executando split de dados ")
print("="*30)

def split_string_palavras(text):
    return text.split(" ")

texto = "Analise de dados relacionais."

print(split_string_palavras(texto))

token = split_string_palavras(texto)

# fazendo split dos dados 
def split_string_letras(text):
    texto = text.upper()
    for i in texto:
        print(i)
        
split_string_letras(texto)