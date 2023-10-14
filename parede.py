larg = float(input("qual a largura da parede?"))
altu = float(input("qual a altura da parede?"))
area = larg * altu

print("a dimensão da sua parede é {}x{} e sua area é de {}m2.".format(larg, altu, area))
tinta = area / 2
print("para pintar a parede, voce vai precisar de {}l de tinta.".format(tinta, area))