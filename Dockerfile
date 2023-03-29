# Must use a Cuda version 11+
FROM nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git && apt-get install -y wget && apt-get install -y curl

RUN curl -O https://raw.githubusercontent.com/YoshitakaMo/localcolabfold/main/install_colabbatch_linux.sh
RUN bash install_colabbatch_linux.sh
ENV PATH="/localcolabfold/colabfold-conda/bin:${PATH}"

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# We add the banana boilerplate here
ADD server.py .

# Add your custom app code, init() and inference()
ADD app.py .

EXPOSE 8000

CMD python3 -u server.py
