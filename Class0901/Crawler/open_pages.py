import os
os.system("start chrome .\page-0.html")

for i in range(10):
    os.system("start chrome .\page-"+str(i)+".html")

# i = 0
# while True:
#   try:
#     os.system("start chrome .\page-"+str(i)+".html")
#     i += 1
#   except:
#     break

os.system("powershell rm page*")
os.system("powershell rm crawed_page.html")
