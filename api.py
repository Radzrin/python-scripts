import requests
import json
import os
import sys
import asyncio



path = 'filename'


isExist = os.path.exists(path)

if not isExist:
  print(f"Created folder named: {path}")
  os.mkdir(path)

async def main():
    i = 0 #page
    x = 0 #image
    list_Size = 100
    url = f"https://example.com/{arguments}"
    response = requests.get(url)


    while x < list_Size: 
    
        if(len(response.content) <= 2):
            print("works bozo")
            break 

        data = response.json()
        val = data[x]["file_url"] #figure out how to know if its at the final image
        x += 1    

        rp = requests.get(val) #put a try catch here to reconnect if connection fails


        if "mp4" in val:
            open(f"{path}/{path}{x}{i}.mp4", "wb").write(rp.content)
        elif "gif" in val:
            open(f"{path}/{path}{x}{i}.gif", "wb").write(rp.content)
        else:
            open(f"{path}/{path}{x}{i}.png", "wb").write(rp.content)    
        
        
    
        if(x == 99):
            url = f"https://example.com/{arguments}"
            response = requests.get(url)
            x = 0
            i += 1
        print(x," : ", i) 


    
   

       

    
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())