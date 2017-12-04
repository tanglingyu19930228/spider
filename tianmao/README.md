# selenium-抓取天猫信息

selenium python xpath

---

当我们需要爬取天猫数据的时候，天猫的网页运用了大量的js代码，普通的抓取手段根本不能正常获取到天猫的数据，其数据都是通过加载js代码获取到的，而且当你进入天猫的网页时，它的定向和验证就能让你不知所措，借助selenium模块，我们可以驱动浏览器来模拟用户行为获取数据，这是一个抓取天猫数据的范例，我们以波司登旗舰店为例，来获取天猫的数据。





程序运行依赖：
=======

下载chrome driver：
----------------

https://sites.google.com/a/chromium.org/chromedriver/downloads

若网站访问不了或者延迟特别高，则你需要一个梯子

安装selenium：
-----------

pip install selenium

运行程序会在本地生成一个csv文件，这就是我们所抓的数据

程序运行效果图：
![此处输入图片的描述][1]


  [1]: https://raw.githubusercontent.com/Csharing/spider/master/tianmao/havegetten/bosideng.png