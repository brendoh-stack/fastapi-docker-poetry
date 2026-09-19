# FastAPI + Docker + Poetry

Este repositório é autocontido e foi preparado para rodar uma aplicação FastAPI estruturada e isolada em um ambiente virtual gerenciado pelo Poetry dentro de um container Docker.

## 🚀 Pré-requisitos
Você precisa ter instalado em sua máquina:
* **Docker**
* **Docker Compose**

---

## 🛠️ Como Executar a Aplicação

### 1. Clonar o Repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO_GITHUB>
cd meu-projeto-fastapi
```

### 2. Construir e Subir o Ambiente
Execute o comando abaixo para construir a imagem Docker e iniciar o serviço em segundo plano (`-d`):
```bash
docker-compose up --build -d
```

A aplicação estará disponível em: [http://localhost:8000](http://localhost:8000)
A documentação interativa (Swagger) estará em: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🔄 3. Desenvolvimento e Live Reload
O Docker Compose mapeia volumes locais. Qualquer alteração salva no arquivo `app/main.py` refletirá instantaneamente na aplicação sem a necessidade de reiniciar o container.

### 🛑 4. Parar a Aplicação
Para derrubar e limpar os containers ativos:
```bash
docker-compose down
```
