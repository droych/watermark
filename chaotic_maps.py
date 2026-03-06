class ChaoticMaps:

    def __init__(self, a=1, b=1, mu=3.854, x0=0.654):
        self.a = a
        self.b = b
        self.mu = mu
        self.x0 = x0
        self._period_cache = {}

    def arnold_cat_map(self, image, iterations):

        N = len(image)
        result = [row[:] for row in image]

        for _ in range(iterations):

            temp = [[0 for _ in range(N)] for _ in range(N)]

            for x in range(N):
                for y in range(N):

                    new_x = (x + self.a*y) % N
                    new_y = (self.b*x + (self.a*self.b+1)*y) % N

                    temp[new_x][new_y] = result[x][y]

            result = temp

        return result


    def get_period(self, N):

        if N in self._period_cache:
            return self._period_cache[N]

        test = [[i*N+j for j in range(N)] for i in range(N)]
        original = [row[:] for row in test]

        for t in range(1,500):

            test = self.arnold_cat_map(test,1)

            if test == original:
                self._period_cache[N] = t
                return t

        self._period_cache[N] = 96
        return 96


    def logistic_map(self,length):

        x = self.x0
        seq = []

        for _ in range(length):
            x = self.mu*x*(1-x)
            seq.append(x)

        return seq


    def chaotic_pattern(self,shape):

        rows,cols = shape
        seq = self.logistic_map(rows*cols)

        binary = [1 if s>0.5 else 0 for s in seq]

        matrix = []
        idx = 0

        for i in range(rows):
            row=[]
            for j in range(cols):
                row.append(binary[idx])
                idx+=1
            matrix.append(row)

        return matrix