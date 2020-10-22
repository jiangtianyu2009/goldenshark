FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["gunicorn", "-w", "4", "-b", "127.0.0.1:4000", "jav:app", "--reload"]