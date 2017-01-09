import os
import subprocess
import glob
import ConfigParser
from github import Github # pip install PyGithub

## Get configuration
configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.ini'
configParser.read(configFilePath)
githubUsername = configParser.get('github_credentials', 'username')
githubPassword = configParser.get('github_credentials', 'password')
destinationPath = configParser.get('local_settings', 'destination_path')

## Set up
d = os.path.expanduser(destinationPath)
if not os.path.exists(d):
    os.makedirs(d)
os.chdir(d)

print "Using Github account: " + githubUsername

## Get list of all your github private repos.
g = Github(githubUsername, githubPassword)
theRepos = []
print "Found followig repositories:"
for repo in g.get_user().get_repos():
#    if not repo.private:
#        continue
    if repo.owner.name != g.get_user().name:
        continue    
    
    theRepos.append((repo.name, repo.clone_url))
    print repo

## Process each repo individually
for theName, theCloneURL in theRepos:
    if not os.path.exists(d + "/" + theName):
    	### Clone all non-existing repos
    	print "cloning " + theName
    	subprocess.check_call(['git', 'clone', theCloneURL, theName])
    else:
    	### Update existing repos
    	print "pulling " + theName
    	os.chdir(d + "/" + theName)
    	subprocess.check_call(['git', 'pull'])
    	os.chdir(d)
