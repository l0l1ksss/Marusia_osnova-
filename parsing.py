import requests
from bs4 import BeautifulSoup





def spisok(url, limit=5):
    eminem=[]
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    header_post=soup.find_all("a", class_="tm-title__link", limit=limit)
    header_post_text=str(header_post)
    chislo=-10
    for i in header_post:
        i=str(i)
        nmb=i.find("<span>")+6
        nmb_2=i.find('/"><span>')
        # print(nmb_2, i)
        # print(i[nmb:-11])
        # eminem[i[nmb:-11]]="https://habr.com"+str(i[99:nmb_2])
        eminem.append(i[nmb:-11])
        stroka = "\n \n"
        for i in eminem:
            chislo += 1
            stroka +=str(chislo) + ": "+ i + " \n \n"
    return stroka

def tekst(url, limit=925):
    retr=""
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    texts = soup.find_all("p")
    for text in texts:
        retr+=str(text.get_text())
    retr=retr[:limit]
    retr+=f"... Статья была взята с сайта Хабр, оригинал -> \n{url}"
    print(len(retr))
    print(retr)

tekst("https://habr.com/ru/companies/rncb/articles/726182/")




