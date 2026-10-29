import json,sys
t=json.load(open('brand/source/snail-trace.json'))
INK,RED,WH="#22262E","#D3263A","#FFFFFF"
stalks=[((206,488),(184,418)),((262,486),(261,412))]
def stalk(b,tip):
    (bx,by),(tx,ty)=b,tip
    return f'<path d="M{bx} {by} C{bx-4} {by-28} {tx+2} {ty+30} {tx} {ty+12}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/><circle cx="{tx}" cy="{ty}" r="12" fill="{WH}" stroke="{INK}" stroke-width="6.5"/>'
face=''.join(f'<path d="{d}" stroke="{INK}" stroke-width="{w:.1f}" stroke-linecap="round" stroke-linejoin="round"/>' for d,w in t['face'])
brush=''.join(f'<path d="{d}" fill="{RED}"/>' for d in t['shell_brush'])
shell=f'<g id="shell"><path id="shell-fill" d="{t["shell_fill"]}" fill="{WH}"/><g id="shell-brush">{brush}</g><path id="shell-center" d="{t["shell_center"]}" stroke="none" fill="none"/></g>'
full=(f'<path id="trail" d="{t["trail"]}" stroke="{RED}" stroke-width="{t["trail_w"]:.1f}" stroke-linecap="round"/>'
      '<g id="stalks">'+''.join(stalk(b,tp) for b,tp in stalks)+'</g>'
      f'<path id="body" d="{t["body"]}" fill="{WH}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
      f'<g id="face">{face}</g>'+shell)
def svg(vb,w,h,inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}" fill="none">{inner}</svg>\n'
out=sys.argv[1]
open(out+'/snail.svg','w',encoding='utf-8').write(svg("138 250 900 610",900,610,full))
open(out+'/shell-mark.svg','w',encoding='utf-8').write(svg("326 266 536 536",536,536,shell))
