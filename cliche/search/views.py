from typing import ContextManager
from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from django.core.paginator import Paginator


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

import math
import pymongo
import django
import requests


def search(request):
    return render(request, "search/search.html")


def list(request):
    args = {}
    AllQry = {"$or":[],}
    FirstQry = {"$or":[],}
    has_first = 0
    count = 0
    count_st = 0
    selectedDomain = [] 
    # q is a name param in url :: http://localhost:8000/search/?q=tube
    str_search = request.GET.get('q') # get parameter form param name as 'q'
    if str_search == '':
        return redirect('http://127.0.0.1:8000')
    else:
        page = int(request.GET.get('page'))
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        
        myclient = pymongo.MongoClient("mongodb+srv://gemPhatsara:lFXvlkSGRujYyR4J@cluster0.aqf8z.mongodb.net/cliche?retryWrites=true&w=majority")

        mydb = myclient["cliche"]
        mycol = mydb["searchengine"]

        limit1 = 10
        skip1 = (page-1)*limit1
        
        arr = str_search.split()

        if len(arr) > 1:

            FirstQry["$or"].append({"desc": {"$regex": str_search}})
            
            dataCursor = mycol.find(FirstQry,{"_id": 0, "keyword":0}).limit(limit1).skip(skip1)
            
            dataListFirst = []
            for row in dataCursor:
                count_st += 1
                selectedDomain.append(row['domain'])
                dict={}
                dict['domain'] = row['domain']
                dict['url'] = row['url']
                dict['desc'] = row['desc']
                dataListFirst.append(dict)

            j = 0    
            for value in dataListFirst:
                print(value)
                dataListFirst[j]['domain'] = value['domain']
                dataListFirst[j]['desc'] = value['desc'].replace(str_search, "<b>"+str_search+"</b>")
                dataListFirst[j]['url'] = value['url']
                j += 1
                

            # objDomain = mycol.find(FirstQry).limit(limit1).skip(skip1)
            # for domain in objDomain:
            #     count_st += 1
            #     selectedDomain.append(domain['domain'])

            # count_st = list_st.count()
            count += count_st
            args['list_st'] = dataListFirst
            has_first = 1
        

        for str in arr:
            AllQry["$or"].append({"domain": {"$regex": str}})
            AllQry["$or"].append({"desc": {"$regex": str}})
        dictSearch = {
                        '$and': [
                                    AllQry,
                                    { "domain": { '$nin': selectedDomain } }
                                ]
                        }    

        if 10-count < 0:
            limit2 = 0
        else:
            limit2 = 10-count
        skip2 = (page-1)*limit2

        has_second = 0
        if limit2 != 0:
            has_second = 1
            dataCursor = mycol.find(dictSearch,{"_id": 0, "keyword":0}).limit(limit2).skip(skip2)
            dataList = []
            for row in dataCursor:
                count += 1
                dict={}
                dict['domain'] = row['domain']
                dict['url'] = row['url']
                dict['desc'] = row['desc']
                dataList.append(dict)
            
            for str in arr:
                i=0
                for value in dataList:
                    dataList[i]['domain'] = value['domain']
                    dataList[i]['desc'] = value['desc'].replace(str, "<b>"+str+"</b>")
                    dataList[i]['url'] = value['url']
                    i+=1

            args['list'] = dataList

        x = range(page,page+4)
        args['AllQry'] = AllQry
        args['count'] = count
        args['str_search'] = str_search
        args['has_first'] = has_first
        args['has_second'] = has_second
        args['page'] = page
        args['npage'] = x
        args['selectedDomain'] = selectedDomain

        return render(request, "search/list.html", args)


