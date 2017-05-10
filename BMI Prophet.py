while True:
    weight_kg=int(input("Tell me your weight in kg: "))
    height_cm=int(input("Tell me your height in cm: "))
    height_m=height_cm/100
    BMI=weight_kg/(height_m**2)

    if BMI<16:
        print("Omfg, you are severely underweight")
    elif 16<=BMI<18.5:
        print("You are underweight. Somebody give this kid a pie.")
    elif 18.5<=BMI<25:
        print("Normal. Just ordinary.")
    elif 25<=BMI<=30:
        print("Overweight. Diettime.")
    elif BMI>30:
        print("Bad news, Blob. You get obesity")

