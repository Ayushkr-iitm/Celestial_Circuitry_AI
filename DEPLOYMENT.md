# 🚀 Deployment Guide - Celestial Circuitry AI

This guide covers various deployment options for the Celestial Circuitry AI platform.

## 📋 Prerequisites

- Python 3.8 or higher
- 4GB+ RAM
- 2GB+ storage space
- Modern web browser

## 🏠 Local Development

### Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/celestial-circuitry-ai.git
cd celestial-circuitry-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### Development Server
```bash
# Run with custom port
streamlit run app.py --server.port 8502

# Run with custom address
streamlit run app.py --server.address 0.0.0.0
```

## ☁️ Cloud Deployment

### Heroku Deployment

1. **Create Heroku App**
   ```bash
   heroku create celestial-circuitry-ai
   ```

2. **Create Procfile**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

### Railway Deployment

1. **Connect Repository**
   - Connect your GitHub repository to Railway
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `streamlit run app.py --server.port=$PORT`

2. **Environment Variables**
   ```
   PORT=8501
   ```

### Render Deployment

1. **Create Web Service**
   - Connect GitHub repository
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

2. **Environment Variables**
   ```
   PORT=8501
   ```

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run
```bash
# Build image
docker build -t celestial-circuitry-ai .

# Run container
docker run -p 8501:8501 celestial-circuitry-ai
```

### Docker Compose
```yaml
version: '3.8'
services:
  celestial-circuitry-ai:
    build: .
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    volumes:
      - ./data:/app/data
      - ./models:/app/models
```

## 🌐 Production Deployment

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Systemd Service

Create `/etc/systemd/system/celestial-circuitry-ai.service`:

```ini
[Unit]
Description=Celestial Circuitry AI
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/celestial-circuitry-ai
Environment=PATH=/path/to/celestial-circuitry-ai/venv/bin
ExecStart=/path/to/celestial-circuitry-ai/venv/bin/streamlit run app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable celestial-circuitry-ai
sudo systemctl start celestial-circuitry-ai
```

## 🔧 Environment Configuration

### Production Environment Variables

```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Application Configuration
CELESTIAL_DEBUG=false
CELESTIAL_LOG_LEVEL=INFO
CELESTIAL_MAX_UPLOAD_SIZE=100MB
```

### Development Environment Variables

```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
STREAMLIT_SERVER_HEADLESS=false
STREAMLIT_BROWSER_GATHER_USAGE_STATS=true

# Application Configuration
CELESTIAL_DEBUG=true
CELESTIAL_LOG_LEVEL=DEBUG
CELESTIAL_MAX_UPLOAD_SIZE=50MB
```

## 📊 Monitoring and Logging

### Application Monitoring

```python
# Add to app.py
import logging
import os

# Configure logging
logging.basicConfig(
    level=os.getenv('CELESTIAL_LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('celestial.log'),
        logging.StreamHandler()
    ]
)
```

### Health Check Endpoint

```python
# Add to app.py
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': time.time()}
```

## 🔒 Security Considerations

### Production Security

1. **HTTPS Configuration**
   - Use SSL certificates
   - Redirect HTTP to HTTPS
   - Set secure headers

2. **Access Control**
   - Implement authentication
   - Rate limiting
   - Input validation

3. **Data Protection**
   - Encrypt sensitive data
   - Secure file uploads
   - Regular backups

### Security Headers

```python
# Add to app.py
import streamlit as st

# Security headers
st.set_page_config(
    page_title="Celestial Circuitry AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add security middleware
@st.cache_data
def secure_data_processing(data):
    # Implement data sanitization
    return sanitized_data
```

## 📈 Performance Optimization

### Caching Strategy

```python
# Model caching
@st.cache_resource
def load_models():
    classifier = ExoplanetClassifier()
    classifier.load_models()
    return classifier

# Data caching
@st.cache_data
def process_light_curve(file_path):
    processor = LightCurveProcessor()
    return processor.process_light_curve(file_path)
```

### Resource Optimization

1. **Memory Management**
   - Use generators for large datasets
   - Implement data chunking
   - Monitor memory usage

2. **CPU Optimization**
   - Parallel processing
   - Async operations
   - Load balancing

## 🧪 Testing Deployment

### Pre-deployment Testing

```bash
# Run tests
python -m pytest tests/

# Check code quality
flake8 .
black --check .

# Test deployment locally
docker build -t test-celestial .
docker run -p 8501:8501 test-celestial
```

### Production Testing

```bash
# Health check
curl http://localhost:8501/health

# Load testing
ab -n 1000 -c 10 http://localhost:8501/

# Performance monitoring
htop
iostat
```

## 🔄 CI/CD Pipeline

### GitHub Actions

```yaml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        run: |
          # Your deployment commands
```

### Automated Deployment

1. **Build Process**
   - Run tests
   - Build Docker image
   - Push to registry

2. **Deployment Process**
   - Update production environment
   - Run health checks
   - Rollback if needed

## 📝 Troubleshooting

### Common Issues

1. **Port Conflicts**
   ```bash
   # Check port usage
   netstat -tulpn | grep :8501
   
   # Kill process
   sudo kill -9 <PID>
   ```

2. **Memory Issues**
   ```bash
   # Monitor memory
   free -h
   
   # Increase swap
   sudo swapon -s
   ```

3. **Permission Issues**
   ```bash
   # Fix permissions
   sudo chown -R www-data:www-data /path/to/app
   sudo chmod -R 755 /path/to/app
   ```

### Debug Mode

```bash
# Enable debug logging
export CELESTIAL_DEBUG=true
export CELESTIAL_LOG_LEVEL=DEBUG

# Run with debug
streamlit run app.py --logger.level=debug
```

## 📞 Support

For deployment issues:
- GitHub Issues: [Create an issue](https://github.com/yourusername/celestial-circuitry-ai/issues)
- Documentation: [Read the docs](https://github.com/yourusername/celestial-circuitry-ai#readme)
- Email: your.email@example.com

---

**Happy Deploying!** 🚀✨
