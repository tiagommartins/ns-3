# NS-3 Projeto de Aula


## Instalação do NS-3

```
wget https://www.nsnam.org/releases/ns-allinone-3.31.tar.bz2  
tar -xf ns-allinone-3.31.tar.bz2  
cd ns-allinone-3.31/  
./build.py --enable-examples --enable-tests  
cd ns-3.31/  
./waf -d optimized --enable-examples --enable-tests configure  
./waf -d debug --enable-examples --enable-tests configure  
./waf  
./test.py -c core  
./waf --run hello-simulator
``` 

## Construindo o Projeto
### Pré-requisito
Setar a variável global **$NS3_HOME** com o path onde está instalado o ns-3.
### Como "Buildar"

```
./build.sh  
```

## Rodando a Simulação
### Pré-requisito
Setar a variável global **$NS3_HOME** com o path onde está instalado o ns-3.
### Como "Rodar"
```
./run.sh first
```

Onde "first" é o nome do projeto compilado.
