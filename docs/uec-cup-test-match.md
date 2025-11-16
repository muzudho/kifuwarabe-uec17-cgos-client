# UEC杯テスト対局


## 手順１

**NOTE:** この操作はせずに、Pythonでつないだ方がいいかも。  

Windows のスタート・ボタンの横の検索ボックスに `control` と打鍵。  
［コントロール パネル］をクリック。  
［プログラム　＞　Windows の機能の有効化または無効化］をクリック。  
［Telnet Client］チェックボックスをチェック。  
［OK］ボタンをクリック。  
インストールが始まるのでしばらく待つ。  
［閉じる］ボタンをクリック。  

VSCode のターミナルを開く。  
PowerShell ではなく Command Prompt を開く。  
以下のコマンドを打鍵。  

```shell
telnet {IPアドレス} {ポート番号}
```

ここで、以下のようなメッセージが表示されると、エラーが起きているので、方法を変える必要がある。  

```plaintext
protocol genmove_analyze
```

その場合、 Python で telnet プログラムを書く。  
