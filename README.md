# Consumindo dados da API de Buzzmonitor com Apache Airflow

<img src="src/buzzmonitor-logo.png" width="100%">

# Introdução

## O que é o Buzzmonitor?

Buzzmonitor é uma ferramenta de gerenciamento de mídias sociais e CRM. 

Utiliza inteligência artificial para monitorar o desempenho das marcas nas redes sociais e possibilidades de análise e comparação com concorrentes usando diversas métricas.

## Sobre a API

Diferente do projeto de extração com Lambda da [API de Brandwatch](https://github.com/macielf1994/brandwatch-api-extract) que é uma API páginada trazendo cinco mil objetos por requisição, a API de Buzzmonitor é uma API de Scroll e retorna até mil objetos por requisição que for feita num intervalo de até sessenta segundos entre uma chamada e outra até o fim scroll. Caso entre uma chamada e outra leve mais do que sessenta segundos o scroll fecha e temos que refazer as chamadas desde o inicio.

A API tem dois endpoints.

Tickets: se um usuário fala com a página, digamos três vezes em um dia, o Buzzmonitor criará um único ticket contemplando os 3 atendimentos associando a esse usuário.

Posts: no endpoint de posts é possível recuperar todas as publicações e tickets do projeto no Buzzmonitor.

Utilizaremos o endpoint de posts.

# O que utilizaremos?

**Apache Airflow**

Poderiamos provisionar o recurso da AWS, Amazon Managed Workflows for Apache Airflow (MWAA) com o CDK. Mas por ser um projeto de teste iremos utilizar o Airflow em uma instância EC2 já que os custos serão bem menores considerando o tamanho do projeto.