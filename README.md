# Calculadora Difal

Calculadora simples para o Difal (Diferencial de Alíquotas) entre Estados brasileiros.

## Como funciona

O script [`calc-difal.py`](calc-difal.py) solicita ao usuário:
- Alíquota interestadual (%)
- Alíquota interna do estado de destino (%)
- Valor da mercadoria (R$)

Com esses dados, calcula o valor do Difal a ser cobrado.

## Como usar

1. Execute o script em um terminal:

   ```sh
   python calc-difal.py

## Melhorias

- Tornar o app executável
- Incluir cálculos do Fundo de Combate à Pobreza, IPI, frete e outras despesas acessórias.
