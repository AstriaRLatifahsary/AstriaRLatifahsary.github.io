import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_news():
    page = requests.get("https://www.republika.co.id/")
    obj = BeautifulSoup(page.text, "html.parser")

    print("menampilkan objek html")
    print("=======================")
    print(obj)

    print("\nmenampilkan title browser dengan tag title")
    print("=======================")
    print(obj.title)

    print("\nmenampilkan title browser tanpa tag")
    print("=======================")
    print(obj.title.text)

    print('\nmenampilkan semua tag h2')
    print("=======================")
    print(obj.find_all('h2'))

    print('\nmenampilkan semua teks h2')
    print("=======================")
    for headline in obj.find_all('h2'):
        print(headline.text)

    print('\nmenampilkan headline berdasarkan div class')
    print("=======================")
    print(obj.find_all('div', class_='title'))

    print('\nmenampilkan semua teks headline')   
    print("=======================")
    for headline in obj.find_all('h2', class_=lambda x: x and x.startswith('headline-')):
        print(headline.text.strip())

    print('\menampilkan semua headline pada file text')
    print("=======================")
    f = open('Headline.txt', 'w')
    for headline in obj.find_all('h2', class_=lambda x: x and x.startswith('headline-')):
        f.write(headline.text.strip() + '\n')
        f.write('\n')
    f.close()

    print('\menampilkan semua headline pada file json')
    print("=======================")
    data = []
    f = open('Headline.json', 'w')
    for headline in obj.find_all('h2', class_=lambda x: x and x.startswith('headline-')):
       data.append({"judul":headline.text.strip()})
    jdumps = json.dumps(data)
    f.writelines(jdumps)
    f.close()

    news_data = []

    # Menambahkan waktu pengambilan data
    scrape_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Mengambil berita
    news_items = obj.find_all('div', class_='carousel-item')
    for item in news_items:
        category_elem = item.find('label', class_='label')
        title_elem = item.find('h2')
        time_elem = item.find('span', class_='date-item__headline')

        # Memeriksa apakah semua elemen yang diperlukan ditemukan
        if category_elem and title_elem and time_elem:
            category = category_elem.text.strip()
            title = title_elem.text.strip()
            publish_time = time_elem.text.strip()

            # Menambahkan data berita ke list
            news_data.append({
                'category': category,
                'title': title,
                'publish_time': publish_time
            })
        else:
            print("Data tidak lengkap untuk satu atau lebih item berita")


    # Menambahkan waktu scraping
    news_data.append({'scrape_time': scrape_time})

    # Menyimpan data ke file JSON
    with open('news_data.json', 'w') as json_file:
        json.dump(news_data, json_file)

if __name__ == "__main__":
    scrape_news()
