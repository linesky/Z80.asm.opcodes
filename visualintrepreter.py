code=""
optcode=""
last=0
ttrue=True
files=input("file data name? ")
try:
    f1=open(files,"r")
    optcode=f1.read()
    f1.close()
except:
    aa=0
sp=[]
spsp=""
tt=0
ttt=0
optc=optcode.split("\n")
for ooo in range(len(optc)):
    lines=optc[ooo]
    lines=lines.strip()
    if lines=="":
        ttrue=False
    else:
        ssp=lines.split("|")
        if len(ssp)>1:
            tt=ssp[1].find("0x0")
            
                
        spsp=""
        spa=ssp[0]
        sp=[]
        for k in range(0,len(ssp[0]),2):
            
            spsp=spsp+spa[k:k+2]
            if k<len(ssp[0])-2:
                spsp=spsp+","
    sp=spsp.split(",")
    s1=""
    
    m=0
    if len(sp)>0:
        for c in range(len(sp)):
            sp1=[]
            n1=c
            sp1=sp[:n1+1]
            s1=",".join(sp1)
            
            s2="    "*(c+1)
            ss2="    "*(c+2)
            s1=s2+"#"+s1+"\n"
            s4=s1+s2+"if value==0x"+sp[c]+":\n"+ss2
            n4=len(s4)
            nn=code.find(s1)
            if tt>0:
               if len(sp)>2:
                   if sp[len(sp)-2]=="00":
                       ttt=len(sp)-3
                   else:
                       ttt=len(sp)-2
            else:
                ttt=len(sp)-1

            
            
            if nn<0 and c<=ttt:
                
                s3=code[:m]
                
                
                s3=s3+s4
                if c==ttt:
                    s3=s3+"print(\""+ssp[1]+"\")\n"
                s3=s3+code[m:]
                code=s3
                m=m+n4
            else:
                if c<=ttt:
                    m=nn+n4+1
            
        
try:
    f1=open(files+".dat","w")
    f1.write(code)
    f1.close()
except:
    print("error on write file")
   


 