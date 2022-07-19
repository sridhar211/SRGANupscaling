FROM python:3.8-buster

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

COPY SRGANupscaling /SRGANupscaling
COPY app.py /app.py
COPY setup.py /setup.py
COPY scripts /scripts
COPY static /static
COPY style.css /style.css
COPY app.yaml /app.yaml
COPY srgan_model /srgan_model

RUN pip install .

CMD streamlit run app.py
