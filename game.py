# game.py
# read readme.md on my github 
from selenium import webdriver


driver_path = "chemin/vers/le/driver/chromedriver"


driver = webdriver.Chrome(driver_path)


url = "https://classic.minecraft.net/?join=vqcrKCVOytfy93qtnec"

driver.get(url)


input("Appuyez sur Entrée pour quitter...")


driver.quit()
