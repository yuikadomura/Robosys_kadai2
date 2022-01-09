# Robosys_kadai2

# ロボットシステム学2021年度課題1

このプログラムは上田隆一先生が担当する2021年ロボットシステム学の課題2で作成したものである. 


講義動画[1]内で上田先生が作成したプログラムを参考にして, 自分で内容を考えプログラミングを行った. 




## ●プログラムの概要

Publisher側で取得したUNIX timeをSubscriberに送信するプログラム.

配信と受信の際のrate( 周波数 )を変更して, 受信したUNIX timeと1つ前で受信したUNIX timeの差分を比較するために作成した.


### ●rospy.Publisher(getUnix.py)


UNIX timeを取得してrospy.Subscriber(diffTime.py)にトピックとして配信する.


### ●rospy.Subscriber(diffTime.py)


diffTime.pyは以下の処理を行う.


1:受信したUNIX timeに対してdatetimeを使用し, 年月日時分秒ミリ秒に変換する.


2:今回受信したUNIX timeと前回受信したUNIX timeの差分を計算する.


3:受信したUNIX timeと1のdatetimeで変換した文字列, 2で計算した差分を結合した文字列を作成.


4:3で作製した文字列をトピックとして配信する.



## ●考察

rateをそれぞれ10Hz, 100Hz, 1000Hzにして差分を比較する. 


### 結果

　【rate】　　     【差分】

  　10Hz　　       1/10秒(0.1秒)

  　100Hz　　     1/100秒(0.01秒)
　

  　1000Hz　　   1/1000秒(0.001秒)


rateを10倍にすると, 差分は1/10倍になった.


## ●動作環境

・Rasberry Pi 4


・Os : Ubuntu 20.04.3 server


・使用言語 : python3


・ROS1




## ●使用したもの


・Rasberry Pi 4





## ●使用方法



### 【ワークスペースの準備】

####  ・ディレクトリを作成する

$ cd

$ mkdir -p catkin_ws/src

$ cd ~/catkin_ws/src

$ catkin_init_workspace 




####  ・.bashrcの下から3行目に以下を記述する

source ~/catkin_ws/devel/setup.bash




####  ・環境をビルドする

$ cd ~/catkin_ws


$ catkin_make


$ source ~/.bashrc





### 【パッケージの作成とインストール】

####  ・作成するパッケージ名と使用するライブラリを指定する

$ cd ~/catkin_ws/src


####  ・インストール

$ git clone https://github.com/yuikadomura/Robosys_kadai2.git 


$ cd cd ~/catkin_ws


$ catkin_make





### 【実行】


$ chmod +x ~/catkin_ws/src/Robosys_kadai2/scripts/getUnix.py


$ chmod +x ~/catkin_ws/src/Robosys_kadai2/scripts/diffTime.py





####  ・以下の3つのコマンドはそれぞれ別のubuntuで実行する


$ roscore


$ rosrun Robosys_kadai2 getUnix.py


$ rosrun Robosys_kadai2 diffTime.py


$ rostopic echo /diffTime



### 【終了】


※実行していたものはctrl+Cで停止


####  ・Rasberry Pi4の停止


$ sudo poweroff






## ●実行時の動画

Youtubeのリンクは[こちら](https://t.co/htlBEjwEVI)



## ●ライセンス


Robosys_kadai2は[こちらのライセンス](https://www.gnu.org/licenses/)に基づいている.



## ●参考


[1] [第10回講義動画](https://youtu.be/PL85Pw_zQH0)



①Readme の書き方について[こちらのサイト](https://style.potepan.com/articles/33682.html#GitHubREADME-3)


②[上田隆一先生](https://github.com/ryuichiueda)の[講義動画3](https://ryuichiueda.github.io/robosys2020/lesson3_git.html#/)と[講義動画10](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/7)のスライド


を非常に参考にさせていただいたため感謝しています.
