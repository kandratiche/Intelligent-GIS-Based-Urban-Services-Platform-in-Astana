"""Generates the editable SVG wireframes (open in Inkscape, draw.io, Figma). Run: python3 make_wireframes.py"""
import os
W,H=1000,620
OUT=os.path.join(os.path.dirname(__file__))
def esc(s): return s.replace("&","&amp;").replace("<","&lt;")
class S:
    def __init__(s,title): s.e=[]; s.title=title
    def rect(s,x,y,w,h,fill="#fff",stroke="#222",r=4,sw=1.5,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.e.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def text(s,x,y,t,size=13,bold=False,fill="#111",anchor="start"):
        s.e.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{"700" if bold else "400"}" fill="{fill}" text-anchor="{anchor}">{esc(t)}</text>')
    def line(s,x1,y1,x2,y2,stroke="#999",sw=2,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.e.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def circ(s,x,y,r,fill="#fff",stroke="#222"):
        s.e.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    def button(s,x,y,w,h,t,primary=True):
        s.rect(x,y,w,h,"#222" if primary else "#fff","#222",4)
        s.text(x+w/2,y+h/2+5,t,13,True,"#fff" if primary else "#222","middle")
    def field(s,x,y,w,label,val="",h=30):
        s.text(x,y-5,label,12,False,"#444"); s.rect(x,y,w,h,"#fff","#777",3,1.2); s.text(x+8,y+h/2+5,val,12,False,"#666")
    def frame(s,active):
        s.rect(0,0,W,H,"#f4f4f4","#222",0,2)
        s.rect(0,0,W,46,"#fff","#222",0,1.5)
        s.text(16,29,"Urban Services Platform – Astana",16,True)
        for i,t in enumerate(["Parking","Hazards","Lost & found","Staff map"]):
            x=380+i*128; on=(t==active)
            s.rect(x,9,118,28,"#222" if on else "#fff","#222",14); s.text(x+59,28,t,12,True,"#fff" if on else "#222","middle")
        s.text(W-12,29,"User ▾",12,False,"#333","end")
    def map(s,x,y,w,h,pins=(),zones=()):
        s.rect(x,y,w,h,"#e8ecef","#777",2,1.5)
        s.e.append(f'<path d="M{x+w*0.35},{y} C{x+w*0.45},{y+h*0.3} {x+w*0.25},{y+h*0.6} {x+w*0.4},{y+h}" stroke="#bcd" stroke-width="16" fill="none"/>')
        for i in range(1,6): s.line(x,y+h*i/6,x+w,y+h*(i/6+0.02*(i%2)),"#cfd4d8",3)
        for i in range(1,7): s.line(x+w*i/7,y,x+w*(i/7-0.02),y+h,"#cfd4d8",3)
        for (zx,zy,zw,zh,lab) in zones:
            s.rect(x+zx,y+zy,zw,zh,"#f3d9d6","#b3261e",6,1.5,"6 4"); s.text(x+zx+6,y+zy+16,lab,11,False,"#7a1b15")
        for (px,py,lab) in pins:
            s.rect(x+px-26,y+py-12,52,24,"#fff","#222",12,1.5); s.text(x+px,y+py+5,lab,12,True,"#111","middle")
        s.text(x+8,y+h-8,"map (OpenStreetMap) – wireframe, mock data",10,False,"#777")
    def save(s,name):
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Arial, sans-serif"><title>{esc(s.title)}</title>'+"".join(s.e)+'</svg>'
        open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(svg)

# 1 parking map
s=S("Parking map and availability"); s.frame("Parking")
s.map(16,60,590,544,pins=[(120,120,"P 34/80"),(300,260,"P 5/60"),(190,430,"P 0/120"),(450,170,"P 22/40")])
s.rect(620,60,364,544,"#fff"); s.text(634,86,"Parking zones",15,True)
s.field(634,108,336,"Search zone or address","Search…"); 
y=170
for n,a,b,c in [("Zone A (synthetic data)","34 free of 80","30 min: ~28 free","free"),("Zone B (synthetic data)","5 free of 60","30 min: ~2 free","filling"),("Zone C (synthetic data)","0 free of 120","30 min: ~4 free","full")]:
    s.rect(634,y,336,92,"#fff","#555",6); s.text(646,y+22,n,13,True); s.text(646,y+42,a,13); s.text(646,y+60,b+"  (forecast)",12,False,"#444"); s.text(646,y+80,"Updated 11:00",11,False,"#666")
    s.rect(900,y+10,60,20,"#ddd","#555",10); s.text(930,y+25,c,11,False,"#111","middle")
    s.button(836,y+50,124,30,"Reserve",c!="full"); y+=104
s.text(634,y+10,"Forecast = model output, not a guarantee",11,False,"#555")
s.save("01-parking-map")
# 2 reservation
s=S("Reservation form"); s.frame("Parking")
s.map(16,60,420,544,pins=[(200,200,"P 34/80")])
s.rect(450,60,534,544,"#fff"); s.text(470,92,"Reserve a place – Zone A",17,True)
s.field(470,130,230,"Date","2026-11-05"); s.field(720,130,230,"Vehicle (optional)","")
s.field(470,196,230,"From","09:00"); s.field(720,196,230,"To","11:00")
s.rect(470,254,480,92,"#f4f4f4","#888",6); s.text(484,278,"Availability for the chosen slot: 12 places",13,True); s.text(484,298,"Forecast at start time: ~10 places",12,False,"#444"); s.text(484,318,"Reservation is held 15 min after start (no-show rule, to be confirmed)",11,False,"#555")
s.rect(470,366,480,70,"#fff","#888",6,1.2,"5 4"); s.text(484,390,"If the zone is full: alternative zones are suggested",12); s.text(484,412,"Zone D – 22 free  |  Zone E – 9 free",12,False,"#444")
s.button(470,470,180,38,"Confirm reservation"); s.button(666,470,100,38,"Cancel",False)
s.text(470,540,"Reservation is saved in a database transaction (no overbooking).",11,False,"#555")
s.save("02-reservation")
# 3 hazard report
s=S("Hazard report form"); s.frame("Hazards")
s.map(16,60,470,544,pins=[(230,260,"●")],zones=[(60,70,150,90,"icy zone (demo)")])
s.rect(500,60,484,544,"#fff"); s.text(520,92,"Report a hazard",17,True)
s.rect(520,112,200,110,"#eee","#777",4,1.5,"6 4"); s.text(620,172,"Photo (no faces / plates)",12,False,"#555","middle")
s.field(740,130,224,"Location","Tap on map (GPS)"); s.field(740,186,224,"Language","Auto: RU")
s.text(520,252,"Description",12,False,"#444"); s.rect(520,258,444,86,"#fff","#777",3,1.2); s.text(530,280,"Large pothole near the crossing…",12,False,"#666")
s.rect(520,362,444,70,"#f4f4f4","#888",6); s.text(534,386,"Suggested category (AI): Road damage – 86 %",13,True); s.text(534,408,"You can change it:  Road damage ▾",12,False,"#444")
s.button(520,452,150,38,"Submit report"); s.text(520,520,"After submission: status New → In review → Resolved/Rejected",11,False,"#555")
s.text(520,540,"My reports:  #112 Road damage – In review   |   #109 Lighting – Resolved",11,False,"#555")
s.save("03-hazard-report")
# 4 lost and found
s=S("Lost and found search"); s.frame("Lost & found")
s.rect(16,60,968,544,"#fff"); s.text(36,90,"Lost and found",17,True)
s.button(790,70,90,30,"I lost",True); s.button(890,70,84,30,"I found",False)
s.field(36,126,200,"Category","Bag ▾"); s.field(252,126,200,"Area","Left bank ▾"); s.field(468,126,200,"Date range","last 7 days"); s.button(690,126,110,30,"Search")
s.text(36,200,"Top-5 candidate matches for your item (photo + text + location)",13,True)
x=36
for i,(sc,t) in enumerate([("0.91","Black backpack"),("0.84","Dark bag"),("0.77","Gray backpack"),("0.69","Black bag"),("0.61","Sports bag")]):
    s.rect(x,216,180,260,"#fff","#555",6); s.rect(x+10,226,160,110,"#eee","#999",4,1,"5 4"); s.text(x+90,286,"photo",12,False,"#777","middle")
    s.text(x+10,358,t,13,True); s.text(x+10,378,f"match score {sc}",12); s.text(x+10,398,"Found 2026-11-0%d, Left bank"%(i+1),11,False,"#555"); s.button(x+10,420,160,30,"Contact via platform",i==0); x+=190
s.text(36,510,"Contact details are not public; the platform passes messages. Owner and finder confirm or reject a match.",11,False,"#555")
s.save("04-lost-and-found")
# 5 staff map
s=S("Decision-support map for city staff"); s.frame("Staff map")
s.map(16,60,560,544,pins=[(120,140,"12"),(330,230,"27"),(200,400,"8"),(450,120,"5")],zones=[(250,170,170,120,"dense reports (heat)")])
s.rect(590,60,394,544,"#fff"); s.text(606,86,"Layers",14,True)
for i,t in enumerate(["Hazard reports","Parking zones","Lost & found items"]): s.rect(606,98+i*26,16,16,"#222","#222",2); s.text(630,111+i*26,t,12)
s.field(606,196,176,"Category","All ▾"); s.field(796,196,176,"Status","New ▾")
s.text(606,262,"Reports by category (open)",13,True)
for i,(n,v) in enumerate([("Road damage",70),("Lighting",44),("Waste",36),("Snow and ice",58),("Other",16)]):
    s.text(606,288+i*24,n,11); s.rect(700,277+i*24,v*2,14,"#777","#444",2,1)
s.text(606,420,"Parking load (now / +30 min)",13,True)
for i,(n,a,b) in enumerate([("Zone B","92 %","97 %"),("Zone C","100 %","96 %"),("Zone A","58 %","65 %")]): s.text(606,446+i*24,f"{n}:  {a}  →  {b}",12)
s.rect(606,530,364,56,"#f4f4f4","#888",6); s.text(618,552,"Report #112 – Road damage (AI 86 %)",12,True); s.button(796,556,66,24,"Confirm",True); s.button(868,556,92,24,"Change",False)
s.save("05-staff-map")
