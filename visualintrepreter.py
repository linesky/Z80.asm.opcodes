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
optc=optcode.split("\n")
for ooo in range(len(optc)):
    lines=optc[ooo]
    lines=lines.strip()
    if lines=="":
        ttrue=False
    else:
        ssp=lines.split("|")
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
            s4=s1+s2+"if value==0x"+sp[c]+":\n"+ss2+"print(\""+ssp[1]+"\")\n"
            n4=len(s4)
            nn=code.find(s1)
            if nn<0:
                
                s3=code[:m]
                
                
                s3=s3+s4
                s3=s3+code[m:]
                code=s3
                m=m+n4
            else:
                m=nn+n4+1

        
try:
    f1=open(files+".dat","w")
    f1.write(code)
    f1.close()
except:
    print("error on write file")
   


 