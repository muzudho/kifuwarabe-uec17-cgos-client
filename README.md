# きふわらべ　第１７回ＵＥＣ杯コンピュータ囲碁大会　対局サーバー・クライアント

対局サーバーの種類： CGOS  

📖 [ブログ](https://note.com/muzudho/n/n63589e046b87)  

* ドキュメント（むずでょブランチ）
    * 📖 [ドキュメント（むずでょブランチ）](./docs/README.md)
    * 📖 [gogui](./docs/go-gui.md)

* ドキュメント（原文）
    * 📖 [Python CGOS Client（原文）](./cgos-client-python-v1.1.0/README.md)
    * 📖 [Python CGOS Client - Get Started（原文）](./cgos-client-python-v1.1.0/docs/README.md)
    * 📖 [Python CGOS Client - 貢献者（原文）](./cgos-client-python-v1.1.0/docs/contributors.md)
    * 📖 [Python CGOS Client - 更新履歴（原文）](./cgos-client-python-v1.1.0/docs/changes.md)


## 不具合

* [ ] FIXME: 対局が終わると、ログが溢れる不具合が起こる？  
コマンドラインが、また叩かれる？ ログが重なる？  
`INFO: Starting GTP engine, command line: C:\Users\muzud\OneDrive\ドキュメント\Tools\kifuwarabe-uec17-golang-from-uec13\kifuwarabe-uec17-from-uec13.exe`  

EngineConnector.connect() がまた呼ばれる？  
接続してるのに、また接続したらダメなのでは？  

`cgosclient.py > _handle_gameover() 482` で `pickNewEngine()` するから再接続するのでは？  
何か［設定ファイル］に設定されたエンジンをローテーションしている？ `_currentEngineIndex`  
