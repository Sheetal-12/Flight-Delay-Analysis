# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only files tracked in GitHub (excluding anything in .dockerignore)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

