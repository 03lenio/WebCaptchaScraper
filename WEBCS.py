import time
from selenium import webdriver
import os
import shutil

global driver

grabbed = 0
captchaCount = 0


def grabCaptchas():
    # create scraped folder if not exist
    if not os.path.exists("scraped"):
        os.mkdir("scraped")
    time.sleep(2)
    global captchaCount
    captchaCount += 1
    driver.find_element_by_id("captchaImage").screenshot("scraped/captcha" + str(captchaCount) + ".png")
    print("Successfully grabbed captcha no." + str(captchaCount))
    global grabbed
    grabbed += 1
    driver.refresh()


def cls():
    os.system('cls' if os.name == 'nt' else 'cls()')  # clear for aesthetic reasons


def main():
    cls()
    # print title
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("██ ███ █ ▄▄█ ▄▄▀████ ▄▄▀█ ▄▄▀█▀▄▄▀█▄ ▄█▀▄▀█ ████ ▄▄▀███ ▄▄█▀▄▀█ ▄▄▀█ ▄▄▀█▀▄▄▀█ ▄▄█ ▄▄▀██")
    print("██ █ █ █ ▄▄█ ▄▄▀████ ████ ▀▀ █ ▀▀ ██ ██ █▀█ ▄▄ █ ▀▀ ███▄▄▀█ █▀█ ▀▀▄█ ▀▀ █ ▀▀ █ ▄▄█ ▀▀▄██")
    print("██▄▀▄▀▄█▄▄▄█▄▄▄▄████ ▀▀▄█▄██▄█ █████▄███▄██▄██▄█▄██▄███▄▄▄██▄██▄█▄▄█▄██▄█ ████▄▄▄█▄█▄▄██")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    time.sleep(1)
    print("---------------------------------------Choose Action------------------------------------")
    time.sleep(1)
    # show menu
    menu = str(input("[0] Grab captchas\n[1] Flush captcha folder\n[99] Exit Web Captcha Scraper\n----------------------------------------------------------------------------------------\n"))
    if menu == "0":
        time.sleep(1)
        print("----------------------------------------------------------------------------------------")
        time.sleep(1)
        # ask for captcha count
        captchas = int(input("How many captchas do you want? "))
        global driver
        driver = webdriver.Chrome()
        driver.get("https://registrieren.web.de/")
        global grabbed
        grabbed = 0
        global captchaCount
        captchaCount = 0
        # grab captchas x times
        while captchas > grabbed:
            grabCaptchas()
        if captchas == grabbed:
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            time.sleep(1)
            print("WEB Captcha Scraper is done scraping, what do you want to do now?")
            driver.close()
            wtd = str(input("[0] Return to main-menu\n[1] Exit WCS\n----------------------------------------------------------------------------------------\n"))
            if wtd == "0":
                time.sleep(1)
                print("----------------------------------------------------------------------------------------")
                cls()
                main()
            elif wtd == "1":
                time.sleep(1)
                print("----------------------------------------------------------------------------------------")
                time.sleep(1)
                print("Thanks for scraping with WEB Captcha Scraper")
                time.sleep(1)
                print("----------------------------------------------------------------------------------------")
                exit(0)
        if captchas == 0:
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            time.sleep(1)
            print("Option not available, restarting menu thread...")
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            cls()
            main()
    elif menu == "1":
        # flush captcha folder
        if os.path.exists("scraped"):
            shutil.rmtree('scraped')
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            time.sleep(1)
            print("Captcha folder removed.")
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            time.sleep(1)
            wtd = str(input("[0] Return to main-menu\n[1] Exit WCS\n----------------------------------------------------------------------------------------\n"))
            if wtd == "0":
                time.sleep(1)
                print("----------------------------------------------------------------------------------------")
                cls()
                main()
            elif wtd == "1":
                time.sleep(1)
                print("----------------------------------------------------------------------------------------")
                time.sleep(1)
                print("Thanks for scraping with WEB Captcha Scraper")
                time.sleep(1)
                print("----------------------------------------------------------------------------------------")
                exit(0)
        else:
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            time.sleep(1)
            print("Captcha folder doesn't exist, restarting menu thread...")
            time.sleep(1)
            print("----------------------------------------------------------------------------------------")
            cls()
            main()
    elif menu == "99":
        time.sleep(1)
        print("----------------------------------------------------------------------------------------")
        time.sleep(1)
        print("Thanks for scraping with WEB Captcha Scraper")
        time.sleep(1)
        print("----------------------------------------------------------------------------------------")
        exit(0)

    else:
        time.sleep(1)
        print("----------------------------------------------------------------------------------------")
        time.sleep(1)
        print("Option not available, restarting menu thread...")
        time.sleep(1)
        print("----------------------------------------------------------------------------------------")
        cls()
        main()


main()
