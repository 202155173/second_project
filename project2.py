from selenium import webdriver

URL = 'https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=2771'
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
driver.get(url=URL)

table = driver.find_element_by_xpath('//*[@id="t_Table_277103"]')

year_list = []
count = 0
for tr in table.find_elements_by_css_selector('tr'):
    count += 1
    if count == 2:
        break

    cyc = 0
    for th in tr.find_elements_by_css_selector('th'):
        cyc += 1
        if cyc < 2:
            continue

        print(th.text,end=' ')
        year_list.append(th.text)

driver.close()

print('')
print(year_list)