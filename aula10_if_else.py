n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

m = (n1 + n2)/2
print('A sua média foi{:.1f}'.format(m))
if m > 6:
    print('Sua media foi boa!')
else:
    print('Sua media foi ruim!')

print('PARABENS!' if m >= 7 else 'ESTUDE MAIS!')