from selenium import webdriver

# keep chrome running

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

# driver.close()
# driver.quit()