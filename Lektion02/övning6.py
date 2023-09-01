

vanligkorv2=int(input("2 vanliga korvar: "))
vanligkorv3=int(input("3 vanliga korvar: "))

veganskkorv2=int(input("2 veganska korvar: "))
veganskkorv3=int(input("3 veganska korvar: "))

vk2=vanligkorv2*2
vk3=vanligkorv3*3
x=vk2 + vk3
vanligkorvpris= x/8*20.95
vanligkorvpaket= x/8

print("Priset för vanlig korv är",round(vanligkorvpris))
print("Så många packet behöver ni",vanligkorvpaket,)
print("Elever som vill ha 2 vanliga korvar",vanligkorv2)
print("Elever som vill ha 3 vanliga korvar",vanligkorv3)

vegkorv2=veganskkorv2*2
vegkorv3=veganskkorv3*3
y=vegkorv2+vegkorv3
vegkorvpris=y/4*34.95
vegkorvpaket=y/4

print("Priset för vegansk korv är",round(vegkorvpris))
print("Så många packet av veganska korvar behöver ni",vegkorvpaket,)
print("Elever som vill ha 2 veganska korvar",veganskkorv2)
print("Elever som vill ha 3 veganska korvar",veganskkorv3)

dryck=vanligkorv2+vanligkorv3+veganskkorv2+veganskkorv3
z=dryck*13.95

print("Ni behöver",dryck,"drycker till eleverna")
print("Det kommer och kosta",round(z),"kronor")
print("Total kostnaden kommer att vara",round(vanligkorvpris+vegkorvpris+z,1))





