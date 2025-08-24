from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 

def test_google_search():
    options = Options() 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    try:
        driver.get("https://www.google.com")
        time.sleep(4)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("qualidade e teste de software")
        search_box.send_keys(Keys.RETURN)
        time.sleep(20)

        assert "qualidade e teste de software" in driver.title.lower()
        print("teste passou!")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        driver.quit()
        print("Navegador fechado.")

# Executar
test_google_search()
