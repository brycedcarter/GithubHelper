__author__ = 'brycecater'

import githubHelper

oAuthToken = raw_input('Enter your oAuth token')

org = 'PetRover'
repos = ['rCore', 'rWifi', 'rMotors', 'rProtocols', 'rPowerSystems', 'rSensors']
labels = [{'name': 'implementation', 'color': 'fbca04'}]

ghc = githubHelper.GithubConnection(oAuthToken)

for label in labels:
    for repo in repos:
        ghc.sendRequest('/repos/{0}/{1}/labels'.format(org, repo), dataDict=label, method='POST')
