import os
from pathlib import Path

def get_path(keyword, scraper):
    keyword = keyword.replace(' ','_').lower()
    dir = os.path.abspath('') + '/scrapers/data'
    filename = Path(f'{dir}/{scraper}_{keyword}.csv')
    if not filename.exists():
        with open(filename, 'w+') as f:
            f.write(',url')
            f.close()
    return filename

if __name__ == "__main__":
    get_path('keyword', 'Monsterboard')