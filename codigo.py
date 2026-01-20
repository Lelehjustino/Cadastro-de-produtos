import pyautogui
import time


# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho 

# configuração para esperar um segundo para executar o próximo comando
pyautogui.PAUSE = 1 
# variável com o link da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa de 3 s para o site carregar 
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=753, y=492)
pyautogui.write("lehjustinowehbe@gmail.com")
pyautogui.press("tab") # passar para o próximo campo
pyautogui.write("123456")
pyautogui.press("tab") # passar para o botão 
pyautogui.press("enter")

#pausa para esperar o site entrar
time.sleep(3)
# pyautogui.click(x=712, y=463)

# Passo 3: abrir base de dados(importar arquivo)
import pandas
print(pandas.__version__)
tabela = pandas.read_csv("produtos.csv") 
for linha in tabela.index: 
    # Passo 4: Cadastrar 1 produto
    # campo código
    pyautogui.click(x=905, y=367) 

    # pyautogui.press("tab")
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # campo marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # campo tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # campo categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # campo preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # campo custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # campo observação 
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": 
        pyautogui.write(obs)
    pyautogui.press("tab")

    # ir para botão enviar
    pyautogui.press("enter")

    # voltar para o inicio 
    pyautogui.scroll(5000)
    time.sleep(5)
# Passo 5: Repetir o cadastro até terminar a base