FROM python:3.9-slim

EXPOSE 8501

WORKDIR /src
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install streamlit
RUN pip install -r requirements.txt

COPY ./app /src/app
COPY config.toml /root/.streamlit
COPY credentials.toml /root/.streamlit

ENTRYPOINT [ "streamlit", "run", "--browser.gatherUsageStats", "false", "app/__main__.py"]