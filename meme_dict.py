meme_dict = {
            "CREEPY": "Korkunç",
            "SHEESH": "onaylamamak",
            "CRINGE": "garip ya da utandırıcı bir şey",
}

print("Selamlar")
while True:
    soru1 = input("Anlamadığınız bir kelime yazınız. (hepsini büyük harfle yazınız):")
    
    
    if soru1 in meme_dict.keys():
        print(meme_dict[soru1])
        
    else:
        print("kelime sözlükte bulunmamaktadır.")
