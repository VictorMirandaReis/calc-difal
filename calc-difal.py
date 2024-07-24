print("-----------------------------------------")
print("Calcular Difal - Diferencial de Alíquotas")
print("-----------------------------------------")

interestadual = input("\nPreencha com a alíquota Interestadual em %: ")
interestadual_corrigido = float(interestadual.replace(',', '.'))

interna = input("Preencha com a alíquota Interna do Estado de destino em %: ")
interna_corrigido = float(interna.replace(',', '.'))

mercadoria = input("Preencha com o valor da mercadoria em R$: ")
mercadoria_corrigido = float(mercadoria.replace(',', '.'))

difal = interna_corrigido - interestadual_corrigido

valor = (mercadoria_corrigido * difal) / 100
valor_arredondado = round(valor, 2)

print("O valor do Difal a ser cobrado é: R$", valor_arredondado)

if valor_arredondado < 0:
    print("Por favor, conferir os valores inseridos!")