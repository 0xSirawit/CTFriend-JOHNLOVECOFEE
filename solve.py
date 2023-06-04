encoded_text = "JOHNLOVEJOHNJOHNJOHNLOVEJOHNJOHNJOHNLOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVEJOHNJOHNLOVECOFFEECOFFEEJOHNLOVEJOHNCOFFEEJOHNCOFFEELOVECOFFEECOFFEECOFFEECOFFEELOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVEJOHNCOFFEEJOHNCOFFEELOVECOFFEEJOHNLOVECOFFEECOFFEEJOHNCOFFEELOVECOFFEECOFFEEJOHNCOFFEELOVECOFFEELOVECOFFEECOFFEELOVEJOHNCOFFEELOVECOFFEELOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVEJOHNCOFFEEJOHNCOFFEELOVECOFFEEJOHNLOVEJOHNCOFFEELOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVEJOHNCOFFEEJOHNCOFFEELOVECOFFEEJOHNLOVECOFFEECOFFEEJOHNLOVECOFFEECOFFEECOFFEELOVECOFFEELOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVECOFFEECOFFEECOFFEECOFFEELOVECOFFEECOFFEELOVEJOHNJOHNCOFFEELOVECOFFEECOFFEECOFFEECOFFEELOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVEJOHNCOFFEECOFFEECOFFEELOVECOFFEEJOHNCOFFEECOFFEELOVEJOHNJOHNJOHNLOVEJOHNJOHNJOHNLOVEJOHNCOFFEECOFFEELOVECOFFEECOFFEEJOHNJOHNCOFFEEJOHNLOVECOFFEEJOHNJOHNCOFFEELOVECOFFEEJOHNCOFFEELOVECOFFEELOVECOFFEECOFFEECOFFEELOVECOFFEECOFFEECOFFEELOVECOFFEECOFFEEJOHNLOVECOFFEEJOHNCOFFEELOVECOFFEE"
morse_code_dict = { '.-':'A', '-...':'B','-.-.':'C', '-..':'D', '.':'E','..-.':'F', '--.':'G', '....':'H','..':'I', '.---':'J', '-.-':'K','.-..':'L', '--':'M', '-.':'N','---':'O', '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T','..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', '--..':'Z','.----':'1', '..---':'2', '...--':'3','....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9','-----':'0', '--..--':', ', '.-.-.-':'.','..--..':'?', '-..-.':'/', '-....-':'-','-.--.':'(', '-.--.-':')', '..--.-':'_'}
morse_code_result_list = []
decode_text = []
for i in range(len(encoded_text)):
    if encoded_text[i] == "J":morse_code_result_list.append("-"); i = i+3
    if encoded_text[i] == "L":morse_code_result_list.append("/"); i = i+3
    if encoded_text[i] == "C":morse_code_result_list.append("."); i = i+5
morse_code = ''.join(str(x) for x in morse_code_result_list).split("/")
for i in range(len(morse_code)): decode_text.append(morse_code_dict[morse_code[i]])
print("CTFr{"+''.join(str(x) for x in decode_text).lower()+"}")
