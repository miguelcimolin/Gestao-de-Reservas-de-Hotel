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
