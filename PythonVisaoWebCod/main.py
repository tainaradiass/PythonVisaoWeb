from selenium import webdriver
import time
import subprocess

driver = webdriver.Chrome()

try:
   driver.get("https://www.tudogostoso.com.br/")
   time.sleep(5)
   conteudo_visivel = driver.find_element("tag name", "body").text
   with open("relatorio.txt", "w", encoding="UTF-8") as arquivo_relatorio:
       arquivo_relatorio.write(conteudo_visivel)
       subprocess.Popen(["notepad.exe", "relatorio.txt"])
except Exception as e:
   print(f"Erro: {e}")
   driver.quit()

finally:
    if 'driver' in locals() or 'driver' in globals():
        driver.quit()