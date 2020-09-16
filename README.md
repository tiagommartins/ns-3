# NS-3 Projeto de Aula

## Pré-requisitos
Este tutorial foi executado em um Sistema Operacional Ubuntu, mas é compatível com windows através do (Cygwin)[https://www.cygwin.com/]

## Instalação do NS-3

Baixar a versão 3.31 do NS-3:
```
wget https://www.nsnam.org/releases/ns-allinone-3.31.tar.bz2  
```

Descompactar os fontes na pasta corrente:
```
tar -xf ns-allinone-3.31.tar.bz2  
```

Acessar a pasta descompactada:
```
cd ns-allinone-3.31/  
```

Construir o projeto com os exemplos e testes habilitados:
```
./build.py --enable-examples --enable-tests  
```

Acessar a pasta do sistema compilado:
```
cd ns-3.31/  
```

Configurar os testes e exemplos do NS-3:
```
./waf -d optimized --enable-examples --enable-tests configure  
```

Configurar debug:
```
./waf -d debug --enable-examples --enable-tests configure  
```

Finalizar a configuração do NS-3:
```
./waf  
```

Executar os testes do core do NS-3:
```
./test.py -c core  
```

Executar o sistema com o projeto de teste "Hello Simulator":
```
./waf --run hello-simulator
``` 

## Construindo o Projeto

Setar a variável de ambiente **$NS3_HOME** com o path onde está instalado o ns-3:
```
NS3_HOME="/path/to/ns3/home"
```

Construir o projeto através do código:
```
./build.sh
```

## Rodando a Simulação

Setar a variável de ambiente **$NS3_HOME** com o path onde está instalado o ns-3.
```
NS3_HOME="/path/to/ns3/home"
```

Rodar o projeto através do código:
```
./run.sh first
```
Onde "first" é o nome do projeto compilado.
