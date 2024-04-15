# How To Install

`pip install HiveWebCrawler`


# Example:

## Sending requests:

```python
# Code
from HiveWebCrawler.Crawler import WebCrawler
CrawlerToolkit = WebCrawler()
request_data = CrawlerToolkit.send_request(target_url="https://google.com")
print(request_data.keys())


# Output 
dict_keys(['success', 'message', 'url', 'status_code', 'timeout_val', 'method', 'data'])
```



## Crawling link from response:

```python
# import Crawler
from HiveWebCrawler.Crawler import WebCrawler

# toolkit init
CrawlerToolkit = WebCrawler()

# sending http/s requests
request_data = CrawlerToolkit.send_request(target_url="https://google.com")

# checking status
if not request_data["success"]:
    print(request_data["message"])
    exit(1)
    
# Crawling links
crawled_links = CrawlerToolkit.crawl_links_from_pesponse_href(
    original_target_url="https://google.com",   # For feedback
    response_text=request_data["data"]
    )

# checking status
if not crawled_links["success"]:
    print(request_data["message"])
    exit(1)
    
# print dict keys
print(crawled_links.keys())


# print crawled links
for single_list in crawled_links["data_array"]:
    print(single_list)



# OUTPUT

dict_keys(['success', 'data_array', 'original_url', 'message']) # dict keys

# Crawled links
['https://www.google.com/imghp?hl=tr&tab=wi', None]
['https://maps.google.com.tr/maps?hl=tr&tab=wl', None]
['https://play.google.com/?hl=tr&tab=w8', None]
['https://www.youtube.com/?tab=w1', None]
['https://news.google.com/?tab=wn', None]
['https://mail.google.com/mail/?tab=wm', None]
['https://drive.google.com/?tab=wo', None]
['https://www.google.com.tr/intl/tr/about/products?tab=wh', None]
['http://www.google.com.tr/history/optout?hl=tr', None]
['https://google.com/preferences?hl=tr', None]
['https://accounts.google.com/ServiceLogin?hl=tr&passive=true&continue=https://www.google.com/&ec=GAZAAQ', None]
['https://google.com/advanced_search?hl=tr&authuser=0', None]
['https://google.com/intl/tr/ads/', None]
['http://www.google.com.tr/intl/tr/services/', None]
['https://google.com/intl/tr/about.html', None]
['https://www.google.com/setprefdomain?prefdom=TR&prev=https://www.google.com.tr/&sig=K_nBMpLM40cwVr7j5Oqk31t_0TCeo%3D', None]
['https://google.com/intl/tr/policies/privacy/', None]
['https://google.com/intl/tr/policies/terms/', None]
                                                            
```

## Crawling Image From Response:


```python
# import Crawler
from HiveWebCrawler.Crawler import WebCrawler

# toolkit init
CrawlerToolkit = WebCrawler()

# sending http/s requests
request_data = CrawlerToolkit.send_request(target_url="https://google.com")

# checking status
if not request_data["success"]:
    print(request_data["message"])
    exit(1)
    
# Crawling Images
crawled_links = CrawlerToolkit.crawl_image_from_response(
    original_url="https://google.com",
    response_text=request_data["data"]
    )


# checking status
if not crawled_links["success"]:
    print(request_data["message"])
    exit(1)
    
# print dict keys
print(crawled_links.keys())


# print crawled Images
for single_list in crawled_links["data_array"]:
    print(single_list)


# OUTPUT 

dict_keys(['success', 'data_array', 'original_url']) # dict keys

# Crawled Images
['https://google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png', 'Google', None]
['https://google.com/textinputassistant/tia.png', None, None]

```


## Crawling Phone Number OR Email address


### E-mail


```python
# import Crawler
from HiveWebCrawler.Crawler import WebCrawler

# toolkit init
CrawlerToolkit = WebCrawler()

# sending http/s requests
request_data = CrawlerToolkit.send_request(target_url="https://www.hurriyet.com.tr/bizeulasin/")

# checking status
if not request_data["success"]:
    print(request_data["message"])
    exit(1)
    
# Crawling email/s
crawled_links = CrawlerToolkit.crawl_email_address_from_response_href(response_text=request_data["data"])



# checking status
if not crawled_links["success"]:
    print(request_data["message"])
    exit(1)
    
# print dict keys
print(crawled_links.keys())


# print crawled email/s
for single_list in crawled_links["data_array"]:
    print(single_list)


# OUTPUT 

dict_keys(['success', 'data_array', 'message']) # dict keys

# Crawled emails
[None, 'CENSORED@hurriyet.com.tr']
                                      
```

### Phone Numbers


```python
# import Crawler
from HiveWebCrawler.Crawler import WebCrawler

# toolkit init
CrawlerToolkit = WebCrawler()

# sending http/s requests
request_data = CrawlerToolkit.send_request(target_url="https://www.hurriyet.com.tr/bizeulasin/")

# checking status
if not request_data["success"]:
    print(request_data["message"])
    exit(1)
    
# Crawling phone numbers
crawled_links = CrawlerToolkit.crawl_phone_number_from_response_href(response_text=request_data["data"])



# checking status
if not crawled_links["success"]:
    print(request_data["message"])
    exit(1)
    
# print dict keys
print(crawled_links.keys())


# print crawled phone numbers
for single_list in crawled_links["data_array"]:
    print(single_list)


# OUTPUT 
dict_keys(['success', 'data_array', 'message']) # dict keys
[None, '+90XXXXXXXXXXX'] # Crawled phone numbers

```

