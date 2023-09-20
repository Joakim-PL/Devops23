def km_to_miles(dist):
    return dist * 0.6214


def miles_to_km(dist):
    return dist * 1.6093


user = input("Ange distans > ").strip().split()
if len(user) == 2:
    dis_str, unit = user

    try:
        dis = float(dis_str)
        unit = unit.lower()

        if unit == 'km':
            miles = km_to_miles(dis)
            print(dis, "km motsvarar", miles, "miles")

        elif unit == 'miles':
            km = miles_to_km(dis)
            print(dis, "motsvarar", km)

        else:
            print("Ogiltig enhet")

    except ValueError:
        print("Ogiltigt inmatning")

else:
    print("Ogiltig inmatning")
