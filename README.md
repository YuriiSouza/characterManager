# Como usar a API

Este é um guia passo a passo para configurar e usar a API que foi criada.

## Configuração do Ambiente

### 1. Configuração do Ambiente Virtual

Para começar, você precisa configurar um ambiente virtual usando o `venv` do Python:

```bash
python3 -m venv .venv
```

### 2. Ativar o Ambiente Virtual

Depois de configurar o ambiente virtual, você precisa ativá-lo. Use os comandos abaixo, dependendo do seu sistema operacional:

#### Mac / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

## Instalação de Dependências

Em seguida, você precisa instalar as dependências necessárias para a API. Execute os seguintes comandos:

```bash
pip install python-dotenv
pip install Watchdog
pip install Flask
```

## Iniciar a API

Agora que o ambiente está configurado e as dependências estão instaladas, você pode iniciar a API. Use o seguinte comando:

```bash
flask --app api run
```

## Acesso à API

Depois de iniciar a API, você pode acessá-la por meio da URL do servidor. Certifique-se de substituir `localhost` pelo endereço IP do seu servidor, se necessário.

```
http://localhost:5000
```

## Documentação Swagger

A documentação Swagger da API está disponível em:

```
http://localhost:5000/swagger
```

Agora você está pronto para começar a usar a API!
