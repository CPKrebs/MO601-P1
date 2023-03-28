# MO601-P1

Doutorando: Casio Pacheco Krebs
RA: 264953

# Configuração do Docker


Construa a imagem Docker a partir do Dockerfile. Este passo usa o comando ```docker build``` para construir a imagem:

```
docker build -t casio_p1 .
```


Modificar o nome do docker, com a flag ```--name```, a partir do comando ```run```: 

```
docker run -d --name casio_p1_exec casio_p1
```



# Coleta de resultados

Primeiramente é necessario deletar a pasta ```test```, a fim de evitar conflito durante a copia dos dados, a partir do comando ```rm```: 

```
rm -R test/
```



Por fim, para realizar as copias dos dados de saida, é utilizado o comando ```docker cp```.

```
docker cp casio_p1_exec:/test test/
```

