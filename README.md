# BIT_PPPRP

## Задание 1

Реализовать простое веб приложение, у которого обрабатывает запросы на два endpoint’а : 
* GET /time - этот endpoint должен отдавать текущее время
* GET /statistics - этот endpoint должен отдавать количество обращений к endpoint’у /time в виде одного числа. Соответственно, ваше приложение должно хранить информацию о каждом обращении и отдавать эту информацию по запросу. 
Далее необходимо реализовать скрипт, который будет обращаться к endpoint’у GET /statistics и записывать полученный результат в файл. Этот скрипт должен будет вызываться раз в 5 секунд.

## Последовательность действий 
### Шаг 0

Установливаем minikube и docker

### Шаг 1

Запускаем наш узел minikube
```bash
minikube start
```

### Шаг 2

Запускаем файл create.sh, который отвечает за манифесты сервиса, приложения и кода
```bash
sh create.sh
```

### Шаг 3
Далее в соседнем терминале получаем нужный url для подключения к сервису
```bash
minikube service my-service
```

### Шаг 4
Чтобы узнать текущее время, нужно выполнить: 
```bash
curl my_url/time
```  

Чтобы получить статистику, нужно выполнить:  
```bash
curl my_url/statistics
```  

### Шаг 5
Узнаем  название пода с помощью команды kubectl get pods -o wide, после получаем доступ к статистике

```bash
kubectl exec -it my_pod -- /bin/bash
cat statistics.txt
```
