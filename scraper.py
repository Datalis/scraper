import enum
import urllib3
from bs4 import BeautifulSoup


class DataType(enum.Enum):
    Url=1,
    Html=2


class Scraper:
    def __init__(self):
        self.bs = None
        self.html = None
        self.url = None
        self.data_type = DataType.Url

    def load(self, data, data_type=DataType.Url):
        if data_type==DataType.Url:
            self.html = self.__get_html__(data)
            self.url = data
        else:
            self.html = data
            self.url = None

        self.data_type = data_type
        self.bs = BeautifulSoup(self.html, 'html.parser')

    def __get_html__(self, url, method='GET'):
        try:
            connection = urllib3.connection_from_url(url)
            response = connection.urlopen(url=url, method=method)
            html = response.data.decode('utf-8')
            response.close()
            connection.close()
            return html
        except:
            return ""

    def get_html(self):
        return self.html

    def remove_script(self):
        return [x.extract() for x in self.bs.find_all('script')]

    def remove_style(self):
        return [x.extract() for x in self.bs.find_all('style')]

    def get_title(self):
        title = self.bs.find('title')
        return title.text if title else ""

    def get_links(self):
        return [a.attrs['href'] for a in self.bs.find_all('a') if a.attrs.__contains__('href')]

    def get_all_tag(self, tag):
        tags = [dict([('tag_name', t.name), ('attrs', t.attrs), ('text', t.text), ('tag', str(t))])
                for t in self.bs.find_all(tag)]
        return tags

    def get_host_url(self):
        try:
            url_parts = str.split(self.url, '/')
            return f"{url_parts[0]}//{url_parts[2]}" if self.url else None
        except:
            pass
        return None

    def process(self):
        pass





