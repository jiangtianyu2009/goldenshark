FROM python:3

WORKDIR /home/goldenshark

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "127.0.0.1:4000", "jav:app", "--reload", "--daemon"]