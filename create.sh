curl -L https://istio.io/downloadIstio | sh -
export PATH="$PATH:$PWD/istio-1.21.2/bin"
istioctl install -y --set profile=demo --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
kubectl label namespace default istio-injection=enabled

docker build -t eriabinin777/my-app -f dockerfileapp .
docker build -t eriabinin777/my-client -f dockerfileclient .
docker push eriabinin777/my-app
docker push eriabinin777/my-client

kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myapp_deployment.yaml
kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myservice.yaml
kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myclient_deployment.yaml

kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/mygateway.yaml
kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myvirtual_service.yaml
kubectl apply -f /Users/rev777/Desktop/Documents/BIT_PPPRP/myentry_service.yaml

minikube tunnel
