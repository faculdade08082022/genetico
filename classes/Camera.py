class Camera:
    def __init__(self, x, y, a):
        # posicao
        self.x = x
        self.y = y
        # angulo
        self.a = a

    def __repr__(self):
        rt = "Camera(x:"+str(self.x)+",y:"+str(self.y) + \
            ",angulo:"+str(self.a)+")"
        return rt
