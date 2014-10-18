#!/usr/bin/env python
import random
class pointcurve():
''' Using a set of points to estimate the points between them
The points are usually token from CDF

^
|
|
|                  *
|            ?
|       *
|   *     
|  
---------------------------->
'''

    def __init__(self, pointsfile):
        with open(pointsfile) as f:
            pp = f.readlines()
        pp = [ t.replace('\n', '') for t in pp ]
        self.xx = [ float(t.split('\t')[0]) for t in pp ]
        self.yy = [ float(t.split('\t')[1]) for t in pp ]

        self.maxyy = max(self.yy)
        self.minyy = min(self.yy)
        self.lenyy = len(self.yy)

    def theintvlof(self, y):
        '''return the index of the first value in yy that yy <= y. \
    for y <= min(yy), return the index of min(yy); \
    for y >= max(yy), return the index of max(yy)'''
        for i in range(self.lenyy):
            if y > self.yy[i]:
                continue
            else: break
        return i-1

    def ytox(self, y):
        '''convert y to x. y in [0,1]'''
        if y < self.minyy:
            return False
        if y > self.maxyy:
            return False

        l = self.theintvlof(y)
        xinterval = self.xx[l+1] - self.xx[l]
        yinterval = self.yy[l+1] - self.yy[l]
        if xinterval == 0: # vertical line
            ret = self.xx[l]
        elif yinterval == 0: # horizontal line
            ret = random.random() * xinterval + self.xx[l]
        else:
            k = yinterval / xinterval
            ret = (y - self.yy[l])/k + self.xx[l]
        return ret

    def average(self):
    ''' estimate the average x
    Note that (xx, yy) is token from a cdf
    Assume that the value (xx[i]+xx[i+1])/2 has the probability of (yy[i+1]-yy[i])
    '''
	sum = 0
	for i in range(self.lenyy-1):
	    sum += 0.5*(self.xx[i] + self.xx[i+1])*(self.yy[i+1]-self.yy[i])
	return sum

if __name__ == '__main__':
    a = pointcurve('datasize.cdf')
    print(a.ytox(0.5))
