# Click4Coin
get free coin with auto click on ads


# usage

first click on links and start bots

[Litecoin](https://t.me/Litecoin_click_bot?start=um7i) <br>
[Zcash](https://t.me/Zcash_click_bot?start=vASSD) <br>
[Dogecoin](https://t.me/Dogecoin_click_bot?start=PpMg) <br>
[BCH](https://t.me/BCH_clickbot?start=BYAkZ) <br>
[Bitcoin](https://t.me/BitcoinClick_bot?start=RBEp) <br>


# Install and run
$ pkg update && pkg upgrade <br>
$ pkg install python git unzip curl <br>
$ git clone https://github.com/s3verus/Click4Coin.git <br>
$ cd Click4Coin <br>
$ pip3 install -r requirements.txt <br>

login to telegram with [this link](https://my.telegram.org/auth) and get your api_id and api_hash <br>
edit main.py and replace your api_id and api_hash in lines 7 and 8 <br>
save file and run codes with : <br>

$ python3 main.py <br>


# notes

$ after run main.py, enter your phone number with country code like : +1858... <br>
$ after enter number, enter telegram login code <br>
$ if you enable two-step verification, please enter your password <br>


# logout

you can logout with this command: <br>
$ python3 main.py logout <br>


# use in behind a Proxy

If Telegram is blocked in your country, you can use the script using the following command: <br>

$ python3 main.py -mt <br><br>

first edit mtproxy.txt file and add your mtproto in first line with this style:<br>
server, port, secret <br>

MTProxy secret must be a hex-string representing 16 bytes <br>


# unlimited mode

for running script for a long time without stop, you can run with -ul like following command: <br>

$ python3 main.py -ul <br><br>

or when you using proxy: <br>

$ python3 main.py -mt -ul <br>

