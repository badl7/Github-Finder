# Github-Finder

Bu kodlar, bir Flask web uygulaması oluşturur. Uygulama, kullanıcının girdiği GitHub kullanıcı adını kullanarak GitHub API'sinden kullanıcı bilgilerini ve repolarını çekmekte ve sonuçları bir web sayfasında görüntülemektedir.

Uygulama, bir index() fonksiyonu içerir. Bu fonksiyon, '/' rotasına ilişkilendirilmiştir ve iki farklı HTTP isteği işlemek için tasarlanmıştır. Eğer istek bir POST isteği ise, kullanıcının girdiği GitHub kullanıcı adını kullanarak GitHub API'sinden kullanıcı bilgilerini ve repolarını çekmektedir. Eğer kullanıcı bulunamazsa bir hata mesajı gösterilir ve eğer kullanıcı bulunursa kullanıcı bilgileri ve repolar bir web sayfasında görüntülenir. Eğer istek bir GET isteği ise, uygulama kullanıcının girdiği bilgi olmadan index.html şablonunu gösterir.

Bu kodları çalıştırmak için, Flask ve requests kütüphanelerini yüklemeniz gerekir. Ayrıca, uygulama için bir GitHub API anahtarınız olması gerekmektedir.

---

These codes create a Flask web application. The application retrieves user information and repositories from the GitHub API using the GitHub username entered by the user, and displays the results on a web page.

The application includes an index() function. This function is associated with the '/' route and is designed to handle two different HTTP requests. If the request is a POST request, it retrieves user information and repositories from the GitHub API using the GitHub username entered by the user. If the user is not found, an error message is displayed, and if the user is found, the user information and repositories are displayed on a web page. If the request is a GET request, the application displays the index.html template without any information entered by the user.

To run these codes, you need to install the Flask and requests libraries. Additionally, you need to have a GitHub API key for the application.

----

* Kullanıcı girişi: Kullanıcı adının doğruluğunu doğrulamak için formda birkaç doğrulama kuralı ekle
* Güvenlik: Uygulamanın güvenliğini arttırmak için birkaç önlem 
* İşlevsellik: Uygulamanın işlevselliğini arttırmak için ekstra özellikler eklenebilir. Örneğin, kullanıcının repolarını sıralamak veya filtrelemek için seçenekler sunabilir.
* Tasarım: Uygulamanın tasarımı için ekstra CSS veya JavaScript kodları
* Performans: Veri çekme işlemlerini arka planda gerçekleştirebilir veya verileri ön bellekte saklayabilir
