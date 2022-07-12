from tokenize import String
import requests
import json

URL = 'https://api.adviceslip.com/advice'

def getRandomAdvice():
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['slip']
    else:
        print(response)
        return response

def getAdviceByID(id):
    if isdigit(id):
        newURL = URL + '/' + id
        response = requests.get(newURL)
        data = json.loads(response.text)
        return data['slip']
    else:
        return "Ei! A gente pediu um número!"

def getAdviceByQuery(query):
    return query + ' is a word and this is a Stub :-*'


def bridge(params = {'params':{'id':'', 'query':''}}):
    returnData = ''
    if params['params']['id'] == '' and params['params']['query'] == '':
        returnData = getRandomAdvice()
    elif params['params']['id'] != '' : 
        returnData = getAdviceByID(params['params']['id'])
    elif params['params']['query'] != '' : 
        returnData = getAdviceByQuery(params['params']['query'])

    return returnData