# 建置說明

## 軟體架構
Python: 3.10
FastAPI
Mariadb: 10.6
Redis

## 建立資料庫資料存放目錄
```bash
mkdir ./data
```
## 建立Server API 程式目錄
```bash
mkdir ./code
```

## 掛載Server程式
```bash
sudo mount --bind {code_path} ./code
```

## 執行Docker Compose
```bash
sudo docker-compose up
```