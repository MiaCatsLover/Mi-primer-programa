meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "Una expresión para sonreir", 
            "AFK" : "Away from keyboard - Significa que no estoy en el compu! ", 
            "MINECRAFT" : " Juego Online de cubos , 15 años de Minecraft! ",
            "IDK" :"No sé",
            "POV" :"Point of view "
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()

if word in meme_dict.keys():
    print("\n")
    print(" Tu palabra si está en el diccionario! ")
    print("\n")
    print(" La definición es: ", meme_dict[word] )   
    
else:
   print(" Tu palabra no está en el diccionario! ")
   decision = input("¿Deseas agregar tu palabra al diccionario? (si o no): ").strip().lower()

if decision == "si":
    palabra = input("tu palabra eso:")
    significado = input("su significado es:")    
    meme_dict[palabra] = significado
    print("tu palabra a sido agregada.")
    print(meme_dict)

elif decision == "no":
    print("Muy bien")
else:
    print("Tu opción no ha sido reconocida, intenta otra vez.")
#   decision = input (" 1. Si y 2. No --- ")
#   if decision == 1:
#       meme_dict.append