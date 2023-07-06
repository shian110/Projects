
# 実行例
- インスタンスを作成  
  python bin/gen_instance.py instance/gra.csv > test.lp
- clingoで解を求める  
  clingo encoding/encoding.lp test.lp > test.log
- 解をcsv形式にデコード  
  Python bin/TTdecode.py test.log test.csv



## encoding
- 符号化を格納するディレクトリ

## bin
- 実行する際に用いる様々なプログラムを格納するディレクトリ

## instance
- 実際のデータなどのインスタンスファイルを格納するディレクトリ


