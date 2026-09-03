# 🚀 DevOps Project

Projeto prático desenvolvido para aplicar conceitos e ferramentas de **DevOps**, construindo progressivamente um fluxo de desenvolvimento, containerização, deploy, automação e observabilidade.

> 🚧 **Projeto em desenvolvimento.**

## 🎯 Objetivo

Construir um ambiente DevOps utilizando uma aplicação **Python/Flask** como base, priorizando ferramentas **open-source** e infraestrutura em **AWS EC2**.

O projeto será evoluído por etapas, incorporando novas tecnologias conforme cada conceito for estudado e implementado.

## 🛠️ Tecnologias

| Tecnologia     | Finalidade      |
| -------------- | --------------- |
| Python / Flask | Aplicação       |
| Gunicorn       | Servidor WSGI   |
| Docker         | Containerização |
| Git / GitHub   | Versionamento   |
| AWS EC2        | Infraestrutura  |
| Prometheus     | Monitoramento   |
| Grafana        | Visualização    |

## 📦 Aplicação

A API possui atualmente os seguintes endpoints:

`GET /` — Endpoint principal

`GET /health` — Health check da aplicação

## 🐳 Executando com Docker

**Build da imagem:**

```bash
docker build -t devops-projeto .
```

**Executar o container:**

```bash
docker run -p 5000:5000 devops-projeto
```

A aplicação estará disponível em:

```text
http://localhost:5000
```

## 🗺️ Roadmap

* [x] Desenvolvimento da aplicação
* [x] Containerização com Docker
* [ ] Deploy na AWS EC2
* [ ] Pipeline CI/CD
* [ ] Reverse Proxy e HTTPS
* [ ] Monitoramento com Prometheus
* [ ] Dashboards com Grafana
