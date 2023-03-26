# PythonWithSelenium
Python Selenium egitim dosyalarim.  
The files contained on this page include homework and exercise files created for Python Selenium library training.



Pytest Decorators :

@pytest.fixture: Fixture fonksiyonları, test fonksiyonlarından önce veya sonra otomatik olarak çalıştırılır ve testlerde kullanılacak verileri sağlar.Fixture'ların, test fonksiyonu parametrelerine eklenerek test sırasında kullanılması sağlanabilir. 


@pytest.mark.xfail:Bir testin hata vermesini bekleyen veya başarısız olmasını beklediğiniz durumlarda kullanılır. Test başarısız olduğunda, test sonucu "beklenen" bir başarısızlık olarak işaretlenir.

@pytest.mark.timeout: Belirli bir testin belirli bir süre içinde tamamlanması gerektiğinde kullanılır. Bu dekoratörü kullanarak, testin istenen zaman aşımı sınırına ulaşması durumunda testin başarısız olmasını sağlayabilirsiniz.

@pytest.mark.order: Testlerin sırasını belirlemek için kullanılır. Bu dekoratörü kullanarak, testlerin belirli bir sırayla çalışmasını sağlayabilirsiniz.

@pytest.mark.usefixtures: Belirli bir test için kullanılacak bir veya daha fazla fixture'ı belirtmek için kullanılır. Bu, testlerin daha net ve düzenli bir şekilde yazılmasını sağlar.

@pytest.mark.dependency:testler arasındaki bağımlılıkları yönetmek için kullanılır. Bu dekoratörü kullanarak, bir testin yalnızca belirli bir sırayla çalışmasını sağlayabilirsiniz. BU dekoratör icin pytest-dependency" eklentisi yüklü olmasi gerekli.

@pytest.mark.filterwarnings: Belirli hata mesajları veya uyarıları filtrelemek veya önemli hale getirmek için kullanılır. 

@pytest.mark.flaky: Testlerin belirli koşullar altında zaman zaman başarısız olabileceği durumlarda kullanılır. Bu dekoratörü kullanarak, belirli bir test için belirli bir hata oranı tanımlayabilir ve testin bu oranın üzerinde başarısız olması durumunda tekrarlanmasını sağlayabilirsiniz.


@pytest.mark.run(order): Testlerin belirli bir sırayla çalışmasını sağlamak için kullanılır. Bu dekoratörü kullanarak, belirli bir testin belirli bir sırada çalışmasını sağlayabilirsiniz.


@pytest.mark.parametrize(argnames, argvalues): Belirli bir test fonksiyonunu farklı parametrelerle çalıştırmak için kullanılır. Bu dekoratörü kullanarak, bir testi farklı parametrelerle tekrarlamak yerine, tek bir test fonksiyonunda farklı parametrelerle çalıştırabilirsiniz.
