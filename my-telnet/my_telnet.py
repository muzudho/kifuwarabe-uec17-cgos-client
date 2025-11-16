import asyncio
import telnetlib3
import argparse

async def telnet_example(host, port, connect_timeout=10.0):
    try:
        # open_connectionをwait_forでラップしてタイムアウト
        reader, writer = await asyncio.wait_for(
            telnetlib3.open_connection(host, port, connect_minwait=2.0, connect_maxwait=3.0),
            timeout=connect_timeout
        )
        
        # コマンド送信（例: 'ls'。サーバー依存で変えろ）
        writer.write('ls\n'.encode('utf-8'))
        await writer.drain()
        
        # 応答読む（これもタイムアウト付き）
        data = await asyncio.wait_for(reader.read(1024), timeout=5.0)
        print(data.decode('utf-8'))
        
    except asyncio.TimeoutError:
        print(f'接続タイムアウト！ {connect_timeout}秒経過')
    except Exception as e:
        print(f'エラー: {e}')
    finally:
        if 'writer' in locals():
            writer.close()
            await writer.wait_closed()


def main():
    # コマンドライン引数解析
    parser = argparse.ArgumentParser(description='Telnet接続ツール（telnetlib3版）')
    parser.add_argument('--host', type=str, default='localhost', help='接続ホスト（デフォ: localhost）')
    parser.add_argument('--port', type=int, default=23, help='接続ポート（デフォ: 23）')
    parser.add_argument('--timeout', type=float, default=10.0, help='接続タイムアウト（秒、デフォ: 10.0）')
    
    args = parser.parse_args()
    
    # 実行
    asyncio.run(telnet_example(args.host, args.port, args.timeout))


if __name__ == '__main__':
    main()
