def prime1(N:int) -> list:
  """総当たりで素数を探索する関数
  Args:
    N (int): 計測する自然数
  Returns:
    primes (list): 素数の配列
    num (int): 処理の合計数
  """
  primes = []       # return用のリスト初期化
  isPrime = False   # 素数判定用初期化
  d = 2             # while判定用の初期化
  num = 0           # 処理計測用変数の初期化
  # for文と同じ(dが2からNになるまでループする)
  while d <= N:
    isPrime = True  # 素数であると仮定する
    t = 2           # while判定用の初期化
    # for文と同じ(tがdになるまでループする)
    while t < d:
      # d mod t が0の時は割り切れる数なので素数ではない
      if d % t  == 0:
        isPrime = False
      # ループ用の加算
      t += 1
      num += 1
    # 上記while文で素数という判定の場合、返却用リストに追加する。
    if isPrime == True:
      primes.append(d)
    # ループ用の加算
    d += 1
  return primes,num

if __name__=="__main__":
  p,n = prime1(20)
  print(f"素数：{p}\r\n処理：{n}回")