import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_republika():
    # Waktu scraping dilakukan
    scraping_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Mengambil halaman web
    page = requests.get("https://www.republika.co.id/")
    obj = BeautifulSoup(page.text, "html.parser")

    # Menginisialisasi list untuk menyimpan data
    data = []

    # Mengambil semua headline
    headlines = obj.find_all('h2', class_=lambda x: x and x.startswith('headline-'))

    for headline in headlines:
        # Mengambil waktu publish
        publish_time_element =  headline.find_previous_sibling('div', class_='date date-item__headline')
        print("Publish Time Element:", publish_time_element)  # Cetak elemen yang ditemukan
        if publish_time_element:
            publish_time = publish_time_element.text.split('-')[1].strip() if '-' in publish_time_element.text else ""
        else:
            publish_time = "Unknown"  # Atau sesuaikan dengan nilai default yang sesuai
        # Mengambil kategori dari parent div
        category = headline.parent.find('label', class_='label').text.strip()
        
        # Mengambil judul berita
        title = headline.text.strip()

        

        # Menambahkan data ke list
        data.append({
            "category": category,
            "title": title,
            "publish_time": publish_time
        })


    # Menambahkan waktu scraping
    data.append({
        "scraping_time": scraping_time
    })

    # Menyimpan data dalam file JSON
    with open('republika_data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Data telah disimpan dalam file republika_data.json")

# Menjalankan fungsi scraping
scrape_republika()
