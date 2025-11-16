# my-telnet

telnet は平文での通信。  
my-telnet は telnet の接続部分を書いたスクリプト。  


## 手順１

この手順１は、既に終わっていれば読み飛ばしてください。  

VSCode を開いてください。  
PowerShell ではなく、 Command Prompt を開いてください。  

```shell
pip install telnetlib3
```


## 手順２

```shell
cd my-telnet

# 対局サーバー CGOS にログイン
python -m my_telnet --host {IPアドレス} --port {ポート番号}

        接続成功！ {IPアドレス} に接続中（ローカルエコーオン）。コマンド入力（quitで終了）：
        応答: protocol genmove_analyze

# なんだか分からないが e1 と入力：
e1

        応答: username

# ユーザー名に admin と入力：
admin

        応答: password

# パスワードに admin と入力：
admin

        応答: ok
```

コンピューター囲碁エンジンをサーバーにログインさせておいてください。  

```shell
# 対局サーバーにログインしているエンジン名を一覧します：

        # ［ログインしているエンジン名］、［状態］、［数字］、［持ち時間（秒）］、［数字］の一覧のようだ：
        応答: gnugo1 waiting 0 1800.0 200.0
        45 protocol 0 1800.0 200.0
        63 protocol 0 1800.0 200.0
        Kifuwarabe waiting 0 1800.0 200.0

# 対局開始。match {プレイヤー１} {プレイヤー２} {プレイヤー１の持ち時間（秒）} {プレイヤー２の持ち時間（秒）} のようだ：
match Kifuwarabe gnugo1 1800 1800

        応答: info Next round will start soon: 15:02
        info Next round will start soon: 15:04
```


```shell
# サーバーからログアウトするとき
quit
```
