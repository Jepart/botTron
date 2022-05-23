#FUNCIONAMENTO
O bot ele le todas as carteiras informadas e em cada uma verifica o saldo, caso a definição seja menor do que definada nas configurações ela armazena a URL da carteira a funcionar.
No primeiro momento ela vai colhetar 20 carteiras aleatórias no site tron scan e mais 20 para que seja feita uma inscrição dupla.
Ao termino das carteira fará outra verificação de saldo e caso não tenha batido o valor definido fará o loop novamente.
Se em algum momento o bot não conseguir entrar na carteira ele fará mais 3 tentativas.

#CONFIGURAÇÃO
Existe dois arquivos na pasta **Carteiras.txt** e **botconfig.py**
No **botconfig.py** você irá configura todas as coordenadas e algumas configurações basicas.
A **Carteiras.txt** será usada caso no **botconfig.py** "*walletLoad*" esteja como verdadeiro, caso não esteja deverá definir uma texto com as carteiras.

#INSTALAÇÃO

Instale o Python no computador (https://www.python.org/downloads/release/python-3913/)
No CMD use o comando
>pip install selenium

No CMD use o comando
>py -m pip install pyautogui

Entre no site do Selenium e baixe o browsebot da versão do seu navegador (https://chromedriver.storage.googleapis.com/index.html)
O Arquivo baixado instale na pasta do Python

Baixe o https://x-mouse-button-control.br.uptodown.com/windows para pegar a posição exata na tela para o bot funcionar

#Execultando

Use o comando em um terminal
>py bugtron.py
