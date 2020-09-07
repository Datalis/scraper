from filetype_scraper import *
import json

def main():
    f_scraper = FiletypeScraper()

    print("-> Start Sraping...")
    extensions = f_scraper.process()

    with open("extension.json", "w+") as fd:
        fd.write(json.dumps(extensions))

    print("-> done!")


if __name__=="__main__":
    main()