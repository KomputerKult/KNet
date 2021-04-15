# KomputerNet [![Build Status](https://travis-ci.org/HelloKomputerNet/KomputerNet.svg?branch=master)](https://travis-ci.org/HelloKomputerNet/KomputerNet) [![Documentation](https://img.shields.io/badge/docs-faq-brightgreen.svg)](https://komputernet.io/docs/faq/) [![Help](https://img.shields.io/badge/keep_this_project_alive-donate-yellow.svg)](https://komputernet.io/docs/help_komputernet/donate/)

[简体中文](./README-zh-cn.md)
[English](./README.md)

Децентрализованные вебсайты использующие Bitcoin криптографию и BitTorrent сеть - https://komputernet.io


## Зачем?

* Мы верим в открытую, свободную, и не отцензуренную сеть и коммуникацию.
* Нет единой точки отказа: Сайт онлайн пока по крайней мере 1 пир обслуживает его.
* Никаких затрат на хостинг: Сайты обслуживаются посетителями.
* Невозможно отключить: Он нигде, потому что он везде.
* Быстр и работает оффлайн: Вы можете получить доступ к сайту, даже если Интернет недоступен.


## Особенности
 * Обновляемые в реальном времени сайты
 * Поддержка Namecoin .bit доменов
 * Лёгок в установке: распаковал & запустил
 * Клонирование вебсайтов в один клик
 * Password-less [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)
   based authorization: Ваша учетная запись защищена той же криптографией, что и ваш Bitcoin-кошелек
 * Встроенный SQL-сервер с синхронизацией данных P2P: Позволяет упростить разработку сайта и ускорить загрузку страницы
 * Анонимность: Полная поддержка сети Tor с помощью скрытых служб .onion вместо адресов IPv4
 * TLS зашифрованные связи
 * Автоматическое открытие uPnP порта
 * Плагин для поддержки многопользовательской (openproxy)
 * Работает с любыми браузерами и операционными системами


## Как это работает?

* После запуска `komputernet.py` вы сможете посетить зайты (komputernet сайты) используя адрес
  `http://127.0.0.1:43110/{komputernet_address}`
(например. `http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D`).
* Когда вы посещаете новый сайт komputernet, он пытается найти пиров с помощью BitTorrent
  чтобы загрузить файлы сайтов (html, css, js ...) из них.
* Каждый посещенный зайт также обслуживается вами. (Т.е хранится у вас на компьютере)
* Каждый сайт содержит файл `content.json`, который содержит все остальные файлы в хэше sha512
  и подпись, созданную с использованием частного ключа сайта.
* Если владелец сайта (у которого есть закрытый ключ для адреса сайта) изменяет сайт, то он/она
  подписывает новый `content.json` и публикует его для пиров. После этого пиры проверяют целостность `content.json`
  (используя подпись), они загружают измененные файлы и публикуют новый контент для других пиров.

####  [Слайд-шоу о криптографии KomputerNet, обновлениях сайтов, многопользовательских сайтах »](https://docs.google.com/presentation/d/1_2qK1IuOKJ51pgBvllZ9Yu7Au2l551t3XBgyTSvilew/pub?start=false&loop=false&delayms=3000)
####  [Часто задаваемые вопросы »](https://komputernet.io/docs/faq/)

####  [Документация разработчика KomputerNet »](https://komputernet.io/docs/site_development/getting_started/)


## Скриншоты

![Screenshot](https://i.imgur.com/H60OAHY.png)
![ZeroTalk](https://komputernet.io/docs/img/zerotalk.png)

#### [Больше скриншотов в KomputerNet документации »](https://komputernet.io/docs/using_komputernet/sample_sites/)


## Как вступить

* Скачайте ZeroBundle пакет:
  * [Microsoft Windows](https://github.com/HelloKomputerNet/KomputerNet-win/archive/dist/KomputerNet-win.zip)
  * [Apple macOS](https://github.com/HelloKomputerNet/KomputerNet-mac/archive/dist/KomputerNet-mac.zip)
  * [Linux 64-bit](https://github.com/HelloKomputerNet/ZeroBundle/raw/master/dist/ZeroBundle-linux64.tar.gz)
  * [Linux 32-bit](https://github.com/HelloKomputerNet/ZeroBundle/raw/master/dist/ZeroBundle-linux32.tar.gz)
* Распакуйте где угодно
* Запустите `KomputerNet.exe` (win), `KomputerNet(.app)` (osx), `KomputerNet.sh` (linux)

### Linux терминал

* `wget https://github.com/HelloKomputerNet/ZeroBundle/raw/master/dist/ZeroBundle-linux64.tar.gz`
* `tar xvpfz ZeroBundle-linux64.tar.gz`
* `cd ZeroBundle`
* Запустите с помощью `./KomputerNet.sh`

Он загружает последнюю версию KomputerNet, затем запускает её автоматически.

#### Ручная установка для Debian Linux

* `sudo apt-get update`
* `sudo apt-get install msgpack-python python-gevent`
* `wget https://github.com/HelloKomputerNet/KomputerNet/archive/master.tar.gz`
* `tar xvpfz master.tar.gz`
* `cd KomputerNet-master`
* Запустите с помощью `python2 komputernet.py`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

### [Arch Linux](https://www.archlinux.org)

* `git clone https://aur.archlinux.org/komputernet.git`
* `cd komputernet`
* `makepkg -srci`
* `systemctl start komputernet`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

Смотрите [ArchWiki](https://wiki.archlinux.org)'s [KomputerNet
article](https://wiki.archlinux.org/index.php/KomputerNet) для дальнейшей помощи.

### [Gentoo Linux](https://www.gentoo.org)

* [`layman -a raiagent`](https://github.com/leycec/raiagent)
* `echo '>=net-vpn/komputernet-0.5.4' >> /etc/portage/package.accept_keywords`
* *(Опционально)* Включить поддержку Tor: `echo 'net-vpn/komputernet tor' >>
  /etc/portage/package.use`
* `emerge komputernet`
* `rc-service komputernet start`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

Смотрите `/usr/share/doc/komputernet-*/README.gentoo.bz2` для дальнейшей помощи.

### [FreeBSD](https://www.freebsd.org/)

* `pkg install komputernet` or `cd /usr/ports/security/komputernet/ && make install clean`
* `sysrc komputernet_enable="YES"`
* `service komputernet start`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

### [Vagrant](https://www.vagrantup.com/)

* `vagrant up`
* Подключитесь к VM с помощью `vagrant ssh`
* `cd /vagrant`
* Запустите `python2 komputernet.py --ui_ip 0.0.0.0`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

### [Docker](https://www.docker.com/)
* `docker run -d -v <local_data_folder>:/root/data -p 15441:15441 -p 127.0.0.1:43110:43110 nofish/komputernet`
* Это изображение Docker включает в себя прокси-сервер Tor, который по умолчанию отключён.
  Остерегайтесь что некоторые хостинг-провайдеры могут не позволить вам запускать Tor на своих серверах.
  Если вы хотите включить его,установите переменную среды `ENABLE_TOR` в` true` (по умолчанию: `false`) Например:

 `docker run -d -e "ENABLE_TOR=true" -v <local_data_folder>:/root/data -p 15441:15441 -p 127.0.0.1:43110:43110 nofish/komputernet`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

### [Virtualenv](https://virtualenv.readthedocs.org/en/latest/)

* `virtualenv env`
* `source env/bin/activate`
* `pip install msgpack gevent`
* `python2 komputernet.py`
* Откройте http://127.0.0.1:43110/ в вашем браузере.

## Текущие ограничения

* ~~Нет torrent-похожего файла разделения для поддержки больших файлов~~ (поддержка больших файлов добавлена)
* ~~Не анонимнее чем Bittorrent~~ (добавлена встроенная поддержка Tor)
* Файловые транзакции не сжаты ~~ или незашифрованы еще ~~ (добавлено шифрование TLS)
* Нет приватных сайтов


## Как я могу создать сайт в Komputernet?

Завершите работу komputernet, если он запущен

```bash
$ komputernet.py siteCreate
...
- Site private key (Приватный ключ сайта): 23DKQpzxhbVBrAtvLEc2uvk7DZweh4qL3fn3jpM3LgHDczMK2TtYUq
- Site address (Адрес сайта): 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2
...
- Site created! (Сайт создан)
$ komputernet.py
...
```

Поздравляем, вы закончили! Теперь каждый может получить доступ к вашему зайту используя
`http://localhost:43110/13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2`

Следующие шаги: [KomputerNet Developer Documentation](https://komputernet.io/docs/site_development/getting_started/)


## Как я могу модифицировать Komputernet сайт?

* Измените файлы расположенные в data/13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2 директории.
  Когда закончите с изменением:

```bash
$ komputernet.py siteSign 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2
- Signing site (Подпись сайта): 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2...
Private key (Приватный ключ) (input hidden):
```

* Введите секретный ключ, который вы получили при создании сайта, потом:

```bash
$ komputernet.py sitePublish 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2
...
Site:13DNDk..bhC2 Publishing to 3/10 peers...
Site:13DNDk..bhC2 Successfuly published to 3 peers
- Serving files....
```

* Вот и всё! Вы успешно подписали и опубликовали свои изменения.


## Поддержите проект

- Bitcoin: 1QDhxQ6PraUZa21ET5fYUCPgdrwBomnFgX
- Paypal: https://komputernet.io/docs/help_komputernet/donate/

### Спонсоры

* Улучшенная совместимость с MacOS / Safari стала возможной благодаря [BrowserStack.com](https://www.browserstack.com)

#### Спасибо!

* Больше информации, помощь, журнал изменений, komputernet сайты: https://www.reddit.com/r/komputernet/
* Приходите, пообщайтесь с нами: [#komputernet @ FreeNode](https://kiwiirc.com/client/irc.freenode.net/komputernet) или на [gitter](https://gitter.im/HelloKomputerNet/KomputerNet)
* Email: hello@komputernet.io (PGP: CB9613AE)
