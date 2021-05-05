from interrupteur import Interrupteur
from lampe import Lampe

l = Lampe()
i = Interrupteur()

print(i)
print(l)

print("le switch")
i.switch(l)

print(i)
print(l)

print("le switch")
i.switch(l)

print(i)
print(l)



#actionner interrupteur

#si allumé
#-> la lampe s'éteind

#else:
#-> la lampe s'allume