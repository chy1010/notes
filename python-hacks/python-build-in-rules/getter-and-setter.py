
class NTD:

    def __init__(self, ntd = 0):
        self.set_ntd(ntd)

    def set_ntd(self, ntd: int = 0):
        self.__ntd = ntd

    def get_ntd(self):
        return self.__ntd
    
    def get_usd(self):
        return (self.get_ntd() * 30)

if __name__ == '__main__':

    wallet = NTD(100)

    try:
        print('try to get ntd in wallet:')
        print(wallet.__ntd)
    except:
        print('fail to get wallet.__ntd')
        print('use method wallet.get_ntd()')
        print(wallet.get_ntd())
    