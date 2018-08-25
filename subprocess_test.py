import subprocess

command = "irasutoya 虎"                  #！ここに実行したいコマンドを書く！
proc = subprocess.Popen(
    command,
    shell  = True,                            #シェル経由($ sh -c "command")で実行。
    stdin  = subprocess.PIPE,                 #1
    stdout = subprocess.PIPE,                 #2
    stderr = subprocess.PIPE)                 #3

stdout_data, stderr_data = proc.communicate() #処理実行を待つ(†1)
print(stdout_data)  #標準出力の確認