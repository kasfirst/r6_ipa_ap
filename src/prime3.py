def prime3(N:int) -> list:
  """prime2に、さらに2の倍数を除いて素数を探索する関数
  Args:
    N (int): 計測する自然数
  Returns:
    primes (list): 素数の配列
    num (int): 処理の合計数
  """
  primes = [2]             # return用のリスト初期化
  isPrime = [] # 素数判定用初期化
  c = 3
  d = 3             # while判定用の初期化
  num = 0           # 処理計測用変数の初期化
  # isPrime配列にN分Trueを挿入する。
  while c <= N:
    isPrime.append(True)
    c += 2
  # for文と同じ(dが2からNになるまでループする)
  while d <= N:
    # isPrimeがFalseの時は素数ではないのでスキップ
    if isPrime[int((d -1)/2)-1] == True:
      primes.append(d)  # 素数の追加
      t = d * d         # tに素数の二乗を代入
      while t <= N:
        # 素数判定用配列にFalseを追加
        isPrime[int((t-1)/2)-1] = False
        t = t + 2*d
        num += 1
    # ループ用の加算
    d += 2
  return primes,num

if __name__=="__main__":
  p,n = prime3(20)
  print(f"素数：{p}\r\n処理：{n}回")