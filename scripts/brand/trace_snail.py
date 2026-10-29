import sys
# 확정판 그림에서 선의 가운데와 굵기를 재서 깨끗한 SVG 로 다시 그린다.
import cv2, numpy as np, json
from collections import deque
im=cv2.imread(sys.argv[1] if len(sys.argv)>1 else 'brand/source/snail-master.jpg')[:,:,::-1].astype(int); R,G,B=im[...,0],im[...,1],im[...,2]
H,W=R.shape
red=((R>140)&(G<110)&(B<110))
ink=((R+G+B<260)&~red&~((G>170)&(R<130)&(B<130)))
green=(G>170)&(R<130)&(B<130)
CX,CY,RR=592.8,532.4,259.5
yy,xx=np.mgrid[0:H,0:W]; dist_c=np.hypot(xx-CX,yy-CY); disk=dist_c<=RR+3

def thin(mask):
    img=mask.astype(np.uint8).copy()
    def nb(a):
        p=np.pad(a,1); return [p[:-2,1:-1],p[:-2,2:],p[1:-1,2:],p[2:,2:],p[2:,1:-1],p[2:,:-2],p[1:-1,:-2],p[:-2,:-2]]
    changed=True
    while changed:
        changed=False
        for step in (0,1):
            P=nb(img); Bc=sum(P); seq=P+[P[0]]
            A=sum(((seq[i]==0)&(seq[i+1]==1)).astype(np.uint8) for i in range(8))
            if step==0: c=(P[0]*P[2]*P[4]==0)&(P[2]*P[4]*P[6]==0)
            else: c=(P[0]*P[2]*P[6]==0)&(P[0]*P[4]*P[6]==0)
            rm=(img==1)&(Bc>=2)&(Bc<=6)&(A==1)&c
            if rm.any(): img[rm]=0; changed=True
    return img.astype(bool)

def longest_path(sk):
    ys,xs=np.nonzero(sk); S=set(zip(ys.tolist(),xs.tolist()))
    def nbrs(p):
        y,x=p
        for dy in(-1,0,1):
            for dx in(-1,0,1):
                if (dy or dx) and (y+dy,x+dx) in S: yield (y+dy,x+dx)
    def bfs(s):
        prev={s:None}; q=deque([s]); last=s
        while q:
            u=q.popleft(); last=u
            for v in nbrs(u):
                if v not in prev: prev[v]=u; q.append(v)
        return last,prev
    a,_=bfs(next(iter(S))); b,prev=bfs(a)
    path=[]; u=b
    while u is not None: path.append(u); u=prev[u]
    return [(x,y) for y,x in path]

def resample(pts,step):
    pts=np.array(pts,float); d=np.r_[0,np.cumsum(np.hypot(*np.diff(pts,axis=0).T))]
    s=np.arange(0,d[-1],step); return np.stack([np.interp(s,d,pts[:,0]),np.interp(s,d,pts[:,1])],1)

def smooth(a,k=5):
    if len(a)<k: return a
    ker=np.ones(k)/k; pad=k//2
    return np.stack([np.convolve(np.pad(a[:,i],pad,mode='edge'),ker,'valid') for i in range(a.shape[1])],1)

def catmull(pts,closed=False):
    P=list(map(tuple,pts)); n=len(P)
    d=f"M{P[0][0]:.1f} {P[0][1]:.1f}"
    rng=range(n) if closed else range(n-1)
    for i in rng:
        p0=P[(i-1)%n] if (closed or i>0) else P[i]; p1=P[i]; p2=P[(i+1)%n]
        p3=P[(i+2)%n] if (closed or i+2<n) else p2
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6); c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d+(" Z" if closed else "")

def stroke_path(mask, step=6, k=5):
    sk=thin(mask); pts=longest_path(sk); dt=cv2.distanceTransform(mask.astype(np.uint8),cv2.DIST_L2,5)
    p=resample(pts,step); p=smooth(p,k)
    w=np.array([2*dt[min(H-1,int(round(y))),min(W-1,int(round(x)))] for x,y in p]); w=smooth(w[:,None],7)[:,0]
    return p,w

def brush_polygon(p,w):
    t=np.gradient(p,axis=0); t/=np.linalg.norm(t,axis=1,keepdims=True)+1e-9; n=np.stack([-t[:,1],t[:,0]],1)
    w=w.copy(); m=len(w); tap=max(3,m//40)
    w[:tap]*=np.linspace(.35,1,tap); w[-tap:]*=np.linspace(1,.2,tap)
    L=p+n*(w[:,None]/2); Rr=p-n*(w[:,None]/2)
    poly=np.vstack([L,Rr[::-1]]); return catmull(poly[::2] if len(poly)>400 else poly,closed=True)

out={}
# 1. 껍데기 나선
nR,labR,stR,_=cv2.connectedComponentsWithStats(red.astype(np.uint8),8)
order=sorted(range(1,nR),key=lambda i:-stR[i,4])[:3]
comps=[i for i in order if stR[i,1]<790]
trail_id=[i for i in order if stR[i,1]>=790][0]
strokes=[]
for i in comps:
    p,w=stroke_path(labR==i,step=5,k=5); strokes.append((p,w))
# 안쪽 나선(가운데 끝이 원 중심에 가까운 것)을 먼저, 가운데에서 바깥으로
def cdist(p): return np.hypot(p[0]-CX,p[1]-CY)
strokes.sort(key=lambda pw: min(cdist(pw[0][0]),cdist(pw[0][-1])))
p1,w1=strokes[0]
if cdist(p1[0])>cdist(p1[-1]): p1,w1=p1[::-1],w1[::-1]
p2,w2=strokes[1]
if np.hypot(*(p2[-1]-p1[-1]))<np.hypot(*(p2[0]-p1[-1])): p2,w2=p2[::-1],w2[::-1]
out['shell_brush']=[brush_polygon(p1,w1),brush_polygon(p2,w2)]
out['shell_center']=catmull(np.vstack([p1,p2])[::2])
out['shell_w']=[float(min(w1.min(),w2.min())),float(np.median(np.r_[w1,w2])),float(max(w1.max(),w2.max()))]
out['shell_ends']=[p1[0].tolist(),p1[-1].tolist(),p2[0].tolist(),p2[-1].tolist()]
# 2. 바닥 자국
trail=(labR==trail_id)
# 껍데기 흰 바탕: 빨간 두 획을 크게 닫아 구멍을 채운 모양을 조금 줄인 것
sh=np.isin(labR,comps).astype(np.uint8)
ys_,xs_=np.nonzero(sh); hull=cv2.convexHull(np.stack([xs_,ys_],1).astype(np.int32))
fillm=np.zeros_like(sh); cv2.fillConvexPoly(fillm,hull,1)
fillm=cv2.erode(fillm,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)))
cs3,_=cv2.findContours(fillm,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); fc=max(cs3,key=cv2.contourArea)[:,0,:].astype(float)
fc=smooth(resample(np.vstack([fc,fc[:1]]),10),5); out['shell_fill']=catmull(fc[:-1],closed=True)
tp,tw=stroke_path(trail,step=8,k=5)
if tp[0][0]>tp[-1][0]: tp=tp[::-1]
tp=np.vstack([[818,811],tp]); out['trail']=catmull(tp[::2] if len(tp)>6 else tp); out['trail_w']=float(np.median(tw))
# 3. 몸 윤곽(잉크 선의 가운데)
cut=(yy<478)&(xx<300)
red_d=cv2.dilate(red.astype(np.uint8),np.ones((5,5),np.uint8)).astype(bool)
body_reg=(~green)&(~cut)&(~red_d)
body_reg=body_reg|cv2.erode(fillm,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25))).astype(bool)
n,lab=cv2.connectedComponents(body_reg.astype(np.uint8))
comp=(lab==lab[700,300]).astype(np.uint8)
inkw=float(np.median(2*cv2.distanceTransform(ink.astype(np.uint8),cv2.DIST_L2,5)[thin(ink&(lab==lab[700,300]))])) if False else 7.0
er=cv2.erode(comp,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))
cs,_=cv2.findContours(er,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea)[:,0,:].astype(float)
c=smooth(resample(np.vstack([c,c[:1]]),10),5)
out['body']=catmull(c[:-1],closed=True)
# 4. 얼굴과 더듬이(잉크 덩어리)
nI,labI,st,cen=cv2.connectedComponentsWithStats(ink.astype(np.uint8),8)
face=[]
for i in range(1,nI):
    x,y,ww,hh,a=st[i]
    if a>120 and 170<cen[i][0]<280 and 530<cen[i][1]<590:
        fp,fw=stroke_path(labI==i,step=3,k=3); face.append((catmull(fp),float(np.median(fw))))
out['face']=face
stalk=ink&(yy<500)&(xx<300)&(yy>380)
nS,labS,stS,cenS=cv2.connectedComponentsWithStats(stalk.astype(np.uint8),8)
out['stalk_boxes']=[stS[i].tolist() for i in range(1,nS) if stS[i,4]>40]
json.dump(out,open('brand/source/snail-trace.json','w'))
print('ends',out['shell_ends']);print('shell w',out['shell_w'],'trail w',out['trail_w'],'face',len(face),[f[1] for f in face],'stalks',out['stalk_boxes'])
