from chaotic_maps import ChaoticMaps

class Watermarking:

    def __init__(self, k=75):
        self.k = k
        self.maps = ChaoticMaps()


    def embed(self,host,watermark):

        print("Embedding watermark...")

        I_scr = self.maps.arnold_cat_map(host,self.k)

        chaotic_mask = self.maps.chaotic_pattern((len(watermark),len(watermark[0])))

        W_scr = [[watermark[i][j]^chaotic_mask[i][j]
                 for j in range(len(watermark[0]))]
                 for i in range(len(watermark))]

        N=len(I_scr)
        I_scr_mod=[[0]*N for _ in range(N)]

        for i in range(N):
            for j in range(N):

                I_scr_mod[i][j]=(I_scr[i][j]&254)|W_scr[i][j]

        T=self.maps.get_period(N)

        watermarked=self.maps.arnold_cat_map(I_scr_mod,T-self.k)

        return watermarked


    def extract(self,watermarked,original_watermark):

        print("Extracting watermark...")

        IW_scr=self.maps.arnold_cat_map(watermarked,self.k)

        N=len(IW_scr)

        lsb=[[IW_scr[i][j]&1 for j in range(N)] for i in range(N)]

        chaotic_mask=self.maps.chaotic_pattern((N,N))

        recovered=[[lsb[i][j]^chaotic_mask[i][j] for j in range(N)] for i in range(N)]

        diff=[[abs(recovered[i][j]-original_watermark[i][j]) for j in range(N)] for i in range(N)]

        T=self.maps.get_period(N)

        tamper_map=self.maps.arnold_cat_map(diff,T-self.k)

        return recovered,tamper_map