FROM python:3.11-slim

WORKDIR /workspace

COPY code/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "run.sh"]
