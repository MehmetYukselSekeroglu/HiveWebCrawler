from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse





"""
            Prime Security | ThiHive @ WebCrawler 

Version         :   __VERSION__
Author          :   __AUTHOR__

"""

# app vendor and version info 
__VERSION__ = "0.1.4"
__AUTHOR__ = "Prime Security"

class WebCrawler():    
    def __init__(self) -> None:
        
        # excluded href target/s
        self.HREF_BLACKLIST = [
            "javascript:;", "_banlk", "__blank","#","javascript:__doPostBack","javascript:void(0);"
        ]    
    
        # excluded image type 
        self.IMAGE_BLACKLIST = ["data:image/svg+xml;",]
        
        # excluded image extensions 
        self.IMAGE_EXTENSION_BLACKLIST = [".svg"]
        
        # for direct URL based image crawling 
        self.IMAGE_LINK_EXTENSIONS = [".png",".jpg",".jpeg",".webm",".tiff",".psd",".eps",".raw"]
        
        
    def prepare_string(self, target_str:str) -> str:
        """
        Args:
            target_str (str): prepare space and other chars

            example input: "    0 555 44 22 11 "
        Returns:
            str: your proccessed data
            example output: "0 555 44 22 11"
        """
        first_numeric_detected = False
        detected_data = ""
        
        for single_char in target_str:
            
            if first_numeric_detected:
                detected_data += single_char
                continue
            
            if single_char == " ":
                pass
            else:
                detected_data += single_char
                first_numeric_detected = True
                
        return detected_data
    
    
    def search_email_address(self,target_str) -> list:
        """
        Args:
            target_str (any): search target

        Returns:
            list: [ bool, str] 
                    |       |-> if success -> phone number else -> error message
                    |-> if success True else False 
        """
        detected_data = self.prepare_string(target_str=target_str)
        if len(detected_data) == 0:
            return [False, "String is null"]


        if detected_data[0:7].lower() != "mailto:":
            return [False, "No email in string"]
        
        detected_data = detected_data.lower()
        detected_data = detected_data.replace("mailto:","")
        detected_data = detected_data.replace(" ","")
        
        if len(detected_data) == 0:
            return [False, "No phone in string"]

        return [True, detected_data]
        
    
    
    def search_phone_numbers(self,target_str:str)->list:
        
        detected_data = self.prepare_string(target_str=target_str)
        if len(detected_data) == 0:
            return [False, "String is null"]


        if detected_data[0:4].lower() != "tel:":
            return [False, "No phone in string"]
        
        # clear string proccess
        detected_data = detected_data.lower()
        detected_data = detected_data.replace("tel:","")
        detected_data = detected_data.replace(" ","")
        detected_data = detected_data.replace("(","")
        detected_data = detected_data.replace(")","")
            
        if len(detected_data) == 0:
            return [False, "No phone in string"]

        return [True, detected_data]
    
    
    def crawl_phone_number_from_text(self,response_text:str) -> dict:
        try:
            pass
        
        except Exception as err:
            pass
        
    
    def crawl_email_address_from_text(self,response_text:str) -> dict:
        try:
            pass
        
        except Exception as err:
            pass
    
    def crawl_email_address_from_response_href(self,response_text:str) -> dict:
        """
        Args:
            response_text (str): request answer text

        Returns:
            dict: 
            {
                "success": (bool),
                "data_array": (list) [title, url],
                "message": (str) error code or feedback
            }
        """

        
        soup_data = BeautifulSoup(response_text, "html.parser")

        results_dict = {
            "success":False,
            "data_array":[],
            "message":""
        }
        
        buffer_list = []
        
        for single_link in soup_data.select("a"):
            
            href_target = None
            href_title = None
            if "href" in single_link.attrs.keys():
                check_href_target = single_link.attrs["href"]
                if not self.is_null(check_href_target):
                    href_target = check_href_target
                    
            if "title" in single_link.attrs.keys():
                check_href_title = single_link.attrs["title"]
                if not self.is_null(check_href_title):
                    href_title = check_href_title

            if href_target is not None:
                result_is = self.search_email_address(target_str=href_target)
                if result_is[0] == True:
                    buffer_list.append([href_title, result_is[1]])
            
        
        
        results_dict["data_array"] = buffer_list
        
        if len(results_dict["data_array"]) == 0:
            results_dict["message"] = "No email detected in page"
        else:
            results_dict["success"] = True
            results_dict["message"] = "Proccess successfuly"
        
        
        return results_dict
        
        
    
    def crawl_phone_number_from_response_href(self,response_text:str) -> dict:
        """
        Args:
            response_text (str): request answer text

        Returns:
            dict: 
            {
                "success": (bool),
                "data_array": (list) [title, phone_number],
                "message": (str) error code or feedback
            }
        """

        
        soup_data = BeautifulSoup(response_text, "html.parser")

        results_dict = {
            "success":False,
            "data_array":[],
            "message":""
        }
        
        buffer_list = []
        
        for single_link in soup_data.select("a"):
            
            href_target = None
            href_title = None
            if "href" in single_link.attrs.keys():
                check_href_target = single_link.attrs["href"]
                if not self.is_null(check_href_target):
                    href_target = check_href_target
                    
            if "title" in single_link.attrs.keys():
                check_href_title = single_link.attrs["title"]
                if not self.is_null(check_href_title):
                    href_title = check_href_title

            if href_target is not None:
                result_is = self.search_phone_numbers(target_str=href_target)
                if result_is[0] == True:
                    buffer_list.append([href_title, result_is[1]])
            
        
        
        results_dict["data_array"] = buffer_list
        results_dict["data_array"] = buffer_list
        
        if len(results_dict["data_array"]) == 0:
            results_dict["message"] = "No phone detected in page"
        else:
            results_dict["success"] = True
            results_dict["message"] = "Proccess successfuly"
        return results_dict
        
        
        
        
    
    def crawl_links_from_pesponse_href(self,original_target_url:str,response_text:str,only_address:bool=False) -> dict:
        """_summary_

        Args:
            original_target_url (str): original url for feedback
            response_text (str): request answer text
            only_address (bool, optional): full address or only url. Defaults to False.

        Returns:
            dict: 
            {
                "success": (bool),
                "data_array": (list) [title, url],
                "original_url":original_target_url,
                "message": (str) error code or feedback
            }
        """
        
        original_target_url = str(original_target_url)
        
        if not original_target_url.endswith("/"):
            original_target_url += "/"
        
        
        soup_data = BeautifulSoup(response_text, "html.parser")

        results_dict = {
            "success":False,
            "data_array":[],
            "original_url":original_target_url,
            "message":"",
        }
        
        for single_link in soup_data.select("a"):
            
            href_target = None
            href_title = None
            
            if "href" in single_link.attrs.keys():
                check_href_target = single_link.attrs["href"]
                if not self.is_null(check_href_target) and check_href_target not in self.HREF_BLACKLIST:
                    href_target = check_href_target
            
            if "title" in single_link.attrs.keys():
                check_href_title = single_link.attrs["title"]
                if not self.is_null(check_href_title):
                    href_title = check_href_title

            if href_target is not None:
                if href_target.startswith("/"):
                    href_target = original_target_url + href_target[1:]
        
                if only_address:
                    href_target = href_target.split("?")
                    href_target = href_target[0]
                
                if not href_target.startswith("http://") and not href_target.startswith("https://"):
                    if href_target.startswith(urlparse(original_target_url).netloc) or href_target.startswith("www.") :
                          href_target = urlparse(original_target_url).netloc + "://" + href_target
                    else:
                        if href_target.startswith("#/"):
                            href_target = href_target[2:]
                
                        href_target ="https://"+ urlparse(original_target_url).netloc + "/" + href_target  
                          
                          
                if href_target.startswith("#"):
                    href_target = None
                
                if href_target.endswith(str(urlparse(href_target).netloc+"/")) or href_target.endswith(str(urlparse(href_target).netloc+"/#")) or href_target.endswith(str(urlparse(href_target).netloc+"/#!")):
                    href_target = None

                analysed_url = urlparse(href_target)
                
                
                if not analysed_url.scheme and href_target != None:
                    href_target = original_target_url + href_target
                
            if href_target is not None:
                results_dict["data_array"].append( [ href_target, href_title ])
        
        # set possible status
        if len(results_dict["data_array"]) == 0:
            results_dict["success"] = False
            results_dict["message"] = "No link detected in url"
        else:
            results_dict["success"] = True
            results_dict["message"] = "Proccess successfuly"
            
        return results_dict
        
        
    def send_request(self,target_url,timeout_sec=5,req_headers:dict=None) -> dict:
        """_summary_

        Args:
            target_url (_type_): _description_
            timeout_sec (int, optional): _description_. Defaults to 5.
            req_headers (dict, optional): _description_. Defaults to None.

        Returns:
            dict:
                {
                    "success":False,
                    "message":f"Web request failed, status code: {send_request.status_code}",
                    "url":target_url,
                    "status_code":send_request.status_code,
                    "timeout_val":timeout_sec,
                    "method":"get",
                    "data":None
                }
        """
        
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
                    "status_code":send_request.status_code,
                    "timeout_val":timeout_sec,
                    "method":"get",
                    "data":None
                }
            
            return {
                "success":True,
                "message":f"Web request success",
                "url":target_url,
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
                "status_code":None,
                "timeout_val":timeout_sec,
                "method":"get",
                "data":None
            }
            
            

    def is_null(self,data) -> bool:
        """
        Args:
            data (any): target string data

        Returns:
            bool -> if string is null return True else False 
        """
        if data ==None:
            return True
        if len(str(data)) == 0:
            return True
        if str(data).lower() == "none":
            return True
        
        return False 



    def crawl_image_from_response(self,response_text:str,original_url:str,exclude_svg=True,only_address=False) -> dict:
        """_summary_

        Args:
            response_text (str): _description_
            original_url (str): _description_
            exclude_svg (bool, optional): _description_. Defaults to True.
            only_address (bool, optional): _description_. Defaults to False.

        Returns:
            dict: 
                {
                "success":False, -> bool | proccess status
                "data_array":[], -> list | your data
                "original_url":original_url -> str | feedback url
                }
        """
        soup_data = BeautifulSoup(response_text, "html.parser")

        if not original_url.endswith("/"):
            original_url += "/"

        results_dict = {
            "success":False,
            "data_array":[],
            "original_url":original_url
        }

        for image in soup_data.select("img"):    
            image_url = None
            image_alt = None
            image_title = None

            if "title" in image.attrs.keys():
                image_check_title = image.attrs['title']
                if not self.is_null(image_check_title):
                    image_title = image_check_title

            if "alt" in image.attrs.keys():

                image_check_alt = image.attrs['alt']
                if not self.is_null(image_check_alt):
                    image_alt = image_check_alt

            if "src" in image.attrs.keys():
                image_check_url = image.attrs['src']
                if not self.is_null(image_check_url):
                
                
                    if image_check_url.startswith("/"):
                        image_check_url = original_url + image_check_url[1:]

                    if not image_check_url.startswith("http://") and not image_check_url.startswith("https://"):
                        if image_check_url.startswith(urlparse(original_url).netloc):
                            image_check_url = "https://" + image_check_url
                        else:
                        
                            if image_check_url.startswith("#/"):
                                image_check_url = image_check_url[2:]
                        
                            image_check_url ="https://"+ urlparse(original_url).netloc + "/" + image_check_url
                    
                    image_url = image_check_url

            if "data-src" in image.attrs.keys():
                image_check_url = image.attrs['data-src']
                if not self.is_null(image_check_url):
                    image_url = image_check_url

            if image_url is not None and exclude_svg:
                exluce_parser = image_url
                if "?" in image_url:
                    exluce_parser = image_url.split("?")
                    exluce_parser = exluce_parser[0]
                if exluce_parser.endswith(".svg")  or "data:image/svg+xml;" in exluce_parser:
                    image_url = None
                    
            
            if image_url is not None:
                if image_url.startswith("/"):
                    image_url = original_url + image_url[1:]
                
                if image_url.startswith("www."):
                    image_url = "https://" + image_url

                if image_url.startswith("#"):
                    image_url = None
                
                analysed_url = urlparse(image_url)
                
                
                if not analysed_url.scheme and image_url != None:
                    image_url = original_url + image_url



            if image_url is not None:    
                results_dict["data_array"].append( [ image_url, image_alt, image_title ])


        # Direct image link detections ( Direcyory index etc..)
        
        for single_link in soup_data.select("a"):
            
            href_target = None
            href_title = None
            
            if "href" in single_link.attrs.keys():
                check_href_target = single_link.attrs["href"]
                if not self.is_null(check_href_target) and check_href_target not in self.HREF_BLACKLIST:
                    href_target = check_href_target
            
            if "title" in single_link.attrs.keys():
                check_href_title = single_link.attrs["title"]
                if not self.is_null(check_href_title):
                    href_title = check_href_title

            if href_target is not None:
                if href_target.startswith("/"):
                    href_target = original_url + href_target[1:]
        
                
                href_target = href_target.split("?")
                href_target = href_target[0]
                
                if href_target.startswith("www."):
                    href_target = "https://" + href_target

                if href_target.startswith("#"):
                    href_target = None
                

                analysed_url = urlparse(href_target)
                
                
                if not analysed_url.scheme and href_target != None:
                    href_target = original_url + href_target
            
            
            if href_target is not None:
                for extensions in self.IMAGE_LINK_EXTENSIONS:
                    if href_target.lower().endswith(extensions):
                        results_dict["data_array"].append( [ href_target, href_title ])
                        break

        if len(results_dict["data_array"]) == 0:
            results_dict["success"] = False
            results_dict["message"] = "No link detected in url"
        else:
            results_dict["success"] = True
            results_dict["message"] = "Proccess successfuly"
        return results_dict
        




        results_dict["success"] = True

        return results_dict


# For develop stage tests
if __name__ =="__main__":
    
    static_test_url = "https://www.hurriyet.com.tr/bizeulasin/"
    static_test_url = "https://www.google.com/"
    
    response_data = requests.get(static_test_url,timeout=3)

    if not response_data.ok:
        print(response_data.status_code)
        exit(1)
        
    toolkit = WebCrawler()
    a = toolkit.send_request(target_url=static_test_url)
    #print(a)
    result_is = toolkit.crawl_image_from_response(response_text=a["data"],original_url=static_test_url) 
    
    print(result_is)
    #original_url = result_is["original_url"]
    original_url = static_test_url
    
    for single_list in result_is["data_array"]:
        
        url = single_list[0]
        title = single_list[1]
        
        print("*"*100)
        print(f"href_target: {url}")
        print(f"title: {title}")
        print(f"Original URL: {original_url}")