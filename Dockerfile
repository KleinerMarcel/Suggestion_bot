FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install aiogram asyncio 
#If you add dependencies, delete "aiogram asyncio" and insert --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "bot_hp.py"]
