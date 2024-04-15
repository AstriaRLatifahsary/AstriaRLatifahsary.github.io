$(document).ready(function() {
    // URL file JSON yang ingin diambil
    const jsonUrl = './js/news_data.json';

    // Fungsi untuk mengambil data JSON dan menampilkan dalam tabel
    function fetchAndDisplayData() {
        // Mengambil data JSON
        $.getJSON(jsonUrl, function(data) {
            // Mendapatkan elemen tbody dari tabel
            const $tbody = $('#scrapedDataBody');
            
            // Variabel untuk menyimpan waktu scraping
            let scrapingTime = '';

            // Mengulangi setiap item data dan membuat baris tabel
            $.each(data, function(index, item) {
                // Jika item memiliki scraping_time, simpan scraping_time
                if (item.scraping_time) {
                    scrapingTime = item.scraping_time;
                    return; // Keluar dari iterasi untuk entri ini
                }

                // Membuat elemen baris tabel
                const $row = $('<tr>');

                // Membuat elemen kolom untuk setiap atribut data
                const $kategoriCell = $('<td>').text(item.category);
                const $judulHeadlineCell = $('<td>').text(item.title);
                const $waktuPublishCell = $('<td>').text(item.publish_time);

                // Menambahkan sel ke dalam baris
                $row.append($kategoriCell, $judulHeadlineCell, $waktuPublishCell);

                // Menambahkan baris ke dalam tabel
                $tbody.append($row);
            });

            // Tampilkan waktu scraping di elemen HTML dengan ID 'scrapingTimeDiv'
            if (scrapingTime) {
                $('#scrapingTimeDiv').text(`Waktu Scraping: ${scrapingTime}`);
            }
        }).fail(function(error) {
            console.error('Error fetching data:', error);
        });
    }

    // Panggil fungsi untuk mengambil dan menampilkan data saat halaman dimuat
    fetchAndDisplayData();
    console.log('JavaScript is running');
});
