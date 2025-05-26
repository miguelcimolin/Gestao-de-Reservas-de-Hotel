# Gestao-de-Reservas-de-Hotel

## Descrição

Este projeto consiste em um sistema de reservas de hotel que passou por uma atualização significativa para aplicar boas práticas de **Clean Code**.

O código inicial era procedural, pouco organizado e de difícil manutenção. A refatoração transformou a base em um código mais legível, modular e reutilizável, facilitando a manutenção e futuras evoluções do sistema.

## Objetivos

- Melhorar a clareza do código  
- Promover a reutilização de componentes  
- Organizar a estrutura do sistema em módulos bem definidos  
- Facilitar a manutenção e evolução do sistema  

## Uso

O sistema é utilizado via **terminal**, permitindo a gestão das reservas de forma simples e direta por meio de comandos.

## Estrutura do Projeto

O código atualizado está organizado em classes e módulos que seguem o princípio da responsabilidade única (SRP) e outras boas práticas de engenharia de software.

# Changelog - Refatoração do Sistema de Reservas

*Data:* 2025-05-21  
*Autor:* [miguelcimolin](https://github.com/miguelcimolin)
*Autor:* [gabrielsouzadg](https://github.com/gabrielsouzadg)

---

## Repositórios

- 🔄 *Código Original:* [Projeto-Final](https://github.com/miguelcimolin/Projeto-Final)  
- ✅ *Novo Código Refatorado:* [Gestao-de-Reservas-de-Hotel](https://github.com/miguelcimolin/Gestao-de-Reservas-de-Hotel)

---

## Visão Geral da Refatoração

> Refatoração completa do sistema original com foco em organização, reutilização de código, legibilidade e princípios de Clean Code.

---

## ✅ Alterações Realizadas

- ✅ Organização em estrutura de *pastas, **módulos* e *funções separadas*
- ✅ Criação da **classe Reserva** para representar dados com mais clareza
- ✅ Separação das funcionalidades em *módulos específicos* dentro da pasta services/
- ✅ Criação da pasta utils/ para *validações, cálculos e persistência de dados*
- ✅ Transformação de *blocos repetitivos* em funções *reutilizáveis e limpas*
- ✅ Nomes de variáveis refatorados para versões mais *descritivas e compreensíveis*
- ✅ Aplicação de princípios de *responsabilidade única (SRP)* em todas as funções
- ✅ Testes unitários implementados com o módulo padrão unittest, utilizando mock para isolar entradas e saídas.
- ✅ Cobertura total de testes de aproximadamente 85%

---

## 🧪 Descrição dos Testes Implementados

Os testes foram desenvolvidos utilizando o framework **unittest**, com uso extensivo de **unittest.mock** para simular interações do usuário, leituras e escritas em arquivos, e chamadas de validação.

### ✅ Testes Unitários por Funcionalidade

- **test_cadastro_reserva**  
  **Objetivo:** Verificar se uma nova reserva é cadastrada corretamente com entradas válidas.  
  **Verificações:**  
  - Mock de `input()` simula os dados do usuário.  
  - Mock de `carregar_reservas()` retorna lista vazia.  
  - Verifica se `salvar_reservas()` é chamado com a nova reserva.

- **test_alteracao_numero_pessoas**  
  **Objetivo:** Validar a alteração do número de pessoas em uma reserva existente.  
  **Verificações:**  
  - Mock de `input()` simula CPF, ID da reserva e novo número de pessoas.  
  - Reserva alterada tem o valor atualizado corretamente.

- **test_checkin**  
  **Objetivo:** Confirmar se uma reserva com status “R” é atualizada para “A” (Ativa) no check-in.  
  **Verificações:**  
  - Mock de `carregar_reservas()` retorna uma reserva com status “R”.  
  - Após o input, o status da reserva se torna “A”.

- **test_checkout**  
  **Objetivo:** Validar que uma reserva ativa (status “A”) muda para “F” (Finalizada) no check-out.  
  **Verificações:**  
  - Mock de `carregar_reservas()` retorna uma reserva com status “A”.  
  - Após o input, o status da reserva se torna “F”.

- **test_relatorio_status**  
  **Objetivo:** Confirmar que o relatório por status retorna apenas as reservas filtradas corretamente.  
  **Verificações:**  
  - `print()` é mockado e verificado com base na string "Total: N reserva(s).".

- **test_relatorio_valor_finalizado**  
  **Objetivo:** Calcular corretamente a soma de valores das reservas finalizadas (status “F”).  
  **Verificações:**  
  - Mock de reservas inclui ao menos uma com status "F".  
  - Verifica se o valor total exibido está correto.

- **test_relatorio_por_cpf**  
  **Objetivo:** Exibir corretamente todas as reservas associadas a um CPF informado.  
  **Verificações:**  
  - Mock de `input()` fornece o CPF.  
  - Mock de reservas retorna várias reservas com o mesmo CPF.  
  - Valida a contagem e exibição correta.

---

## 🛡️ Abordagem de Testes

- Todos os testes isolam dependências externas.  
- Arquivos reais não são lidos ou escritos durante a execução dos testes.  
- Entradas do usuário são simuladas com `patch('builtins.input')`.  
- Funções críticas como `carregar_reservas` e `salvar_reservas` são mockadas no local correto, ou seja, onde são importadas para garantir o isolamento.

---

## ⚙️ Como Executar os Testes

```bash
# Execute os testes com cobertura
python -m unittest discover -v
```

## Estrutura Modular do Novo Projeto

```plaintext
Gestao-de-Reservas-de-Hotel/
├── main.py
├── models/
│   └── reserva.py
├── services/
│   ├── cadastro.py
│   ├── checkin.py
│   ├── checkout.py
│   ├── alterar.py
│   └── relatorio.py
├── utils/
│   ├── arquivo.py
│   ├── calculos.py
│   └── validacoes.py
└── reservas.txt



