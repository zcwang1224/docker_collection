FROM nginx:1.27-alpine

# 自訂的 nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

#COPY conf.d/*.conf /etc/nginx/conf.d/

COPY html/ /usr/share/nginx/html/

# daemon off => 強制不放在背景跑nginx
CMD ["nginx", "-g", "daemon off;"]