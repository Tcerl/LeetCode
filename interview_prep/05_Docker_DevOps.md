# 🐳 DOCKER & DEVOPS - ÔN THI PHỎNG VẤN

---

## 1. DOCKER FUNDAMENTALS

### 1.1 Image vs Container vs Volume vs Network
```bash
# Image: Blueprint read-only (như class trong Python)
docker images                          # list images
docker pull python:3.11-slim          # tải image
docker build -t myapp:v1.0 .          # build từ Dockerfile
docker rmi myapp:v1.0                 # xóa image
docker image prune                    # xóa dangling images

# Container: Running instance từ image (như object)
docker run -d -p 8080:5000 myapp:v1.0  # chạy nền
docker ps                               # list running containers
docker ps -a                            # list tất cả (kể cả stopped)
docker start/stop/restart container_id
docker rm container_id                  # xóa container
docker exec -it container_id bash      # interactive shell

# Volume: Persistent storage
docker volume create mydata
docker run -v mydata:/app/data myapp   # mount named volume
docker run -v $(pwd):/app myapp        # bind mount (dev)

# Network
docker network create mynet
docker run --network mynet myapp
```

---

### 1.2 Dockerfile Best Practices (QUAN TRỌNG)
```dockerfile
# ❌ BAD: Image lớn, cache miss thường xuyên
FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# ✅ GOOD: Optimized Dockerfile
# Stage 1: Dependencies (cached khi requirements.txt không thay đổi)
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies (thay đổi ít nhất)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies (chỉ re-run khi requirements.txt thay đổi)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code (thay đổi thường xuyên nhất → copy cuối)
COPY . .

# Non-root user (security)
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:create_app()"]
```

> **🎯 Layer caching rules:**
> 1. Layer chỉ invalidate khi nó hoặc layer trước thay đổi
> 2. Instructions ít thay đổi nhất → đặt **trên**
> 3. `COPY source code` luôn đặt **sau** `pip install`

---

### 1.3 Multi-stage Build
```dockerfile
# Build stage: compile and test (không cần trong production)
FROM node:18 AS frontend-builder
WORKDIR /app
COPY frontend/package*.json ./frontend/
RUN cd frontend && npm ci
COPY frontend/ ./frontend/
RUN cd frontend && npm run build

# Python setup
FROM python:3.11-slim AS python-deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final production image
FROM python:3.11-slim AS production
WORKDIR /app

# Copy only what we need from previous stages
COPY --from=python-deps /usr/local/lib/python3.11/site-packages/ \
    /usr/local/lib/python3.11/site-packages/
COPY --from=frontend-builder /app/frontend/dist /app/static
COPY backend/ /app/backend/
COPY app.py /app/

RUN adduser --disabled-password appuser
USER appuser
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

> **🎯 Multi-stage benefits:**
> - Production image không có build tools (gcc, npm)
> - Giảm attack surface (security)
> - Image nhỏ hơn 10x

---

## 2. DOCKER COMPOSE

### 2.1 Cơ bản cho Flask App
```yaml
# docker-compose.yml
version: '3.9'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production       # multi-stage target
    image: myapp:latest
    container_name: flask_app
    restart: unless-stopped
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    env_file:
      - .env.production        # sensitive vars từ file
    volumes:
      - ./logs:/app/logs
    depends_on:
      db:
        condition: service_healthy    # chờ DB healthy
      redis:
        condition: service_started
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:15-alpine
    container_name: postgres_db
    restart: unless-stopped
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: ${DB_PASSWORD}  # từ .env file
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mydb"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  redis:
    image: redis:7-alpine
    container_name: redis
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    networks:
      - backend

  celery_worker:
    build: .
    command: celery -A app.celery worker --loglevel=info --concurrency=4
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - app
      - redis
    networks:
      - backend

  nginx:
    image: nginx:alpine
    container_name: nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./certbot/conf:/etc/letsencrypt
    depends_on:
      - app
    networks:
      - backend

volumes:
  postgres_data:
  redis_data:

networks:
  backend:
    driver: bridge
```

---

### 2.2 Useful docker-compose commands
```bash
# Build và start tất cả
docker-compose up -d --build

# Xem logs
docker-compose logs -f app           # logs của service 'app'
docker-compose logs --tail=100       # 100 dòng cuối tất cả services

# Scale services
docker-compose up -d --scale celery_worker=3

# Exec vào container
docker-compose exec app bash

# Run một lần (migration)
docker-compose run --rm app flask db upgrade

# Stop và xóa
docker-compose down
docker-compose down -v              # kèm xóa volumes (NGUY HIỂM ở prod!)

# Restart specific service
docker-compose restart app

# Check health
docker-compose ps
```

---

## 3. LINUX COMMANDS CHO PHỎNG VẤN

### 3.1 File và Directory
```bash
# Tìm file
find /app -name "*.py" -mtime -7    # files.py thay đổi trong 7 ngày
find /app -size +100M                # files > 100MB

# Text processing (quan trọng)
grep -r "TODO" ./app                 # recursive search
grep -n "def create" ./app.py        # với line number
grep -i "error" app.log             # case insensitive
grep -v "DEBUG" app.log             # exclude DEBUG lines

# Xem file lớn
tail -f app.log                      # follow log real-time
tail -n 100 app.log                  # 100 dòng cuối
head -n 50 app.log                   # 50 dòng đầu

# AWK cho log processing
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10
# Top 10 IPs từ access log

# sed
sed -i 's/localhost/production.db.com/g' config.py
```

### 3.2 Process và System
```bash
# Process
ps aux | grep python                # tìm python processes
kill -9 <pid>                       # force kill
pgrep -f "gunicorn"                 # tìm PID theo pattern

# System resources
top                                  # interactive process viewer
htop                                 # enhanced top
df -h                                # disk usage
du -sh ./app                         # size của folder
free -h                              # memory usage

# Network
netstat -tlnp                        # listening ports
ss -tlnp                             # modern netstat
curl -I https://example.com          # check HTTP headers
nc -zv host 5432                     # test port connectivity
lsof -i :5000                        # process using port 5000
```

### 3.3 System Service (Systemd)
```bash
# Quản lý services
systemctl start myapp
systemctl stop myapp
systemctl restart myapp
systemctl status myapp
systemctl enable myapp               # auto-start on boot

# View logs
journalctl -u myapp -f              # follow service logs
journalctl -u myapp --since "1 hour ago"
```

---

## 4. NGINX CONFIGURATION (cơ bản cần biết)

```nginx
# /etc/nginx/sites-available/myapp
server {
    listen 80;
    server_name example.com;
    
    # Redirect HTTP → HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
    # Proxy to Flask/Gunicorn
    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeout
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # WebSocket support
    location /socket.io {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
    
    # Static files (phục vụ trực tiếp qua Nginx nhanh hơn)
    location /static {
        alias /app/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

---

## 5. GIT WORKFLOW

```bash
# Feature branch workflow
git checkout -b feature/user-authentication
git add -p                          # interactive staging theo hunks
git commit -m "feat(auth): add JWT authentication

- Implement login/logout endpoints
- Add JWT token generation with claims
- Add @jwt_required decorator for protected routes
- Write tests for auth flow

Closes #123"

git push origin feature/user-authentication
# → Create Pull Request → Code Review → Merge

# Useful commands
git log --oneline --graph --all     # visual branch history
git stash                           # tạm thời save changes
git stash pop                       # restore stashed changes
git rebase -i HEAD~3                # interactive rebase (squash commits)
git bisect start/bad/good           # binary search bug
```

### Conventional Commits
```
feat:     New feature
fix:      Bug fix
docs:     Documentation
style:    Formatting (no logic change)
refactor: Code restructure
test:     Add/fix tests
chore:    Build tools, dependencies
perf:     Performance improvements

Format: type(scope): description

# Ví dụ:
feat(auth): add JWT refresh token endpoint
fix(migration): resolve MariaDB driver compatibility
chore(docker): optimize Dockerfile layer cache
```

---

## 6. CI/CD PIPELINE (GitHub Actions)

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: test_db
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: pip install -r requirements.txt
        
      - name: Run tests
        run: pytest --cov=app tests/
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost/test_db

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Deploy via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /app
            git pull origin main
            docker-compose pull
            docker-compose up -d --build
            docker-compose exec app flask db upgrade
```

---

## ✅ CHECKLIST DOCKER & DEVOPS

- [ ] Giải thích sự khác biệt image/container/volume/network
- [ ] Tối ưu Dockerfile layer cache
- [ ] Multi-stage build và lợi ích
- [ ] docker-compose cho multi-service app  
- [ ] Linux commands: grep, awk, tail, netstat
- [ ] Nginx proxy config cho Flask
- [ ] Git conventional commits
- [ ] CI/CD pipeline cơ bản
