FROM python:3
USER root

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
#RUN apt-get -y install libhdf5-dev

EXPOSE 8501
EXPOSE 8000

#↑しなくてもいい？

RUN python -m pip install pydantic fastapi uvicorn sqlalchemy mysqlclient streamlit requests
#RUN pip3 install --upgrade --ignore-installed https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl

ENTRYPOINT [ "uvicorn","memoback.main:app","--host","0.0.0.0","--reload" ]
#0.0.0.0とすることで外部からもアクセスできるようになるらしい
#localhostとすることでlocalhostになるらしい
#ENTRYPOINT [ "streamlit","run","main.py" ]