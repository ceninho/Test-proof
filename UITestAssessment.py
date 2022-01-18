import time
from selenium import webdriver
import os

wd = os.getcwd()

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(wd+"\\employees.html")

try:
   
  elem0= driver.find_element_by_class_name("jqx-tree-grid-collapse-button")
  elem0.click()
  elements= driver.find_elements_by_class_name('jqx-tree-grid-checkbox')
  length = len(elements)
  for i in range(length):
      elem= driver.find_elements_by_class_name('jqx-tree-grid-checkbox')[i].click()  
  elem2=driver.find_element_by_id('btn')
  elem2.click()
  ciudades= driver.find_elements_by_class_name('jqx-listitem-state-normal')
  length = len(ciudades)
  text_file = open(wd+"\\data.txt", "w")
  from datetime import datetime
  now = datetime.now()
  text_file.write("Test Performed at " +now.strftime('%Y-%m-%d %H:%M:%S')+'\n')
  for i in range(length):
      elem3= driver.find_elements_by_class_name('jqx-listitem-state-normal')[i].text
      text_file.write(elem3+'\n')
      print(elem3)
  time.sleep(5)
  text_file.close()
  driver.close()
  os.system("notepad data.txt")
except Exception as e:

    print ("Exception occured", format(e));

finally:
    driver.quit()

    print ("finally")