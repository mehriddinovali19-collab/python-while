while True:
    son1 = float(input("Birinchi sonni kiriting: "))
    son2 = float(input("Ikkinchi sonni kiriting: "))
    

    amal = input("Amalni tanlang (+, -, *, /): ")
    
    
    if amal == "+":
        natija = son1 + son2
    elif amal == "-":
        natija = son1 - son2
    elif amal == "*":
        natija = son1 * son2
    elif amal == "/":
        if son2 != 0:
            natija = son1 / son2
        else:
            natija = "Xato! Nolga bo'lish mumkin emas."
    else:
        natija = "Noma'lum amal!"

    print(f"Natija: {natija}")
    
    savol = input("Davom etasizmi? (ha/yo'q): ").lower()
    if savol != "ha":
        print("Dastur tugatildi. Xayr!")
        break
