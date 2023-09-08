from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import openpyxl

class Scrapy:
    def __init__(self):
        self.site_link = 'https://www.magazineluiza.com.br/'
        self.site_map = {
            "buttons":{
                "entrada":{
                    "xpath": "/html/body/div[4]/div/main/section[1]/div[2]/header/div/div[3]/nav/ul/li[3]/div[1]/a"
                }
            },
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def main(self):
        self.abre_o_site()
        self.chega()
        sleep(10)
        self.raspagem_magalu_cell()
        sleep(100000)

    def abre_o_site(self):
        self.driver.get(self.site_link)
        sleep(10)

    def chega(self):
        self.driver.find_element(By.XPATH, self.site_map['buttons']['entrada']['xpath']).click()
        sleep(5)

    def raspagem_magalu_cell(self):
        for contador in range(1, 50):  # Comece com contador em 1
            self.site_dados = {
                "scrap": {
                    "nome": f"/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[{contador}]/a/div[3]/h2",
                    "preco": f"/html/body/div[1]/div/main/section[4]/div[3]/div/ul/li[{contador}]/a/div[3]/div[2]/div/div/p"
                }
            }
 
            elemento_nome = self.driver.find_element(By.XPATH, self.site_dados['scrap']['nome']).text
            elemento_preco = self.driver.find_element(By.XPATH, self.site_dados['scrap']['preco']).text
            print(elemento_nome)
            print(elemento_preco)
            print(contador)






scrap = Scrapy()
scrap.main()