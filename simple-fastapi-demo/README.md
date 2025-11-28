# Build a simple FastApi service demo

## Build Image
```sbashh
docker build -t my-fastapi-test
```

## Run 

```bash
docker run -it --name fastapi-test -p 8888:8000 my-fastapi-test
# docker run -d --name fastapi-test -p 8888:8000 my-fastapi-test
```

## Testing
```bash
curl --location 'http://localhost:8888/health'
curl --location 'http://localhost:8888'
```