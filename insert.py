import pymongo

myclient = pymongo.MongoClient("mongodb+srv://gemPhatsara:lFXvlkSGRujYyR4J@cluster0.aqf8z.mongodb.net/cliche?retryWrites=true&w=majority")

mydb = myclient["cliche"]
mycol = mydb["searchengine"]
mylist = []
x = range(50)

for n in x:
    n = str(n)
    dict =  {
                "title": "Google "+n,
                "desc": n+"Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
                "keywords": "",
                "url": "https://www.google.co.th/",
                "domain": "google",
            }
    mylist.append(dict)

    dict = {
        "title": "Youtube "+n,
        "desc": n+"Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.",
        "keywords": "",
        "url": "https://www.youtube.co.th/",
        "domain": "youtube",
    }
    mylist.append(dict)

    dict = {
        "title": "Instagram "+n,
        "desc": n+"Create an account or log in to Instagram - A simple, fun & creative way to capture, edit & share photos, videos & messages with friends & family.",
        "keywords": "",
        "url": "https://www.instagram.com/",
        "domain": "instagram",
    }
    mylist.append(dict)

    dict = {
        "title": "Netflix "+n,
        "desc": n+"Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries, and more on thousands of internet-connected devices. You can watch as much as you want, whenever you want without a single commercial – all for one low monthly price.",
        "keywords": "",
        "url": "https://www.netflix.com",
        "domain": "netflix",
    }
    mylist.append(dict)

    dict = {
        "title": "Twitter "+n,
        "desc": n+"We would like to show you a description here but the site won’t allow us.",
        "keywords": "",
        "url": "https://twitter.com",
        "domain": "twitter",
    }
    mylist.append(dict)




mylist.append
x = mycol.insert_many(mylist)
