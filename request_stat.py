import requests
import time

url = "http://app-service/statistics"
output_file = "statistics.txt"

def recoder(url, output_file):
    try:
        response = requests.get(url)  
        if response.status_code == 200:  
            with open(output_file, 'a') as f: 
                f.write(response.text + '\n')
        else:
            with open(output_file, 'a') as f:  
                f.write(f'Error: Status Code {response.status_code}\n')
    except requests.RequestException as e:
        with open(output_file, 'a') as f:  
            f.write(f'Error: {str(e)}\n')
    time.sleep(5)

while True:
    recoder(url, output_file)
