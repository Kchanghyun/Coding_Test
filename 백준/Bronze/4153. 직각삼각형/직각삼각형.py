while True:
    Ausar, Auset, Heru = map(int, input().split()) # 높이, 밑변, 대각..?
    if Ausar == 0 and Auset == 0 and Heru == 0:
        break
    
    Ausar **= 2
    Auset **= 2
    Heru **= 2

    if Heru == Ausar + Auset or Ausar == Heru + Auset or Auset == Heru + Ausar:
        print('right')
    else:
        print('wrong')
