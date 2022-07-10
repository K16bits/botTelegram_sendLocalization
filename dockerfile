FROM python:3
COPY . /app
RUN pip install python-telegram-bot && pip install python-dotenv
WORKDIR /app
CMD ["python3","bot.py"]