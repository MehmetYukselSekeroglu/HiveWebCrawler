from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

# app vendor and version info 
__VERSION__ = "0.1.4"
__AUTHOR__ = "Prime Security"


INSTAGRAM_BASE_URL ="https://instagram.com/"

class instaCrawl():
    def __init__(self) -> None:
        pass
       
    def profile_request(self,target_username:str,timeout_sec=5,req_headers:dict=None) -> dict:
        """_summary_

        Args:
            target_username (_type_): _description_
            timeout_sec (int, optional): _description_. Defaults to 5.
            req_headers (dict, optional): _description_. Defaults to None.

        Returns:
            dict:
                {
                    "success":False,
                    "message":f"Web request failed, status code: {send_request.status_code}",
                    "url":target_url,
                    "username":target_username,
                    "status_code":send_request.status_code,
                    "timeout_val":timeout_sec,
                    "method":"get",
                    "data":None
                }
        """
        
        target_url = INSTAGRAM_BASE_URL + target_username
        
        
        try:
            request_header = {
                "User-Agent":f"{__AUTHOR__} WebCrawle {__VERSION__}"
            }            
            if req_headers is not None:
                request_header = req_headers
                
            send_request = requests.get(url=target_url,timeout=timeout_sec,headers=request_header)
            
            if not send_request.ok:
                return {
                    "success":False,
                    "message":f"Web request failed, status code: {send_request.status_code}",
                    "url":target_url,
                    "username":target_username,
                    "status_code":send_request.status_code,
                    "timeout_val":timeout_sec,
                    "method":"get",
                    "data":None
                }
            
            return {
                "success":True,
                "message":f"Web request success",
                "url":target_url,
                "username":target_username,
                "status_code":send_request.status_code,
                "timeout_val":timeout_sec,
                "method":"get",
                "data":send_request.text,
                }
        
        # if any error handled
        except Exception as err:
            return {
                "success":False,
                "message":f"Web request failed, error: {err}",
                "url":target_url,
                "username":target_username,
                "status_code":None,
                "timeout_val":timeout_sec,
                "method":"get",
                "data":None
            }
        
    
    
    
    def getProfileInfo(self, insta_username:str,timeout_sec=5,req_headers:dict=None) -> dict:
        try:
            profileInfo = self.profile_request(insta_username,timeout_sec=timeout_sec,req_headers=req_headers)
            
            if not profileInfo["success"]:
                return 
            

            parsedRequestData = BeautifulSoup(profileInfo["data"], "lxml")
            get_json_script = parsedRequestData.find_all("profile_pic_url")
            print(get_json_script)
            
            
            #print(profileInfo["data"])
        
        except Exception as err:
            pass
        
        
        
        

if __name__ == "__main__":
    toolkit = instaCrawl()
    toolkit.getProfileInfo(insta_username="mehmet_skroglu")
    




        