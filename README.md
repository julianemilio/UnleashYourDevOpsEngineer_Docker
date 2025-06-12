# 🐳 Introduction to Docker

## 🧠 What is Docker?

Docker is a platform that lets you package an application and all its dependencies into a container, ensuring it runs the same in any environment.

## 📦 Basic Docker Commands

```bash
## 1. Check installation
docker --version

## 2. Run a test container
docker run hello-world

## 3. Run an application (example: Nginx web server)
docker run -d -p 8889:80 prakhar1989/static-site

## 4. List running containers
docker ps

## 5. List all containers (including stopped ones)
docker ps -a

## 6. Stop a container
docker stop <container_id>

## 7. Remove a container
docker rm <container_id>

## 8. Remove an image
docker rmi <image_id>

## 9. List downloaded images
docker images

## 10. Build image
docker build -t my-app .

## 11. Run container
docker run -p 3000:3000 my-app

```

# 📦 Push a Docker Image to Azure Container Registry (ACR)

## 🌱 1. Create a Resource Group (if needed)

```bash
az group create --name rgUnleash --location eastus
```

> Replace `rgUnleash` with your preferred name and `eastus` with your preferred region.

---

## 🏗️ 2. Create an Azure Container Registry (ACR)

```bash
az acr create --resource-group rgUnleash --name acrunleash --sku Basic --admin-enabled true
```

> Replace `acrunleash` with a unique name (it will become `acrunleash.azurecr.io`).  
> The `--sku Basic` is the cheapest tier and sufficient for most use cases.

---

## 🔐 3. Log in to Azure

```bash
az login
```

---

## 🔑 4. Log in to your ACR

```bash
az acr login --name acrunleash
```

---

## 🧱 5. Build your Docker image locally

```bash
docker build -t myimage:v1 .
```

> This builds a Docker image from your local Dockerfile and tags it as `myimage:v1`.

---

## 🏷️ 6. Tag the image for ACR

```bash
docker tag myimage:v1 acrunleash.azurecr.io/myimage:v1
```

---

## ⬆️ 7. Push the image to ACR

```bash
docker push acrunleash.azurecr.io/myimage:v1
```

---

## 🔍 8. Verify the image in ACR

List available repositories:

```bash
az acr repository list --name acrunleash --output table
```

List image tags:

```bash
az acr repository show-tags --name acrunleash --repository myimage --output table
```

---
