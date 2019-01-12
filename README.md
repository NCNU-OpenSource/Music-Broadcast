# Music-Broadcast
bluetooth and discord Music bot
- [Music-Broadcast ppt](https://docs.google.com/presentation/d/1nwv5Nd4ezVqHHSsWhAWOu3u2sVftfk7g9xN1NgFk7Cg/edit?usp=sharing)

# Group 6

# Group member
1. 資工四 104321002 何建宏
2. 資工四 104321003 謝萬霖
3. 資工四 104321024 蔡旻勳

## 前言
- 使用 raspberry pi 連接藍芽播放音樂
- 創造 discord music robot，專門播放音樂 

## 播放藍芽音樂
### 套件下載
<pre><code>
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install bluetooth
sudo apt-get install --no-install-recommends pulseaudio pulseaudio-module-bluetooth
</code></pre>
### 環境設定
 - /etc/systemd/system/pulseaudio.service
<pre><code>
內容:
[Unit]  
Description=Pulse Audio  
  
[Service]  
Type=simple  
ExecStart=/usr/bin/pulseaudio --system --disallow-exit --disable-shm
</code></pre>
 - 執行指令
<pre><code>systemctl daemon-reload</code></pre>
 - /etc/dbus-1/system.d/pulseaudio-bluetooth.conf
<pre><code>
內容:
<!ELEMENT busconfig>
<policy user="pulse">  
<allow send_destination="org.bluez"/>  
</policy>  
</busconfig> 
</code></pre>

 - /etc/pulse/system.pa
 <pre><code>
 添加到檔案最後:
 ### Automatically load driver modules for Bluetooth hardware  
.ifexists module-bluetooth-policy.so  
load-module module-bluetooth-policy  
.endif  
 
.ifexists module-bluetooth-discover.so  
load-module module-bluetooth-discover  
.endif 
</code></pre>
- 設定藍芽
<pre><code>
bluetoothctl
agent on  
default-agent  
scan on  
pair 00:00:00:00:00:00
trust 00:00:00:00:00:00  
connect 00:00:00:00:00:00
</code></pre>
 - 設定藍芽參數
 <pre><code>
 usermod -aG pulse-access,audio root
 usermod -aG pulse-access,audio pi
 pactl set-card-profile 1 a2dp
 </code></pre>
 - 撥放
 <pre><code>aplay 檔案名稱.WAV</code></pre>
## Discord Music Bot
### 事前準備
- [建立 Bot 帳號](https://discordapp.com/developers/applications/)
- 教學 : 參照上方 ppt
### 安裝環境
<pre><code>sudo apt-get update -y</code></pre>
<pre><code>sudo apt-get upgrade -y</code></pre>
<pre><code>sudo apt-get install git libopus-dev libffi-dev libsodium-dev ffmpeg -y</code></pre>
<pre><code>sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl -y</code></pre>
<pre><code>pip install aiohttp</code></pre>
<pre><code>install python3.5+</code></pre>
<pre><code>python3 -m pip install -U youtube_dl</code></pre>
- 視需求安裝不同 discord.py 版本
- '0.16.2'
> <code>sudo python3.5 -m pip install -U discord.py[voice]</code>
- ‘1.0.0a’
> <code>sudo python3.6 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]</code>
- 可透過 <code>discord.__version__</code> 查看
### 程式設定 & 執行
- 進入 configure.txt 設定 Bot's token and prefix command
- 執行 <code>python3.5 music_bot.py</code>
- 進入 discord, 執行 prefix command + "join", 將 bot 加入語音頻道
- prefix command + "play" + url, 播放音樂

## 參考
- [Making a python Bot with discord.py](https://www.youtube.com/playlist?list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9)
- [disocrd.py](https://github.com/Rapptz/discord.py)
- [discord.py’s documentation](https://discordpy.readthedocs.io/en/latest/)

## 分工
- 播放藍芽音樂 : 何建宏
- discord music bot : 蔡旻勳
- 所有網路相關設定 (包含 raspberry pi 本體設定) 與 youtube 抓取音樂 : 謝萬霖

## 影片
- [測試影片](https://www.youtube.com/watch?v=HARYLiyPiIk)
- [Discord Music Bot](https://youtu.be/Ewlr_iKJ3Eo)
