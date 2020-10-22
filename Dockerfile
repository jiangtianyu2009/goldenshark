FROM python:3

WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4000

ENTRYPOINT ["gunicorn", "--config", "/src/gunicorn.conf", "jav:app"]