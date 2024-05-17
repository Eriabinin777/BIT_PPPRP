docker build -t eriabinin777/my-app -f dockerfileapp .
docker build -t eriabinin777/my-client -f dockerfileclient .
docker push eriabinin777/my-app
docker push eriabinin777/my-client

kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myapp_deployment.yaml
kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myservice.yaml
kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myclient_deployment.yaml

minikube tunnel
