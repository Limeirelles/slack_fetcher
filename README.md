# Slack Message Fetcher

Projeto para capturar e exibir mensagens de um canal específico do Slack, utilizando a API oficial do Slack.

## 🚀 Visão geral

Este projeto faz uma requisição para a API `conversations.history` do Slack e exibe as mensagens mais recentes de um canal determinado. É útil para integrar histórico de conversas em dashboards, relatórios ou outros sistemas internos.

## 🛠️ Tecnologias utilizadas

* Python
* Requests (HTTP library)
* API do Slack

## ⚙️ Configuração e execução

1. **Clone o repositório:**

```bash
git clone https://github.com/Limeirelles/slack_fetcher.git
cd slack_fetcher
```

2. **Crie e configure o arquivo `.env`:**

O projeto utiliza variáveis de ambiente para proteger credenciais sensíveis. Crie um arquivo `.env` na raiz do projeto com o seguinte formato:

```env
SLACK_BOT_TOKEN=seu_token_aqui
CHANNEL_ID=seu_channel_id_aqui
```

> 🔒 **Importante:** O arquivo `.env` está no `.gitignore`, garantindo que não seja enviado para o repositório.

3. **Instale as dependências:**

Recomenda-se usar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate    # (Windows)

pip install -r requirements.txt
```

> Obs.: Caso o arquivo `requirements.txt` ainda não exista, você pode instalar manualmente:
>
> ```bash
> pip install requests python-dotenv
> ```

4. **Execute o script:**

```bash
python fetch_messages.py
```

## 📄 Estrutura esperada

* `.env` ➔ Arquivo local para armazenar token e ID do canal
* `.gitignore` ➔ Arquivo para evitar vazamento de credenciais
* `fetch_messages.py` ➔ Script principal para buscar mensagens
* `requirements.txt` ➔ Lista de dependências (opcional)

## ✅ Checklist de segurança

* [x] O `.env` está protegido e listado no `.gitignore`
* [x] Nenhuma credencial sensível está comitada
* [x] O repositório segue boas práticas de segurança

## 🤝 Contribuição

Fique à vontade para abrir *issues* ou enviar *pull requests* caso tenha melhorias ou sugestões!

## 📬 Contato

Desenvolvido por Limeirelles.

* GitHub: [@Limeirelles](https://github.com/Limeirelles)
