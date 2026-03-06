import math

def psnr(original,modified):

    N=len(original)

    mse=0

    for i in range(N):
        for j in range(N):

            diff=original[i][j]-modified[i][j]
            mse+=diff*diff

    mse=mse/(N*N)

    if mse==0:
        return float('inf')

    return 10*math.log10((255*255)/mse)