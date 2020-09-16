# NS-3 Projeto de Aula

## Pré-requisitos
Este tutorial foi executado em um Sistema Operacional Ubuntu 18.04.5 LTS, mas é compatível com windows através do [Cygwin](https://www.cygwin.com/)

### Pacotes necessários:
Para instalação e uso do NS-3 serão necessários a instalação dos seguintes pacotes (execução somente no Ubuntu):
```
apt-get install g++ python3 python3-dev pkg-config sqlite3
```

Para utilização do visualizador deve instalar os seguintes componentes (Opcional):
```
apt-get install gir1.2-goocanvas-2.0 python-gi python-gi-cairo python-pygraphviz python3-gi python3-gi-cairo python3-pygraphviz gir1.2-gtk-3.0 ipython ipython3
```

## Instalação do NS-3

Criar a pasta onde será utilizado para a instalação:
```
cd $HOME
mkdir unilasalle
cd unilasalle
mkdir workspace
```

Acessar a pasta padrão para iniciar a instalção do ns-3:
```
cd workspace
```

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

Para habilitar Python como interpetrador do NS-3, favor configurar através do comando abaixo:
```
/usr/bin/python3.6 ./waf configure
```
## Projeto em C++
### Construindo o Projeto

Caso você efetuou a instalação em outro diretório, é necessário setar a variável de ambiente **$NS3_HOME** com o path onde está instalado o ns-3:
```
NS3_HOME="/path/to/ns3/home"
```

Construir o projeto através do código:
```
./build.sh
```

### Rodando a Simulação

Caso você efetuou a instalação em outro diretório, é necessário setar a variável de ambiente **$NS3_HOME** com o path onde está instalado o ns-3.
```
NS3_HOME="/path/to/ns3/home"
```

Rodar o projeto através do código:
```
./run.sh first
```
Onde "first" é o nome do projeto compilado.

## Projeto em Python
### Rodando a Simulação
Caso você efetuou a instalação em outro diretório, é necessário setar a variável de ambiente **$NS3_HOME** com o path onde está instalado o ns-3.
```
NS3_HOME="/path/to/ns3/home"
```

Rodar o projeto através do código:
```
./pyrun.sh first.py
```
Onde "first" é o nome do projeto compilado.