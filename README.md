<h1 align="center"><span style="color: orange">LAB_PROJECT_DIO:</span> Aprimorando o sistema bancário com Python</h1>

<h3 align="center">Laboratório prático de desenvolvimento de software financeiro 💰</h3>
<h3 align="center">
=============================================<br>
===== SEJA BEM-VINDO AO BANCO PYTHON 🐍 =====<br>
=============================================<br>
</h3>

<br>

<div align="center">
<img src="https://cdn.lospec.com/gallery/piggy-bank-132881.gif" width="240px">
</div>

<br><br>

<div align="center">

# Objetivo geral e Desafio

"Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: **cadastrar usuário (cliente)** e **cadastrar conta bancária**." <br>

"Precisa deixar o código mais modularizado. Para isso, precisa criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do sistema, precisa criar duas novas funções: criar usuário (cliente do banco) e criar conta conrrente (vincular com usuário)." <br>

</div>

<br><br>

# Teste o projeto você mesmo!

Você pode testar de duas maneiras:

1) Git clone:
```bash
git clone "https://github.com/JeffsHenrique/banco-python-lab-dio.git"
```

Depois, basta abrir o terminal:
```bash
python banco.py
```

ou

```bash
banco.py
```

2) Copie/cole o código dentro de [`banco.py`](banco.py)

<br><br>

# Funcionalidades do projeto

- [Depósito](#d-depósito)
- [Saque](#s-saque)
- [Extrato](#e-extrato)
- [Cadastrar Usuário](#1-cadastrar-usuário)
- [Criar Conta](#2-criar-conta)
- [Filtrar Usuários](#3-filtrar-usuários)
- [Listar Contas](#4-listar-contas)
- [Sair](#q-sair)

## Separação em funções

"Deve-se criar funções para todas as operações do sistema." <br>
"Para exercitar o que foi aprendido no módulo, cada função vai ter uma regra na passagem de argumentos." <br>
"O retorno e a forma como serão chamadas pode ser definida da maneira que [eu] achar melhor." <br>

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[d] Depósito</span>](#funcionalidades-do-projeto)

### V1
"Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário. Dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato"

### V2
[x] - "A função depósito deve receber os argumentos apenas por posição (positional only)." <br>
[x] - "**Sugestão de argumentos:** saldo, valor, extrato." <br>
[x] - "**Sugestão de retorno:** saldo e extrato." <br>

</div>

### Outputs:

Depósito realizado:

```
informe o valor do depósito: 1000
>>> Depósito realizado: R$ 1000.00

>>> Saldo atual: 1000.00
```

<br><br>

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[s] Saque</span>](#funcionalidades-do-projeto)

### V1
"O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato."

### V2
[x] - "A função saque deve receber os argumentos apenas por nome (keyword only)" <br>
[x] - "**Sugestão de argumentos:** saldo, valor, extrato, limite, numero_saques, limite_saques." <br>
[x] - "**Sugestão de retorno:** saldo e extrato." <br>

</div>

### Outputs:

Saque efetuado:

```
informe o valor do saque: 500
>>> Saque realizado: R$ 500.00

>>> Saldo atual: 500.00
```

<br>

Limite de saque excedido:
```
informe o valor do saque: 800
Falha! O valor do saque excede o limite permitido de R$ 500.00.
>>> Saldo atual: 0.00
```

<br>

Saques diários excedidos:
```
informe o valor do saque: 154
Número de saques diários excedidos. Não é possível realizar mais saques.
```

<br>

Saldo insuficiente para saque:
```
informe o valor do saque: 10
Falha! Você não tem saldo suficiente para realizar essa operação.
>>> Saldo atual: 0.00
```

<br><br>

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[e] Extrato</span>](#funcionalidades-do-projeto)

### V1
"Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: <span>Não foram realizadas movimentações.</span> Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: R$ 1500.45"

### V2
[x] - "A função extrato deve receber os argumentos por posição e nome (positional only e keyword only)." <br>
[x] - "**Argumentos posicionais:** saldo." <br>
[x] - "**Argumentos nomeados:** extrato." <br>

</div>

### Outputs

Extrato:

```
================ EXTRATO ================
>>> Depósito realizado: R$ 1500.00
>>> Saque realizado: R$ 500.00
>>> Saque realizado: R$ 500.00


Saldo: R$ 500.00
==========================================
```

<br>

Banco sem movimentações:
```
================ EXTRATO ================
Não foram realizadas movimentações.

Saldo: R$ 0.00
==========================================
```

<br><br>

<div align="center">

## [<span style="color:rgb(231, 188, 44)">[1] Cadastrar Usuário</span>](#funcionalidades-do-projeto)

[x] - "O programa deve armazenar os usuários em uma lista." <br>
[x] - "Um usuário é composto por: **nome, data de nascimento, CPF e endereço**." <br>
[x] - "O endereço é uma *string* com o formato: `logradouro, número - bairro - cidade/sigla estado`." <br>
[x] - "Deve ser armazenado somente os números do CPF." <br>
[x] - "Não pode cadastrar 2 usuários com o mesmo CPF." <br>

</div>

### Outputs

Usuário cadastrado:
```
Informe o CPF (somente números): 12345678900
Informe o nome completo: Jeffs Henrique
informe a data de nascimento: 15-04-1950
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Brasil/Terra
====================================================================================================
USUÁRIO CADASTRADO COM SUCESSO! SEJA BEM-VINDO, JEFFS HENRIQUE!
```

<br>

CPF Inválido:
```
Informe o CPF (somente números): 454.454.454-44
CPF inválido! Por favor, tente novamente.
```

<br>

CPF em branco:
```
Informe o nome completo: 
CPF em branco! Por favor, tente novamente.
```

Também se aplica ao nome.

<br>

CPF já existe:
```
Informe o CPF (somente números): 12345678900
Ja existe um usuário com esse CPF!
```

<br><br>
<div align="center">

## [<span style="color:rgb(231, 188, 44)">[2] Criar Conta</span>](#funcionalidades-do-projeto)

[x] - "O programa deve armazenar contas em uma lista." <br>
[x] - "Uma conta é composta por: **agência, número da conta e usuário**." <br>
[x] - "O número da conta é sequencial, iniciando em 1." <br>
[x] - "O número da agência é fixo: `0001`." <br>
[x] - "O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário." <br>

</div>

### Outputs

Conta criada:
```
>>> Conta cadastrada com sucesso!

>>> Agência: 0001 || Conta: 1 || Titular: Jeffs Henrique
```

<br>

CPF inválido:
```
Informe o CPF do usuário (somente números): 123.456.789-00
CPF inválido! Por favor, tente novamente.
```

<br>

Usuário não encontrado:
```
Informe o CPF do usuário (somente números): 12345678911
Falha ao criar conta! O usuário não existe.
```

<br><br>
<div align="center">

## [<span style="color:rgb(231, 188, 44)">[3] Filtrar Usuários</span>](#funcionalidades-do-projeto)

Função para filtrar um usuário no banco. Mostra o usuário cadastrado a partir do CPF, além de retornar a quantidade de contas que o usuário possui.

</div>

### Outputs

Usuário filtrado:
```
Informe o CPF do usuário (somente números): 12345678900
Nome: Jeffs Henrique - CPF: 12345678900 - Quantidade de contas: 1
```

<br>

CPF inválido:
```
Informe o CPF do usuário (somente números): 123.456.789-00
CPF inválido! Por favor, tente novamente.
```

<br>

Usuário não encontrado:
```
Informe o CPF do usuário (somente números): 2345678901
Usuário não encontrado.
```

<br>

Não há usuários cadastrados:
```
Nenhum usuário cadastrado
```

<br><br>
<div align="center">

## [<span style="color:rgb(231, 188, 44)">[4] Listar Contas</span>](#funcionalidades-do-projeto)

Função para mostrar todas as contas cadastradas no banco. Retorna a Agência, Conta e o Nome do usuário (titular da conta). 

</div>

### Outputs

Contas criadas:
```
Agência: 1 || Conta: 0001 || Titular: Jeffs Henrique
Agência: 2 || Conta: 0002 || Titular: Jeffs Henrique
Agência: 3 || Conta: 0003 || Titular: John Doe
```

<br>

Nenhuma conta foi criada:
```
Nenhuma conta criada.
```

<br><br>
<div align="center">

## [<span style="color:rgb(231, 188, 44)">[q] Sair</span>](#funcionalidades-do-projeto)

Função que para o programa.

</div>

### Outputs

Saída:
```
==============================================
=== OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS! ===
==============================================
```

<br><br>

