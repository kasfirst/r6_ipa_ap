def prime2(N:int) -> list:
  """2乗を活用して素数を探索する関数
  Args:
    N (int): 計測する自然数
  Returns:
    primes (list): 素数の配列
    num (int): 処理の合計数
  """
  primes = []             # return用のリスト初期化
  isPrime = [False] # 素数判定用初期化
  c = 2
  d = 2             # while判定用の初期化
  num = 0           # 処理計測用変数の初期化
  # isPrime配列にN分Trueを挿入する。
  while c <= N:
    isPrime.append(True)
    c += 1
  # for文と同じ(dが2からNになるまでループする)
  while d <= N:
    # isPrimeがFalseの時は素数ではないのでスキップ
    if isPrime[d -1] == True:
      primes.append(d)  # 素数の追加
      t = d * d         # tに素数の二乗を代入
      while t <= N:
        # 素数判定用配列にFalseを追加
        isPrime[t -1] = False
        t = t + d
        num += 1
    # ループ用の加算
    d += 1
  return primes,num

if __name__=="__main__":
  p,n = prime2(20)
  print(f"素数：{p}\r\n処理：{n}回")