# Robosys_kadai2

#ロボットシステム学2021年度課題1
このプログラムは上田隆一先生が担当する2021年ロボットシステム学の課題2で作成したものである. 

講義動画[1]内で上田先生が作成したプログラムを参考にして, 自分で内容を考えプログラミングを行った. 


##●プログラムの概要
Rasberry Pi 4を用いて, rospy.Publisher(count.py)から現在の日付時間とマイクロ秒をrospy.Subscriber(twice.py)にトピックとして送り, 画面上に10Hz毎に日付時間マイクロ秒と前回の値との差分を表示するプログラムである.


##●動作環境
・Rasberry Pi 4
・Os : Ubuntu 20.04.3 server
・使用言語 : python3
・ROS noetic


##●使用したもの
・Rasberry Pi 4
・ノートパソコン


##●使用方法

###【Githubから】
###【ワークスペースの準備】
・ディレクトリを作成する
$ cd
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace 

・.bashrcの下から3行目に以下を記述する
source ~/catkin_ws/devel/setup.bash

・環境をビルドする
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc

###【パッケージの作成とインストール】
・作成するパッケージ名と使用するライブラリを指定する
$ cd ~/catkin_ws/src

・インストール
$ git clone https://github.com/yuikadomura/Robosys_kadai2.git 
$ cd cd ~/catkin_ws
$ catkin_make

###【実行】
$ chmod +x ~/catkin_ws/src/Robosys_kadai2/scripts/count.py
$ chmod +x ~/catkin_ws/src/Robosys_kadai2/scripts/twice.py

・以下の3つのコマンドはそれぞれ別のubuntuで実行する
$ roscore
$ rosrun mypkg count.py
$ rosrun mypkg twice.py

###【終了】
※実行していたものはctrl+Cで停止

・Rasberry Pi4の停止
$ sudo poweroff

##●実行時の動画
Youtubeのリンクは[こちら]()

##●ライセンス
Robosys_kadai2は[こちらのライセンス](https://www.gnu.org/licenses/)に基づいている.

##●参考
[1] [第10回講義動画](https://youtu.be/PL85Pw_zQH0)

①Readme の書き方について[こちらのサイト](https://style.potepan.com/articles/33682.html#GitHubREADME-3)
②[上田隆一先生](https://github.com/ryuichiueda)の[講義動画3](https://ryuichiueda.github.io/robosys2020/lesson3_git.html#/)と[講義動画10](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/7)のスライド
を非常に参考にさせていただいたため感謝しています.
