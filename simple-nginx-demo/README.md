# Simple Nginx Service Demo

## Method 1: docker run command 
```
docker run -p 8080:80 nginx
docker run --name simple-nginx-demo -p 8080:80 nginx

```

--------
## Method 2: Dockerfile

### Build Image
```bash
docker build -t simple-nginx-demo
```

### Run
```bash
docker run -it --name simple-nginx-demo -p 8080:80 simple-nginx-demo
```

--------

## Method 3: Compose
```bash
docker compose up
```

--------


# Testing
```bash
curl -l 'http://127.0.0.1:8080'
```