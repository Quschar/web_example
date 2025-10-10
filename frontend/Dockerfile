# 使用 Node.js 官方镜像作为基础环境
FROM node:22-alpine

# 设置环境变量
ENV CONTAINER_PATH /frontend
ARG https_proxy
ARG http_proxy

# 设置工作目录
WORKDIR CONTAINER_PATH /frontend

# 复制 package.json 和 package-lock.json
COPY package*.json ./

# 安装依赖（开发依赖和生产依赖均安装）
RUN npm install --legacy-peer-deps

# 复制项目文件
COPY . .

# 暴露开发服务器端口
EXPOSE 5173

# 启动开发命令（支持热重载）
# CMD ["npm", "run", "build"]
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]