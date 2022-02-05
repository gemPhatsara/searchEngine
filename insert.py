import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["cliche"]
mycol = mydb["search"]
mylist = []
x = range(100)

for n in x:
    n = str(n)
    dict =  {
                "title": "Google "+n,
                "description": n+"Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
                "keywords": "",
                "url": "https://www.google.co.th/",
                "url_hash": "",
            }
    mylist.append(dict)

    dict = {
        "title": "Youtube "+n,
        "description": n+"Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.",
        "keywords": "",
        "url": "https://www.youtube.co.th/",
        "url_hash": "",
    }
    mylist.append(dict)

    dict = {
        "title": "Instagram "+n,
        "description": n+"Create an account or log in to Instagram - A simple, fun & creative way to capture, edit & share photos, videos & messages with friends & family.",
        "keywords": "",
        "url": "https://www.instagram.com/",
        "url_hash": "",
    }
    mylist.append(dict)

    dict = {
        "title": "Netflix "+n,
        "description": n+"Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries, and more on thousands of internet-connected devices. You can watch as much as you want, whenever you want without a single commercial – all for one low monthly price.",
        "keywords": "",
        "url": "https://www.netflix.com",
        "url_hash": "",
    }
    mylist.append(dict)

    dict = {
        "title": "Twitter "+n,
        "description": n+"We would like to show you a description here but the site won’t allow us.",
        "keywords": "",
        "url": "https://twitter.com",
        "url_hash": "",
    }
    mylist.append(dict)




mylist.append
x = mycol.insert_many(mylist)
