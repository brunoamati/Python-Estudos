# and = e, ff = f/ tf = f/ ft = f/ tt = t
# or = ou, ff = f/ tf = t/ ft = t/ tt = t
# not = não, se entrada for false sai true e se entrar true sai false
# t = true e f = false

idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar? ' + str(resultado)
print(msg)

#Programa de disparo de alarme

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'alarme disparado? ' + str(alarme)
print(msg)

#dinheiro para compra

tem_din = False
tem_din = not tem_din
msg = 'Tem dinheiro? ' + str(tem_din)
print(msg)