import asyncio
import telnetlib3
from telnetlib3.telopt import ECHO  # ECHOオプション (1)
import argparse


class CustomTelnetClient(telnetlib3.TelnetClient):
    """WILL ECHOを拒否してローカルエコー強制オン"""


    async def handle_will(self, cmd, opt):
        if opt == ECHO:  # WILL ECHO拒否
            await self.send_iac(telnetlib3.IAC, telnetlib3.DONT, opt)
            self.log.debug('Echo交渉拒否: ローカルエコー維持！')
        else:
            await super().handle_will(cmd, opt)


async def telnet_example(host, port, connect_timeout=10.0, read_timeout=5.0):
    try:
        # client_factoryでカスタムクライアント指定
        reader, writer = await asyncio.wait_for(
            telnetlib3.open_connection(
                host,
                port,
                client_factory=CustomTelnetClient,  # ここがキー！
                connect_minwait=2.0,
                connect_maxwait=3.0
            ),
            timeout=connect_timeout
        )
        print(f'接続成功！ {host}:{port} に接続中（ローカルエコーオン）。コマンド入力（quitで終了）：')
        
        while True:
            # 同期input()でコマンド取得
            cmd = input("telnet> ").strip()
            if cmd.lower() in ('quit', 'exit', 'q'):
                print('接続終了中...')
                break
            
            # コマンド送信
            writer.write(cmd + '\n')
            await writer.drain()
            
            # 応答読む（タイムアウト付き）
            data = await asyncio.wait_for(reader.read(1024), timeout=read_timeout)
            print('応答:', data)
            
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
    parser = argparse.ArgumentParser(description='インタラクティブTelnet接続ツール（エコーオン固定版）')
    parser.add_argument('--host', type=str, default='localhost', help='接続ホスト（デフォ: localhost）')
    parser.add_argument('--port', type=int, default=23, help='接続ポート（デフォ: 23）')
    parser.add_argument('--timeout', type=float, default=10.0, help='接続タイムアウト（秒、デフォ: 10.0）')
    parser.add_argument('--read-timeout', type=float, default=5.0, help='読取タイムアウト（秒、デフォ: 5.0）')
    
    args = parser.parse_args()

    # 実行
    asyncio.run(telnet_example(args.host, args.port, args.timeout, args.read_timeout))


if __name__ == '__main__':
    main()
