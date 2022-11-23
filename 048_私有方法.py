class Dog(object):
    def __send_msg(self):
        print('有权发送消息')

    def send_msg(self, new_money):
        if new_money > 10:
            self.__send_msg()
        else:
            print('请充值')


dog = Dog()
dog.send_msg(20)
dog.send_msg(0)
