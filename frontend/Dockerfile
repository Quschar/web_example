# 使用 Node.js 官方镜像作为基础环境
FROM node:22-alpine

# 设置环境变量
ARG https_proxy
ARG http_proxy

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package*.json ./
RUN npm ci --only=production

# 复制项目文件
COPY . .

# 安装开发依赖（热重载工具）
RUN npm install --save-dev nodemon

# 暴露开发服务器端口
EXPOSE 5173

# 设置环境变量（区分环境）
ENV NODE_ENV=development

# 启动开发命令（支持热重载）
# CMD ["npm", "run", "build"]
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
# CMD [ "sh", "-c", "nodemon --exec 'npm run dev' --watch src --ext js,jsx" ]