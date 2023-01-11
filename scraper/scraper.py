import requests
import json

def fetch(url):
    r = requests.get(url)
    data = r.json()
    return data
  
def save(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data 
  
def main():
    appended_data = []
    # run a loop two times
  
    
    
    
    for year in range(2015, 2017):
      months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
      for count, month in enumerate(months):
        start = months[count]
        print(start)
        days = 30
        if count % 2 == 0:
          days = 31
        else:
          days = 30
        
        if start == '02':
          days = 28

        url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=bba54a37707a444f9f9112453231001&q=Kuala Lumpur&format=json&date={3}-{0}-01&enddate={3}-{1}-{2}&includelocation=yes".format(start, start, days, year)
        print(url)
        data = fetch(url)
        appended_data.append(data['data']['weather'])
    
    save(appended_data, 'weather.json')

if __name__ == '__main__':
  main()