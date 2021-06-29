# python_core
Projelerinizde kullanabileceğiniz çekirdek katman. Ayrıca UI klasörünü ve main.py dosyasını inceleyerek tüm paketlerin nasıl kullanıldığı ile ilgili demoları görebilirsiniz.
[ Update: 09.04.2021 ]
#
### Kullanılan kütüphaneler:
- sqlite3
- datetime
- json
- os
#
"Core" klasörünü projenizin ana dizinine kopyalayarak kullanabilirsiniz. Projenizde kullanılmayacak klasörleri silebilirsiniz.

NOT: Gerekli kütüphaneler yüklü değilse hata alabilirsiniz.
#
### Decorator ( [AOP](https://github.com/cihatyalman/python_core/tree/master/Core/utilities/decorators) ):
Bir fonksiyon işleve başlamadan önce, işlevi bittiğinde veya işlev sırasında bir hata aldığında başka bir işlev çalıştırmasını istiyorsanız kullanabilirsiniz.

Örnek olarak, işlevden önce bir doğrulama yaptırabilirsiniz, işlevden sonra bir log kaydı yaptırabilirsiniz, hata aldığında işlevden başka bir veri dönüşü yaptırabilirsiniz.
#
### Result ( [results](https://github.com/cihatyalman/python_core/tree/master/Core/utilities/results) ):
Bir fonsiyonun belli bir kalıpta sonuç dönmesini istiyorsanız kullanabilirsiniz. 

Örnek olarak, "success, message" döndürebilirsiniz veya "success, message, data" döndürebilirsiniz.
#
### Local Database ( [local_database](https://github.com/cihatyalman/python_core/blob/master/Core/local_database/sqlite_base.py) ):
Verilerinizi local bir veritabanında yönetmek istiyorsanız bu paketi kullanabilirsiniz.
#
### Datetime İşlemleri ( [datetime_operations](https://github.com/cihatyalman/python_core/blob/master/Core/datetime_operations/datetime_core.py) ):
Geçerli tarihi (gmt ayarlanabilir) timestamp olarak kullanabilirsiniz. Ayrıca istenildiği zaman datetime ve timestamp arası dönüşümler yapabilirsiniz.
#
### Json Dosya İşlemleri ( [json_file_operations](https://github.com/cihatyalman/python_core/blob/master/Core/json_file_operations/json_file_base.py) ):
Json türünde olan verilerinizi bir dosyada tutmak isterseniz kullanabilirsiniz.
#
