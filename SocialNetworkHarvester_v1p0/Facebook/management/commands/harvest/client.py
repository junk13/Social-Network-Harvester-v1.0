import re, requests
from sys import maxsize as MAX_INT
import time
from .globals import *
#import facebook
from SocialNetworkHarvester_v1p0.settings import FACEBOOK_APP_PARAMS


class Client:

    name = "Unnamed Facebook Client"


    def __str__(self):
        return self.name


    def __init__(self, **kwargs):
        self.access_token = kwargs['access_token']
        if not self.access_token: raise NullAccessTokenException()
        if "name" in kwargs:
            self.name = kwargs['name']
        #self.graph = facebook.GraphAPI(access_token=self.access_token)
        if not FACEBOOK_APP_PARAMS['version']:
            raise Exception("Please set FACEBOOK_APP_PARAMS values in settings")
        self.baseURL = 'https://graph.facebook.com/%s/' % FACEBOOK_APP_PARAMS['version']

    def get(self, node, **kwargs):
        url = self.baseURL + node + '?access_token=' + self.access_token
        if 'fields' in kwargs:
            strFields = self.fieldify(kwargs['fields'])
            url += '&fields=' + strFields
            kwargs.pop('fields')
        for kwarg in kwargs.keys():
            url += '&%s=%s' % (kwarg, kwargs[kwarg])
        log('calling: %s'%url)
        response = requests.get(url).json()
        self.lastRequestAt = time.time()
        if 'error' in response.keys():
            raise Exception(response['error'])
        return response

    def fieldify(self, jfields):
        s = ''
        for item in jfields:
            if isinstance(item, dict):
                for key in item.keys():
                    s += key
                    if isinstance(item[key], list):
                        s += '{' + self.fieldify(item[key]) + '}'
            else:
                s += item
            s += ','
        return s[:-1]

    def getNext(self, response):
        nextResponse = None
        if 'paging' in response and 'next' in response['paging']:
            url = response['paging']['next']
            nextResponse = requests.get(url)
            nextResponse = nextResponse.json()
        return nextResponse


def getClient():
    client = None
    while not client:
        if not clientQueue.empty():
            client = clientQueue.get()
    return client


def returnClient(client):
    assert not clientQueue.full(), "Client Queue is already full. There is a Client that has been returned twice!"
    clientQueue.put(client)


def createClient(profile):
    try:
        client = Client(
            name = "%s's facebook App"%profile.user,
            access_token = profile.fbAccessToken._token
        )
        return client
    except NullAccessTokenException:
        profile.facebookApp_parameters_error = True
        profile.save()
        facebookLogger.exception('%s has got an invalid Facebook app'%profile.user)
        return None


class ExitFlagRaised(Exception):
    pass


class NullAccessTokenException(Exception):
    def __init__(self): super(NullAccessTokenException, self).__init__("Access token cannot be null")