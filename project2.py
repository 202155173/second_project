from selenium import webdriver
import matplotlib
import matplotlib.pyplot as plt

URL = 'https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=2771'
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
driver.get(url=URL)

table = driver.find_element_by_xpath('//*[@id="t_Table_277103"]')

year_list = []
p_lists = []
count = 0
for tr in table.find_elements_by_css_selector('tr'):
    p_list = []
    count += 1
    if count == 2:
        continue

    cyc = 0
    for th in tr.find_elements_by_css_selector('th'):
        cyc += 1
        if cyc < 2:
            continue

        print(th.text,end=' ')
        year_list.append(th.text)

    for td in tr.find_elements_by_css_selector('td'):
        print(td.text,end=' ')
        p_list.append(td.text)

    print('')
    if count == 1:
        continue
    p_lists.append(p_list)

driver.close()

total_list = [float(i) for i in p_lists[0]]
man_list = [float(i) for i in p_lists[1]]
woman_list = [float(i) for i in p_lists[2]]

print('')
print(year_list)
print(total_list)
print(man_list)
print(woman_list)

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')

plt.plot(range(1,10),total_list,color='lightgray',linewidth=2.5,label='전체')
plt.plot(range(1,10),man_list,color='lightskyblue',linewidth=2.5,label='남자')
plt.plot(range(1,10),woman_list,color='lightpink',linewidth=2.5,label='여자')
plt.suptitle('연도별 흡연율')
plt.xticks(range(1,10),year_list,fontsize=9)
plt.xlabel('연도',fontsize=9)
plt.ylabel('(단위:%)',fontsize=9)
plt.legend()
plt.show()