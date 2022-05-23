from botconfig import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

def golink(link,getRef,wallet1,wallet2):
    time.sleep(2)
    pyautogui.click(clicarNoCantoInferior)
    time.sleep(2)
    pyautogui.click(clicarNaIconeNavegador)
    time.sleep(1)
    pyautogui.click(cliqueNoMeioDaTela)
    pyautogui.hotkey('ctrl','shift','n')
    time.sleep(2)
    pyautogui.click(cliqueNaUrl)
    time.sleep(1)
    pyautogui.typewrite(link)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    check = "Exchange "
    verific = ""
    time.sleep(5)
    while check != verific:
        pyautogui.doubleClick(cliquePalavraExchange)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        verific = pyperclip.paste()
        time.sleep(delayExchange)
    pyautogui.click(cliqueInputTextWallet)
    time.sleep(1)
    pyautogui.typewrite(wallet1)
    time.sleep(1)
    pyautogui.click(cliquenoBotao)
    time.sleep(2)
    check = "Dashboard"
    verific = ""
    tentativas = 0
    while check != verific:
        pyautogui.doubleClick(cliquePalavraDashboard)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        verific = pyperclip.paste()
        time.sleep(delayDashboard)
        tentativas = tentativas+1
        if tentativas == 30:
            pyautogui.click(cliqueInputTextWallet)
            time.sleep(1)
            pyautogui.typewrite(wallet1)
            time.sleep(1)
            pyautogui.click(cliquenoBotao)
        if tentativas == 60:
            pyautogui.click(cliqueInputTextWallet)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.typewrite(walletRef[i])
            time.sleep(1)
            pyautogui.click(cliquenoBotao)
        if tentativas == 90:
            pyautogui.click(cliqueInputTextWallet)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.typewrite(walletRef[i])
            time.sleep(1)
            pyautogui.click(cliquenoBotao)
    time.sleep(1)        
    if getRef:
        pyautogui.moveTo(cliqueNoMeioDaTela)
        pyautogui.scroll(-400)
        time.sleep(1)
        pyautogui.click(cliqueIconeURL)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt','f4')
        time.sleep(5)
        golink(pyperclip.paste(),False,wallet2,0)
    else:
        pyautogui.hotkey('alt','f4')
        time.sleep(5)

if questionario:
    walletRef = input('Digite as Carteira com a seguinte ordem "LINK,Carteira" e use "|" para caso tenha mais de uma carteira ou digite "Carregar Arquivo"')
    if walletRef == "Carregar Arquivo":
        walletRef = input('O Carregamento de arquivo deve está no formato de "LINK,Carteira" e use quebra de linha como separador de carteiras.\n Insira o caminho do arquivo que queria ser lido:')
        walletRef = open(walletRef).read()
        walletRef = walletRef.split("\n")
    else:
        if walletRef[len(walletRef)-1] == "|":
            walletRef = walletRef[0:(en(walletRef)-1)]
        walletRef = walletRef.split("|")
    
    limiteType = input('Qual o limitador de carteira será usado?\nValor em "USDT" ou "Seguidores"? ')
    if limiteType == "USDT":
        limiteType = 1
    else:
        limiteType = 2

    limiteValue = int(input("Qual o Valor?"))
else:
    if walletLoad:
        walletRef = open(walletRef).read()
        walletRef = walletRef.split("\n")
    else:
        if walletRef[len(walletRef)-1] == "|":
            walletRef = walletRef[0:(en(walletRef)-1)]
        walletRef = walletRef.split("|")
scan = "https://tronscan.org/#/blockchain/transactions"
url = "https://tronseed.com/"

for i in range(0,len(walletRef)):
    forRepeat = 0
    while forRepeat == 0:
        time.sleep(2)
        pyautogui.click(clicarNoCantoInferior)
        time.sleep(2)
        pyautogui.click(clicarNaIconeNavegador)
        time.sleep(1)
        pyautogui.click(cliqueNoMeioDaTela)
        pyautogui.hotkey('ctrl','shift','n')
        time.sleep(2)
        pyautogui.click(cliqueNaUrl)
        time.sleep(1)
        pyautogui.typewrite(url)
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(2)
        check = "Exchange "
        verific = ""
        time.sleep(5)
        while check != verific:
            pyautogui.doubleClick(cliquePalavraExchange)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            verific = pyperclip.paste()
            time.sleep(delayExchange)
        pyautogui.click(cliqueInputTextWallet)
        time.sleep(1)
        pyautogui.typewrite(walletRef[i])
        time.sleep(1)
        pyautogui.click(cliquenoBotao)
        time.sleep(2)
        check = "Dashboard"
        verific = ""
        tentativas = 0
        while check != verific:
            pyautogui.doubleClick(cliquePalavraDashboard)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            verific = pyperclip.paste()
            time.sleep(delayDashboard)
            tentativas = tentativas+1
            if tentativas == 30:
                pyautogui.click(cliqueInputTextWallet)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(1)
                pyautogui.typewrite(walletRef[i])
                time.sleep(1)
                pyautogui.click(cliquenoBotao)
            if tentativas == 60:
                pyautogui.click(cliqueInputTextWallet)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(1)
                pyautogui.typewrite(walletRef[i])
                time.sleep(1)
                pyautogui.click(cliquenoBotao)
            if tentativas == 90:
                pyautogui.click(cliqueInputTextWallet)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(1)
                pyautogui.typewrite(walletRef[i])
                time.sleep(1)
                pyautogui.click(cliquenoBotao)
        if limiteType==1:
            pyautogui.doubleClick(cliquePosicaoUSDT)
            pyautogui.hotkey('ctrl', 'c')
            if float(pyperclip.paste()) >= limiteValue:
                forRepeat = 1
        else:
            pyautogui.doubleClick(cliquePosicaoInvite)
            pyautogui.hotkey('ctrl', 'c')
            if float(pyperclip.paste()) >= limiteValue:
                forRepeat = 1
        time.sleep(5)

        if forRepeat == 0: 
            pyautogui.scroll(-400)
            time.sleep(1)
            pyautogui.click(cliqueIconeURL)
            pyautogui.hotkey('ctrl', 'c')
            priorytuWallet = pyperclip.paste()

        pyautogui.hotkey('alt','f4')
        
        if forRepeat == 0: 
            browser = webdriver.Chrome()
            arraywallet = [[],[]]
            for k in range(0,2):
                browser.get(scan)
                time.sleep(6)
                for j in range(1,21):
                    xpath1 = "/html/body/div[1]/div[2]/main/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr["
                    xpath2 = "]/td[4]/span/span/div/div/span/div/a/div/div"
                    wallet = browser.find_elements_by_xpath(xpath1 + str(j) + xpath2 + "[1]")[0].text + browser.find_elements_by_xpath(xpath1 + str(j) + xpath2 + "[2]")[0].text
                    arraywallet[k].append(wallet)
            browser.close()
            time.sleep(2)
            for k in range(0,20):
                golink(priorytuWallet,True,arraywallet[0][k],arraywallet[1][k])


