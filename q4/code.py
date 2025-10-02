import numpy as np

def P(W,H,n,f,fx,fy,ox,oy,shx=0.0):
    M = np.zeros((4,4), float)
    M[0,0] = 2*fx/W
    M[0,1] = 2*shx/W
    M[0,2] = (W-2*ox)/W
    M[1,1] = 2*fy/H
    M[1,2] = (-H+2*oy)/H
    M[2,2] = -(f+n)/(f-n)
    M[2,3] = -(2*f*n)/(f-n)
    M[3,2] = -1.0
    return M

def uv(pc, M, W, H):
    x,y,z = pc
    c = M @ np.array([x,y,z,1.0])
    ndc = c[:3] / c[3]
    u = 0.5*(ndc[0]+1)*W
    v = 0.5*(ndc[1]+1)*H
    return ndc, (u,v)

def fval(prompt, default):
    s = input(f"{prompt} [{default}]: ").strip()
    return float(s) if s else default


W  = fval("W", 640)
H  = fval("H", 480)
n  = fval("near", 0.1)
f  = fval("far", 10.0)
fx = fval("fx", 650.0)
fy = fval("fy", 650.0)
ox = fval("ox", fx/2)
oy = fval("oy", fy/2)
shx = fval("shx", 0.0)
X = fval("X", 0.2)
Y = fval("Y", -0.2)
Z = fval("Z", -9.0)

M = P(W,H,n,f,fx,fy,ox,oy,shx)
ndc,(u,v) = uv((X,Y,Z), M, W, H)

print("P=\n", M)
print("ndc=", ndc)
print("uv=", (u,v))
