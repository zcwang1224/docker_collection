# Docker Network Demo

## docker-compose.yaml

### Structure
bridge_pc_1 ---> bridge_pc_2 ok

bridge_pc_2 ---> bridge_pc_1 ok

host_pc_1 ---> bridge_pc_1 X

host_pc_1 ---> bridge_pc_2 X

bridge_pc_1 ---> host_pc_1 X

bridge_pc_2 ---> host_pc_1 X

### RUN
```
docker compose up
```

--------

## docker-compose-multi-network.yaml

一台主機同時連接兩個network

### Structure
backend ---> backend ok

backend ---> web X

web ---> backend X

web ---> web OK


### RUN
```bash
docker compose -f docker-compose-multi-networkd.yaml up
```

## docker-compose-ipam.yaml

給容器固定IP、設定subnet

ipam (IP Address Management)

### 

