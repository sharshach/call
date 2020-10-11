# Calling Web Site
runs on python (django) where we can be able to call from frontend through any device connected on local network.

### Required Apps/Frameworks
- termux (android app)
- termux-api (android app)

### Working Procedure
We can initiate get req from frontend / website from which a backend api is called.
The backend process will execute a termux script which makes the call

### Instalation Procedure
- After installing termux
  - install python and django
  - git and vim for easy 
  - follow this script

(STFW if you need any help in the commands)

- apt update && apt upgrade
- pkg install python
- pip install django
- apt install git
- pkg install vim
##### INSTALATION
- fork and clone the repo and navigate to that code ([visit this for basic git](https://JOURNEY-CP.github.io/NOTES/GIT))
- cp data_saample.json data.json
- python manage.py migration
- python manage.py runserver

### Usage Tips
- update data.json file with the contacts you mostly used (follow same pattern as in file)
- try to run with hotspot
  
### caution
- dont run the app on public networks (all people who are on same network can make calls)
- !!!!!!!!dont run on your collage / company wifi toooooo :cool !!!!!!!!!!!!