@echo off

rem 文字化け対策。コマンドプロンプトがデフォルトで Shift-JIS なので、その文字コードを消すことで、UTF-8 にする。
chcp 65001 >nul

echo 全部任せろだぜ（＾～＾）...

rem プロジェクト・ルートで作業する。
cd ..

rem プロジェクト・ルートに 📁 `go-to-championship/cgos-client-gtp` フォルダーを作成。
mkdir go-to-championship\cgos-client-gtp

rem プロジェクト・ルートにある 📁 `cgos-client-python-v1.1.0-muzudho-branch` フォルダーを、さきほど作った 📁 `go-to-championship/cgos-client-gtp` フォルダーにコピーします。
rem     /E サブディレクトリ（空のディレクトリーも含める）コピーするオプション。
rem     /I コピー先がフォルダーの場合に確認しないオプション。
xcopy /E /I cgos-client-python-v1.1.0-muzudho-branch go-to-championship\cgos-client-gtp\cgos-client-python-v1.1.0-muzudho-branch

echo コピー完了！

rem 以下の３行が書かれたテキストファイルを、📁 `go-to-championship\cgos-client-gtp` フォルダーに作成します。
rem ## GTPエンジンを起動し、対局サーバーに接続する方法。
rem cd cgos-client-python-v1.1.0-muzudho-branch\src
rem python cgosclient.py ../kifuwarabe-uec-17.cfg
(
    echo ## GTPエンジンを起動し、対局サーバーに接続する方法。
    echo cd cgos-client-python-v1.1.0-muzudho-branch\src
    echo python cgosclient.py ../kifuwarabe-uec-17.cfg
) > go-to-championship\cgos-client-gtp\readme.txt

pause
