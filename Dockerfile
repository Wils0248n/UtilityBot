FROM python:3.6-stretch
WORKDIR /app
ENV TOKEN=""
CMD ["cd", "/app"]
RUN pip install discord
CMD ["sh", "-c", "python3 utilitybot.py $TOKEN"]
