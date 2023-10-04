# Gerenciador de Recursos para Loja Online

Neste projeto, meu objetivo é desenvolver um script em Python para automatizar um processo específico de negócio. O objetivo é criar um bot que seja capaz de realizar tarefas repetitivas em um cenário fictício de processamento de pedidos em uma loja online. Minhas habilidades de desenvolvimento em Python e meu entendimento dos conceitos de automação de processos serão demonstrados neste desafio.

## Como Clonar e Testar o Projeto

Siga os passos abaixo para clonar o repositório e testar o programa:

1. Clone o repositório para o seu computador:

   ```bash
   git clone https://github.com/gabrielmango/gerenciador-recursos.git
   ```

2. Navegue para a pasta do projeto:

   ```bash
   cd seu-projeto
   ```

3. Crie um ambiente virtual Python (recomendado):

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS e Linux:

     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

6. Execute o arquivo __init__.py para criar o banco de dados:

   ```bash
   python __init__.py
   ```

7. Execute o arquivo main.py para iniciar o programa:

   ```bash
   python main.py
   ```

# Descrição do Projeto

Neste projeto, meu objetivo é demonstrar minhas habilidades em linguagem de programação Python. O sistema opera da seguinte maneira:

## Funcionamento

- Um timer é configurado para executar a função principal. Por padrão, o projeto inicia diariamente às 10:30.

- Um arquivo JSON localizado na pasta 'entrada_pedidos' é lido, e os dados do pedido são convertidos em um formato mais conveniente para o Python, ou seja, em um dicionário.

- O primeiro passo é verificar se o cliente já está cadastrado no banco de dados. Caso não esteja cadastrado, os dados pessoais são tratados e armazenados.

- Em seguida, os detalhes do pedido são buscados para validar a quantidade de peças disponíveis em estoque e confirmar o pedido de compra.

- O processo de entrega é então processado e registrado no banco de dados, juntamente com a lista de produtos no pedido.

- Após esse processo, uma nota de entrega contendo informações relevantes para a transportadora é gerada e salva em um arquivo .txt, que posteriormente é impresso.

## Objetivo

O objetivo principal do projeto é automatizar tarefas relacionadas à coleta de dados de pedidos, validação do cadastro do cliente, controle de estoque e gerenciamento da documentação de entrega.

No entanto, ainda existem algumas tarefas manuais necessárias, como atualizar o registro de entrada de estoque, imprimir a guia de entrega e configurar o timer para o funcionamento correto do sistema.

Este projeto está em constante desenvolvimento, e novas funcionalidades estão sendo adicionadas para aprimorar a automação e tornar o processo ainda mais eficiente.

## Bibliotecas Python Utilizadas

- [NumPy](https://numpy.org/doc/1.26/): NumPy é uma biblioteca fundamental para computação científica em Python, que oferece suporte a arrays multidimensionais e funções matemáticas de alto desempenho.

- [Schedule](https://schedule.readthedocs.io/en/stable/): Schedule é uma biblioteca para agendar tarefas em Python de forma simples e legível.

- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/): SQLAlchemy é uma biblioteca de mapeamento objeto-relacional (ORM) que facilita a interação com bancos de dados relacionais em Python.

- [Unidecode](https://pypi.org/project/Unidecode/): Unidecode é uma biblioteca que ajuda a transliterar texto Unicode em texto ASCII, útil para normalização de texto.


## Contribuindo

Se você está interessado em contribuir com o projeto, ficaremos felizes em receber sua ajuda. Para contribuir, siga os passos abaixo:

1. Faça um "Fork" deste repositório clicando no botão "Fork" no canto superior direito desta página. Isso criará uma cópia do repositório em sua própria conta.

2. Clone o repositório forkado para sua máquina local. Você pode fazer isso usando o comando git:

   ```
   git clone https://github.com/gabrielmango/gerenciador-recursos.git
   ```

   Substitua `seu-username` pelo seu nome de usuário do GitHub e `seu-fork` pelo nome do seu fork.

3. Crie uma nova branch para a sua feature, onde `feature-nova` deve ser substituído por um nome descritivo para a sua contribuição:

   ```
   git checkout -b feature-nova
   ```

4. Realize as mudanças que deseja fazer no projeto. Certifique-se de manter o código limpo e seguir as convenções de estilo do projeto.

5. Faça commit das suas mudanças com mensagens descritivas:

   ```
   git commit -m 'Adicione uma nova feature'
   ```

6. Envie suas alterações para o seu repositório fork no GitHub:

   ```
   git push origin feature-nova
   ```

7. Acesse a página do seu repositório fork no GitHub e clique no botão "New Pull Request" para criar um novo Pull Request. Certifique-se de descrever suas alterações de forma clara e concisa.

A equipe do projeto revisará seu Pull Request e poderá solicitar alterações adicionais antes de mesclar suas contribuições. Agradecemos por sua colaboração!

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Certifique-se de substituir as informações relevantes, como o título do projeto, a descrição, os links para a documentação das bibliotecas, seu nome de usuário no GitHub e outros detalhes específicos do seu projeto. Isso deve fornecer um README.md básico com todas as seções que você mencionou.