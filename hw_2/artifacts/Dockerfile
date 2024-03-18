FROM python:3.11.8-slim as base

LABEL maintainer="Denis <densiderkach2003@gmail.com>"

RUN apt-get update
RUN apt-get install -y --no-install-recommends texlive

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir latex-table-and-image==0.0.2

VOLUME /app

RUN python PDF_generator_with_package.py

RUN pdflatex example_table_and_image.tex

