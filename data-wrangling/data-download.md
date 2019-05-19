python上でunixコマンドを実行する
https://qiita.com/tdrk/items/9b23ad6a58ac4032bb3b

osモジュールを使った os.system やcommandsモジュールを使った commands.getstatusoutput がありましたが、現在は推奨されていないようです。

```
import subprocess
args = ['ls', '-l', '-a']
try:
    res = subprocess.check_call(args)
except:
    print "Error."
```

