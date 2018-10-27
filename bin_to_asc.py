import os
import sys

def main():
  argv = sys.argv
  argc = len(argv)

  if (argc < 1):
    # 引数の個数チェック
    print('Usage: python %s target_file' %argv[0] )
    quit()
  else:
    if not os.path.exists(argv[1]):
      print('%s not found.' %argv[1])
      quit()

  filename = argv[1]

  # ファイルをオープンする
  loadData = open(filename, "r")

  # 行ごとにすべて読み込んでリストデータにする
  lines = loadData.readlines()

  # ファイルをクローズする
  loadData.close()

  for line in lines:
    line.strip()
    data = int(line,2)
    # print("%d --> %s" %(data, chr(data)), end="")
    print("%s" %(chr(data)), end="")


if __name__ == "__main__":
  main()
