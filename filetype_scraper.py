from scraper import *

class FiletypeScraper(Scraper):
    def get_sources(self):
        sufix = "1abcdefghijklmnopqrstuvwxyz"
        url = "https://fileinfo.com/list/"
        return list(map(lambda x: url+x, sufix))

    def get_filetype_links(self):
        host_url = self.get_host_url()
        return [host_url+link for link in self.get_links() if link.startswith('/extension')]

    def parse_extension(self, data, data_type):
        description = dict()

        extension_scraper = Scraper()
        extension_scraper.load(data, data_type)

        try:
            info_table = extension_scraper.bs.find("table", attrs={"class": "headerInfo"})
            info_table_rows = info_table.find_all("tr")

            filetype = extension_scraper.bs.find("article").h1.b.text

            description["filetype"] = filetype.lower()

            for row in info_table_rows:
                td = row.find_all("td")

                if len(td) < 2:
                    continue

                info_name, info_value = td[:2]

                if info_name.text == "Developer":
                    description["developer"] = info_value.text
                elif info_name.text == "Category":
                    description["category"] = info_value.a.text
                elif info_name.text == "Format":
                    description["format"] = info_value.a.text
        except:
            pass

        return description

    def process(self):
        filetype_sources = self.get_sources()

        extensions_db = []

        for i, source in enumerate(filetype_sources):
            self.load(source, DataType.Url)
            extension_links = self.get_filetype_links()
            for j, extension_link in enumerate(extension_links):
                print(f'-> scan {(i+1)*(j+1)}: {extension_link}')
                extension_info = self.parse_extension(extension_link, DataType.Url)
                if extension_info != {}:
                    extensions_db.append(extension_info)

        return extensions_db