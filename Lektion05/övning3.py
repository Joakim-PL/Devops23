fornamn = [" Maria ", " Erik ", " Karl "]
efternamn = [" Svensson ", " Karlsson ", " Andersson "]

for fname in fornamn:
    for lname in efternamn:
        fullt_namn = fname.strip() + lname.strip()
        print(fullt_namn)
