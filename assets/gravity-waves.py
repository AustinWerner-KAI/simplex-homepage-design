"""Hero background for index.html: gravitational waves from two black holes spiralling together.
Run from the repo root:  python3 assets/gravity-waves.py [highlight strength, default 0.2]
Needs numpy and Pillow. Writes assets/gravity-waves.webp and links it from index.html."""
import numpy as np, base64, io, sys
from PIL import Image, ImageFilter
S=3000
y,x=np.mgrid[0:S,0:S].astype(np.float32)
X=(x-S/2)/S*2; Y=(y-S/2)/S*2
r=np.hypot(X,Y)+1e-6; th=np.arctan2(Y,X)

# ---- inspiral: chirping quadrupole wave, amplitude ~ 1/r, wavelength grows with distance (emitted earlier, slower orbit)
tau0=0.03; tau=tau0+r
Phi=-46.0*tau**(5/8)
amp=tau**(-0.25)/(1+5*r)
env=(1-np.exp(-(r/0.07)**2))
h=0.013*amp*np.cos(2*Phi-2*th)*env
# second, weaker harmonic for realism (higher-order modes)
h+=0.002*amp*np.cos(3*Phi-3*th)*env

# ---- two black holes: funnel-shaped wells (-M/sqrt(d^2+e^2)), on opposite arms
a=0.05; orb=46.0*tau0**(5/8)
for s in (0,np.pi):
    bx,by=a*np.cos(orb+s),a*np.sin(orb+s)
    d=np.hypot(X-bx,Y-by)
    h-=0.0016/np.sqrt(d*d+0.00015)
# central saddle softening so the middle doesn't spike
h-=0.008*np.exp(-(r/0.06)**2)

# ---- spacetime fabric: fine grid displaced by the strain
gy,gx=np.gradient(h)
u=X-gx*45; v=Y-gy*45
sp=0.032
def lines(t): return np.exp(-((np.abs(((t/sp)+.5)%1-.5))/0.045)**2)
gl=np.clip(lines(u)+lines(v),0,1)
h-=0.00022*gl*np.exp(-r/1.1)

# ---- long-wavelength undulation (fabric isn't perfectly flat) + satin grain
rng=np.random.default_rng(3)
def noise(n,amp):
    z=rng.standard_normal((n,n)).astype(np.float32)
    return np.asarray(Image.fromarray(z).resize((S,S),Image.BICUBIC))*amp
h+=noise(6,0.006)+noise(24,0.0015)+noise(S//3,0.00003)

# ---- shading
Z=S*0.7
gy,gx=np.gradient(h*Z)
N=np.dstack([-gx,-gy,np.ones_like(h)]); N/=np.linalg.norm(N,axis=2,keepdims=True)
def unit(v): v=np.array(v,np.float32); return v/np.linalg.norm(v)
V=unit([0,0,1])
key=unit([-0.55,-0.7,0.45])      # cool key light, top-left
rim=unit([0.8,0.5,0.25])         # faint warm rim from bottom-right
def blinn(Lv,p):
    H=unit(Lv+V); return np.clip(N@H,0,1)**p - H[2]**p
diff_k=(N@key)-key[2]
diff_r=(N@rim)-rim[2]
spec=np.clip(blinn(key,90),0,1)*1.4+np.clip(blinn(key,14),0,1)*0.5
fres=(1-np.clip(N[...,2],0,1))**3
ao=np.clip(1+h/0.05,0.25,1)      # wells sink into darkness

bg=np.array([5,7,12],np.float32)
cool=np.array([120,180,235],np.float32)
warm=np.array([200,170,150],np.float32)
col=np.zeros((S,S,3),np.float32)+bg
args=[a for a in sys.argv[1:] if not a.startswith('--')]
k=float(args[0]) if args else 0.2
col+=(cool-bg)*np.clip(diff_k*2.2,0,1)[...,None]*k
col+=(cool-bg)*spec[...,None]*k*0.9
col+=(warm-bg)*np.clip(diff_r*1.6,0,1)[...,None]*k*0.25
col+=(cool-bg)*fres[...,None]*k*0.35
col*= (1+np.clip(diff_k*2.2,-1,0)[...,None]*0.9)   # shadow side goes to near-black
col*= ao[...,None]
# very soft bloom on highlights
lum=col.mean(2)
bl=np.asarray(Image.fromarray(np.clip(lum,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(18)),np.float32)
col+= (cool-bg)*np.clip(bl-14,0,255)[...,None]/255*0.35

im=Image.fromarray(np.clip(col,0,255).astype(np.uint8)).resize((2000,2000),Image.LANCZOS)
buf=io.BytesIO(); im.save(buf,'WEBP',quality=66,method=6); data=buf.getvalue()
print(len(data)//1024,'KB'); open('assets/gravity-waves.webp','wb').write(data)
b64=base64.b64encode(data).decode()
# index.html links the file; pass --inline to embed it as base64 (used for the self-contained share page)
src='data:image/webp;base64,'+b64 if '--inline' in sys.argv else 'assets/gravity-waves.webp'
html=open('index.html').read()
css=('.hero{position:relative;isolation:isolate;overflow:hidden}'
 '.hero::before{content:"";position:absolute;z-index:-1;left:62%;top:46%;width:1800px;height:1800px;'
 'transform:translate(-50%,-50%) perspective(950px) rotateX(58deg) rotateZ(-18deg);'
 f'background:url("{src}") center/cover no-repeat;'
 '-webkit-mask-image:radial-gradient(circle at 50% 50%,#000 20%,transparent 58%);mask-image:radial-gradient(circle at 50% 50%,#000 20%,transparent 58%);pointer-events:none}'
 '.hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,var(--bg) 0,var(--bg) 38%,transparent 70%),linear-gradient(180deg,var(--bg) 0,transparent 30%);pointer-events:none}'
 '.hero .node:not(.server){background:rgb(5 7 12/.86)}'
 '@media (max-width:860px){.hero::before{left:62%;top:700px;width:1000px;height:1000px;transform:translate(-50%,-50%) perspective(600px) rotateX(55deg) rotateZ(-18deg);opacity:.85}.hero::after{background:linear-gradient(180deg,var(--bg) 0,var(--bg) 19%,transparent 33%)}}')
import re
marker='/* Hero background:'
if marker in html:
    html=re.sub(re.escape(marker)+r'.*?(?=</style>)',lambda m: marker+' gravitational waves from a binary inspiral, rendered in code (assets/gravity-waves.py). Decorative, no text sits on its brightest area. */'+css,html,count=1,flags=re.S)
else:
    html=html.replace('</style>',css+'</style>',1)
open('index.html','w').write(html)
