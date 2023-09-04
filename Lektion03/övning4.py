country = input("Ange ett land < ").lower()
nordic = ["sverige", "norge", "finland", "danmark", "island"]
uk = ["england", "nordirland", "skottland", "wales"]

if country in uk:
    print("Detta land är en del av Storbritanien")
elif country in nordic:
    print("Detta land är en del av Norden.")
else:
    print("ERROR! Detta land är inte en del av Norden eller Storbritanien")



