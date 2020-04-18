#  WebCaptchaScraper 

## Introduction

>### This program is for everyone who wants to auto-solve captchas using machine learning, this program can generate you a database of 1 to ∞ captcha samples, the standard is web.de a german mail provider but you can easily change this in code :)

## Code Samples

> ### code for the scrape method:
    # create scraped folder if not exist
    if not os.path.exists("scraped"):
        os.mkdir("scraped")
    time.sleep(2)
    # this will call the global captcha count to count how many captchas you already have
    global captchaCount
    captchaCount += 1
    # here selenium finds the captcha image via its id and then screenshots it
    try:
        driver.find_element_by_id("captchaImage").screenshot("scraped/captcha" + str(captchaCount) + ".png")
    except:
        print("Something went wrong while trying to scrape, retrying...")
        grabCaptchas()
    print("Successfully grabbed captcha no." + str(captchaCount))
    global grabbed
    grabbed += 1
    # this will refresh the site so another captcha can be scraped
    driver.refresh()


## Installation

>The easiest way of installing it, is using the release which will be updated every once in a while, but if you want to scrape captchas from another site than web.de you'll have to install [Selenium](https://pypi.org/project/selenium/) with the command: pip install selenium, after downloading this you can easily change your script and execute itwithin any shell!
