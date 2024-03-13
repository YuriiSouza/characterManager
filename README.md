# Como usar a API

Este é um guia passo a passo para configurar e usar a API que foi criada.

## Configuração do Ambiente

### 1. Configuração do Ambiente Virtual

Para começar, você precisa configurar um ambiente virtual usando o `venv` do Python:

```bash
python -m venv .venv
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

Se caso ocorrer erro de permicao de scripts, rode o comando
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

### 3. Instalar o PostgreSQL

Certifique-se de ter o PostgreSQL instalado em seu sistema. Você pode baixá-lo em [postgresql.org](https://www.postgresql.org/download/).

### 4. Configurar o Arquivo .env

Copie o arquivo `.env.example` para `.env` e preencha as variáveis de ambiente com as informações de configuração do seu banco de dados PostgreSQL.

```bash
cp .env.example .env
```

## Instalação de Dependências

Em seguida, você precisa instalar as dependências necessárias para a API. Execute os seguintes comandos:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todas as dependências necessárias, juntamente com suas versões específicas, se aplicável.

## Iniciar a API

Agora que o ambiente está configurado e as dependências estão instaladas, você pode iniciar a API. Use o seguinte comando:

```bash
python app/main.py
```

## Acesso à API

Depois de iniciar a API, você pode acessá-la por meio da URL do servidor. Certifique-se de substituir `localhost` pelo endereço IP do seu servidor, se necessário.

```
http://localhost:5000
```

## Documentação Swagger

A documentação Swagger da API está disponível em:

```
http://localhost:5000
```

Agora você está pronto para começar a usar a API!
