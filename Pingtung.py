import urllib.request as req
def getData(url):
    url="https://www.google.com/search?q=%E5%B1%8F%E6%9D%B1%E6%B8%AF%E5%BC%8F&rlz=1C1CAFC_enTW886TW886&biw=1280&bih=576&tbm=lcl&sxsrf=AOaemvJO19X0HuTv2cl583gR_-aP91JIlg%3A1634110822009&ei=Zo1mYZcF7pKvvA-OmreICg&oq=%E5%B1%8F%E6%9D%B1%E6%B8%AF%E5%BC%8F&gs_l=psy-ab.3..0i512k1l10.44265.46308.0.46958.8.8.0.0.0.0.131.742.7j1.8.0....0...1c.1j4.64.psy-ab..0.5.471...0i333k1.0.GLXlkf77k6A#rlfi=hd:;si:;mv:[[23.190942416869365,122.12928818785178],[22.12389088876266,119.76722764097678],null,[22.658453621071423,120.94825791441428],9]"
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="dbg0pd")
    for title in titles:
        if title.string != None:
            print(title.string)
        else:
            print(title.div)
    nextLink="https://www.google.com/search?q=%E5%B1%8F%E6%9D%B1%E6%B8%AF%E5%BC%8F&amp;rlz=1C1CAFC_enTW886TW886&amp;biw=471&amp;bih=576&amp;tbs=lf:1,lf_ui:9&amp;tbm=lcl&amp;sxsrf=AOaemvLCaD3_KmhiiAnWL5s9vLoAf6zZOA:1634116355382&amp;ei=A6NmYZbgFpHj0ASakZzAAg&amp;start=40&amp;sa=N&amp;ved=2ahUKEwjW7YjnhcfzAhWRMZQKHZoIByg4FBDy0wN6BQgBEIUC"
    print(nextLink)
pageURL="https://www.google.com/search?sa=X&rlz=1C1CAFC_enTW886TW886&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=AOaemvIohuYxK-HQvnVsmWbAzGBWro6mfA:1634114683422&q=%E5%B1%8F%E6%9D%B1%E6%B8%AF%E5%BC%8F&rflfq=1&num=10&ved=2ahUKEwiY0ejJ_8bzAhVFL6YKHViTAs4QjGp6BAgGEFc&biw=471&bih=576&dpr=1.5#rlfi=hd:;si:;mv:[[22.697333,120.54396989999998],[22.443407999999998,120.4429155]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9]"
getData(pageURL)
# count=0
# while count<2:
#     pageURL="https://www.google.com"+getData(pageURL)
#     count+=1