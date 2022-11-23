def get_wendu():
    wendu = 22
    print('摄氏度：%d' % wendu)
    return wendu


def get_huashi():
    wendu = get_wendu() * 1.8 + 32
    print('华氏温度：%d' % wendu)


get_huashi()
