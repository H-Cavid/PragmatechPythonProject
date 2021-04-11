class DRF:
    def __init__(self,*args, **kwargs):
        self.__dict__.update(**kwargs)
        self.model = None
        print(self.__dict__)
    
    

    