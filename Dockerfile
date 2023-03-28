FROM ubuntu


# Adicionando os pacotes e dependências necessárias para a sua simulação
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install -y python3.9 


# Copia o scripy do diretório local para dentro do container
RUN echo "Copiando o script"
COPY Projeto_1_Casio_Krebs.py /


# Copia os circuitos da pasta test/ do host para o docker
RUN echo "Copiando os circuitos"
RUN mkdir test
COPY test/ test/


# Executa o script do simulador desenvolvido
RUN echo "Executando o simulador"
RUN python3 Projeto_1_Casio_Krebs.py
