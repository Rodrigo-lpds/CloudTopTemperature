# Criação de projeções de Temperatura em Topo de Nuvem

## Descrição
O projeto foi criado com o objetivo de utilizar dados geoespaciais (de formato **NetCDF**) dados pelo satélite **GOES-16** para confecção de projeções. A partir dos **16** canais do satélite podemos extrair diferentes tipos de dados, sendo cada canal diferente entre si por estarem em frequencias diferentes.
Neste projeto, o canal **13** foi escolhido, pois mostrou-se ser o ideal para criação de projeções que determinem a temperatura em topo de nuvem.

## Instalação
Para a execução dos scripts que serão mencionados posteriormente, será necessária a instalação de certos programas.

#### Anaconda
Distribuição que nos dará as ferramentas necessárias para uma execução mais prática e direta.
O download da distribuição pode ser encontrado no [site oficial](https://www.anaconda.com), e até o momento por este [link](https://www.anaconda.com/distribution/#download-section).

**Importante: É recomendado que após a instalação completa do Anaconda, seja criado um Ambiente ou, Environment, _específico_ para o projeto.**
#### Spyder
IDE que utilizaremos para plotar as projeções e para debugar os scripts.
As instruções para download podem ser encontradas neste [link](https://docs.spyder-ide.org/installation.html).
