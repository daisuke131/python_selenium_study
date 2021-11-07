from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

MYNAVI_URL = "https://tenshoku.mynavi.jp/list/"


def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(MYNAVI_URL)
    sleep(3)
    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        sleep(1)
        driver.execute_script('document.querySelector(".karte-close").click()')
    except Exception:
        pass


if __name__ == "__main__":
    main()
