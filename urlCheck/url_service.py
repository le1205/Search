import httpx
from concurrent.futures import ThreadPoolExecutor
from httpx import ConnectTimeout, ReadTimeout

class URLService:
    @staticmethod
    def check_url(site, username, result_list):
        url = site.replace('@username', username)
        try:
            with httpx.Client(timeout=(5,14)) as client:
                response = client.get(url)
                if response.status_code == 200:
                    result_list.append({url: True})
                else: 
                    result_list.append({site: False})
        except (ConnectTimeout, ReadTimeout):
            print('Request time out: ', url)
            result_list.append({site: None})
        except Exception as e:
            print('Request error: ',str(e), url)
            result_list.append({site: None})

    @staticmethod
    def is_username_present(username, URL):
        resutl_list = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(lambda site: URLService.check_url(site, username, resutl_list), URL)
        
        return resutl_list
    
    @staticmethod
    def scrape_user_instagram(username: str, session: ScrapflyClient):
        """scrape user's data"""
        result = session.scrape(ScrapeConfig(
            url=f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}", 
            headers={"x-ig-app-id": "936619743392459"},
            asp=True
        ))
        data = json.loads(result.content)
        return data['data']['user']
