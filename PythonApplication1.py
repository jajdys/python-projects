import string
import getpass

def check_password(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    sila = 0
    remarks = ''

    if lower_alpha_count >= 1:
        sila += 1
    if upper_alpha_count >= 1:
        sila += 1
    if number_count >= 1:
        sila += 1
    if whitespace_count >= 1:
        sila += 1
    if special_char_count >= 1:
        sila += 1

    if sila == 1:
        remarks = "Twoje haslo jest fatalne. Zmien haslo tak szybko jak to mozliwe."
    elif sila == 2:
        remarks = "Twoje haslo nie nalezy do najlepszych. Powinienes zastanowic sie nad lepszym haslem."
    elif sila == 3:
        remarks = "Twoje haslo jest OK, ale moze byc o wiele silniejsze"
    elif sila == 4:
        remarks = "Twoje haslo jest trudne do zlamania. Mozesz zrobic je jeszcze silniejsze"
    elif sila == 5:
        remarks = "Niemozliwie trudne haslo do zlamania!! Anonymous nie maja szans odgadnac twojego hasla."

    print("|| Haslo posiada: ")
    print(f"|| male litery:   {lower_alpha_count} ")
    print(f"|| wielkie litery:   {upper_alpha_count} ")
    print(f"|| cyfry {number_count} ")
    print(f'|| spacje {whitespace_count} ')
    print(f"|| znaki specjalne {special_char_count} \n")
    print(f"|| Wynik hasla: {sila}/5")
    print(f"|| Zastrzezenia: {remarks}")

print("===== Witaj w silomierzu hasel =====")
while 1:
    choice = input("Czy chcesz sprawdzic sile twojego hasla? (y/n) : ")
    if 'y' in choice.lower():
        password = getpass.getpass("Wpisz haslo: \n")
        check_password(password)
    elif 'n' in choice.lower():
        print('Opuszczanie...')
        break
    else:
        print('Bledne wprowadzenie. Sprobuj ponownie')
    print()
