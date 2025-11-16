# telnet

telnet は平文での通信。  


## 手順１

PowerShell ではなく、 Command Prompt を使う。  

```shell
pip install telnetlib3
```


## 手順２

```shell
cd my-telnet

# 対局サーバーにログイン
python -m my_telnet --host {IPアドレス} --port {ポート番号}

e1

admin

admin
```

コンピューター囲碁エンジンをサーバーにログインさせておいてください。  

```shell
# ログインしているエンジン名一覧
who

# 対局開始
match Kifuwarabe gnugo1 1800 1800

# サーバーからログアウトするとき
quit
```
