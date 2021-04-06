# playstation-craftdemo

Below are the list of tasks this project would accomplish and the steps followed to accomplish them:

Task 1
● Create a simple CLI to quickly look up country codes.
● Write a country lookup service using your favorite programming language.
● Explore the following API ​https://www.travel-advisory.info/api
● Given country code -> return country name example.
--Steps followed to achieve this:
1. Written a python code - lookup.py and defined the function getall_countrycodes_api() to achieve this.
Test:
$ lookup --countryCode=AU
 Australia
--------------------------------------------------------------------------------
Task 2:
Task 2.a: Save the data from ​https://www.travel-advisory.info/api​ to a file called ​data.json and add functionality to your program to work with a file instead of real api endpoint.
--Steps followed to achieve this:
1. Used curl command to save the API output of ​https://www.travel-advisory.info/api​ into data.json file.
2. Written a python code - lookup_file.py and defined the function getall_countrycodes_fromfile() to achieve this.
Test:
$ lookup --countryCode=AU
 Australia
----------------------

Task 2.b: This program supports multiple country codes as input.
--Steps followed to achieve this:
Written a python code - lookup_multi.py to achieve this.
Test:
$ lookup --countryCode=AU,AI
 Australia
 Anguilla
--------------------------------------------------------------------------------
------------------------------BONUS---------------------------------------------

Task 3:
Task 3.a: Extend the tool functionality via REST.
● Convert code written in Craft demo to a REST service with two routes
--Steps followed to achieve this:
Used FLASK framework and created the app -api.py- to run on host="0.0.0.0", port=5050

Tests:
● Run $python api.py
In the browser run - http://0.0.0.0:5050/
Output - Welcome

● /health returns health of your service
In the browser run - http://0.0.0.0:5050/health
Output - Status OK

● /diag check returns status of the api ​https://www.travel-advisory.info/api​
In the browser run - http://0.0.0.0:5050/diag
Output - {"api_status": {"request": {"item": "not specified"}, "reply": {"cache": "cached", "code": 200, "status": "ok", "note": "The api works, we could fetch countries.", "count": 238}}}

● /convert – converts country name to country code
In the browser run - http://0.0.0.0:5050/convert/Australia
Output - "AU"
----------------------

Task 3.b: Create local k8s cluster on your workstation
--Steps followed to achieve this:
install kubectl - $ brew install kubectl
install virtualbox - $ brew install virtualbox
install minikube - $ brew install minikube
Start Minikube - $ minikube start --vm-driver=virtualbox --logtostderr

----------------------

Task 3.c: Deploy your service to local k8s cluster
--Steps followed to achieve this:
● Build a docker image for the app by writing a Dockerfile
● Port the installed modules into our container
● Start Minikube - $ minikube start
● Trigger the build process on the Docker host of the Minikube cluster -
$ minikube ssh
● Create a Deployment - $ kubectl run demo-backend --image=demo-backend:latest   --port=5050 --image-pull-policy Never
● Verify the Deployment - $ kubectl get deployments
● Get the Pods - $ kubectl get pods
● Create a Service to make the REST endpoint of our app available
$ kubectl expose deployment demo-backend --type=NodePort
● Verify that the service was created successfully and get the ip address and port
$ kubectl get services
● Call the backend service - $ minikube service demo-backend
This will start our default browser at http://192.168.99.100:30840/ where our service will be running

Test:
● Run $python api.py
In the browser run - http://192.168.99.100:30840/
Output - Welcome

● /health returns health of your service
In the browser run - http://192.168.99.100:30840/health
Output - Status OK

● /diag check returns status of the api ​https://www.travel-advisory.info/api​
In the browser run - http://192.168.99.100:30840/diag
Output - {"api_status": {"request": {"item": "not specified"}, "reply": {"cache": "cached", "code": 200, "status": "ok", "note": "The api works, we could fetch countries.", "count": 238}}}

● /convert – converts country name to country code
In the browser run - http://192.168.99.100:30840/convert/Australia
Output - "AU"
