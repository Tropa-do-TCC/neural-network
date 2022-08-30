FROM continuumio/miniconda2 AS base
WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml
RUN conda activate network
COPY . .

ENTRYPOINT ["/bin/bash"]
