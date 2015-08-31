__author__ = 'brycecarter'

import json
import urllib2


class GithubConnection:
    def __init__(self, oAuthToken):
        self.oAuthToken = oAuthToken
        self.headers = {}

    @staticmethod
    def fullUrlFromPartial(partialUrl):
        url = 'https://api.github.com/{0}'.format(partialUrl.lstrip('/'))
        return url

    def sendRequest(self, partialUrl, dataDict=None, method='POST'):
        url = self.fullUrlFromPartial(partialUrl)
        request = urllib2.Request(url)

        headers = {'Authorization': 'token {0}'.format(self.oAuthToken)}
        if method in ['POST']:
            headers["Content-Type"] = "application/json"
            dataString = json.dumps(dataDict)
            request.add_data(dataString)

        for key, value in headers.items():
            request.add_header(key, value)

        request.get_method = lambda: method
        response = urllib2.urlopen(request).read()
        return response