FROM python:3.9-slim

WORKDIR /opt/program

# Copy requirements & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY autocorrect.py serve.py big.txt ./

# Expose port
ENV PORT=8080
ENV PYTHONUNBUFFERED=TRUE

CMD ["gunicorn", "-b", "0.0.0.0:8080", "serve:app"]
