def poly6 (time, tEnd, xStart, xEnd, xDepth) :

    tStart = 0.0;
    dxStart = 0.0;
    ddxStart = 0.0;
    dxEnd = 0.0;
    ddxEnd = 0.0;
    dt = 0.004;


    Ts = tEnd - tStart;
    if time > Ts*3 :
        time = 0
    if time > Ts*2 :
        time = time - Ts
    if time > Ts :
        time = time - Ts
        
    Rt = time - tStart;

    n0 = xStart;
    n1 = dxStart;
    n2 =  ddxStart/2;
    n3 =  -(((5*ddxStart)/2 + ddxEnd/2)*Ts**2 + (16*dxStart - 6*dxEnd)*Ts + 42*xStart + 22*xEnd - 64*xDepth)/Ts**3;
    n4 = (((9*ddxStart)/2 + 2*ddxEnd)*Ts**2 + (38*dxStart - 23*dxEnd)*Ts + 111*xStart + 81*xEnd - 192*xDepth)/Ts**4;
    n5 = -(((7*ddxStart)/2 + (5*ddxEnd)/2)*Ts**2 + (33*dxStart - 27*dxEnd)*Ts + 102*xStart + 90*xEnd - 192*xDepth)/Ts**5;
    n6 = ((ddxStart + ddxEnd)*Ts**2 + (10*dxStart - 10*dxEnd)*Ts + 32*xStart + 32*xEnd - 64*xDepth)/Ts**6

     
    if time < (tStart - dt*0.25) :
        Pos = xStart
	Vel = dxStart
	Acc = ddxStart
    elif time > (tEnd - dt*0.25) :
	Pos = xEnd
	Vel = dxEnd
	Acc = ddxEnd
    else :
	Pos = n0 + Rt*(n1 + Rt*(n2 + Rt*(n3 + Rt*(n4 + Rt*(n5 + Rt*n6)))))
	Vel = n1 + Rt*(2*n2 + Rt*(3*n3 + Rt*(4*n4 + Rt*(5*n5 + Rt*6*n6))))
	Acc = 2*n2 + Rt*(6*n3 + Rt*(12*n4 + Rt*(20*n5 + Rt*30*n6)))

    return Pos
