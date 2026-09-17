#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh phiên bản HTML dễ đọc cho toàn bộ 20 bộ đề TOEIC (Set_001 – Set_020).

- Mỗi bộ -> 1 file HTML tự chứa (inline CSS/JS) trong  Toeic_exam_paper/html/Set_XXX.html
  gồm 4 tab: Listening · Reading · Đáp án (che, bấm mới hiện) · Ghi chú
- Trang mục lục:  Toeic_exam_paper/html/index.html

Chạy lại bất cứ lúc nào:  python3 Toeic_exam_paper/build_html.py
"""
import os
import re
import html
import datetime
import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "html")

THEMES = {
    "001": "Office hỗn hợp", "002": "Travel & Hospitality", "003": "Finance & Banking",
    "004": "Manufacturing & Logistics", "005": "HR, Recruitment & Training",
    "006": "Marketing & Advertising", "007": "Technology & IT", "008": "Retail & Customer Service",
    "009": "Real Estate & Facilities", "010": "Health & Medicine", "011": "Environment & Science",
    "012": "Media & Publishing", "013": "Legal & Contracts", "014": "Education & Training",
    "015": "Food Service & Restaurants", "016": "Construction & Development",
    "017": "Energy & Utilities", "018": "Nonprofit & NGO", "019": "Government & Public Services",
    "020": "Ôn tổng (mixed final mock)",
}

TABS = [
    ("listening.md", "listening", "🎧 Listening"),
    ("reading.md", "reading", "📖 Reading"),
    ("answer_key.md", "key", "🗝️ Đáp án"),
    ("notes.md", "notes", "📝 Ghi chú"),
]

# ---- chuyển markdown -> html (giữ chỗ trống điền tay) --------------------------

def md_to_html(text: str) -> str:
    # blank Part 6:  ---81---  ->  (81)
    text = re.sub(r"-{2,3}(\d{2,3})-{2,3}", lambda m: f"\x00BN{m.group(1)}\x00", text)
    # blank Part 5:  -------    ->  ________
    text = re.sub(r"-{5,}", "\x00BD\x00", text)
    # ô điền tay:  ___________  hoặc  __/6
    text = re.sub(r"_{2,}", "\x00FILL\x00", text)

    md = markdown.Markdown(
        extensions=["tables", "sane_lists", "nl2br", "fenced_code", "attr_list"]
    )
    out = md.convert(text)

    out = out.replace("\x00BD\x00", '<span class="blk">________</span>')
    out = re.sub(r"\x00BN(\d{2,3})\x00", r'<span class="blk">(\1)</span>', out)
    out = out.replace("\x00FILL\x00", '<span class="fill"></span>')
    return out


# ---- template ---------------------------------------------------------------

PAGE = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
<noscript><style>
.tabs{{display:none}} .panel{{display:block !important}}
.keybody{{display:block !important}} .gate{{display:none}}
</style></noscript>
</head>
<body data-set="{num}">
<header class="top">
  <div class="bar">
    <a class="home" href="index.html">☰ Mục lục</a>
    <strong class="tt">SET_{num}</strong>
    <span class="theme">{theme}</span>
    <span class="spacer"></span>
    <button class="ib" id="fdn" title="Chữ nhỏ">A-</button>
    <button class="ib" id="fup" title="Chữ to">A+</button>
    <button class="ib" id="thm" title="Sáng/Tối">◐</button>
  </div>
  <nav class="tabs">
    {tabbtns}
  </nav>
</header>
<main>
  {panels}
</main>
<button id="toTop" title="Lên đầu">↑</button>
<script>{js}</script>
</body>
</html>
"""

INDEX = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TOEIC 600+ — 20 bộ đề (HTML)</title>
<style>{css}</style>
</head>
<body class="idx">
<header class="top"><div class="bar">
  <strong class="tt">TOEIC 600+ L&amp;R</strong>
  <span class="theme">20 bộ đề đầy đủ · 3.000 câu</span>
  <span class="spacer"></span>
  <button class="ib" id="thm" title="Sáng/Tối">◐</button>
</div></header>
<main class="wrap">
  <p class="lead">Mỗi bộ = Listening 50 câu + Reading 100 câu + đáp án cân bằng A/B/C/D + ghi chú.
  Không có audio (bản quyền ETS) — phần Listening là script + câu hỏi để luyện đọc-hiểu Part 3/4 và logic Part 2.</p>
  <div class="grid">
    {cards}
  </div>
  <p class="foot">Sinh tự động từ các file <code>.md</code> — {stamp}. Chạy lại: <code>python3 Toeic_exam_paper/build_html.py</code></p>
</main>
<script>{js}</script>
</body>
</html>
"""

CARD = """<a class="card" href="Set_{num}.html">
  <span class="cn">SET_{num}</span>
  <span class="ct">{theme}</span>
  <span class="cm">L50 · R100 · key · notes</span>
</a>"""

CSS = r"""
:root{
  --bg:#fbfaf7; --fg:#1f2328; --mut:#5b6570; --line:#e6e2d9; --card:#ffffff;
  --accent:#8a5a2b; --accent-bg:#f3ead d; --blk:#c9762e; --sel:#fff2d9;
  --fs:17px;
}
:root.dark{
  --bg:#15171a; --fg:#e6e6e3; --mut:#9aa2ab; --line:#2c2f34; --card:#1d2024;
  --accent:#d9a066; --accent-bg:#2a2318; --blk:#e0a35b; --sel:#33291a;
}
@media (prefers-color-scheme:dark){
  :root:not(.light){
    --bg:#15171a; --fg:#e6e6e3; --mut:#9aa2ab; --line:#2c2f34; --card:#1d2024;
    --accent:#d9a066; --accent-bg:#2a2318; --blk:#e0a35b; --sel:#33291a;
  }
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font:var(--fs)/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
.top{position:sticky; top:0; z-index:20; background:var(--bg); border-bottom:1px solid var(--line)}
.bar{display:flex; align-items:center; gap:10px; padding:8px 12px; max-width:860px; margin:0 auto; flex-wrap:wrap}
.home{color:var(--accent); text-decoration:none; font-size:.82em; white-space:nowrap}
.tt{font-size:.95em; letter-spacing:.5px}
.theme{color:var(--mut); font-size:.8em}
.spacer{flex:1}
.ib{border:1px solid var(--line); background:var(--card); color:var(--fg); border-radius:8px;
  padding:3px 9px; font-size:.8em; cursor:pointer; line-height:1.4}
.ib:active{transform:translateY(1px)}
.tabs{display:flex; gap:4px; padding:0 8px 8px; max-width:860px; margin:0 auto; overflow-x:auto}
.tabbtn{flex:1; min-width:max-content; border:1px solid var(--line); background:var(--card); color:var(--mut);
  border-radius:9px; padding:7px 12px; font-size:.86em; cursor:pointer; white-space:nowrap}
.tabbtn.on{background:var(--accent-bg); color:var(--accent); border-color:var(--accent); font-weight:600}
main{max-width:860px; margin:0 auto; padding:18px 16px 120px}
.panel{display:none}
.panel.on{display:block; animation:fade .18s ease}
@keyframes fade{from{opacity:.3}to{opacity:1}}

h1,h2,h3{line-height:1.3; margin:1.5em 0 .5em}
h1{font-size:1.35em; border-bottom:2px solid var(--line); padding-bottom:.25em}
h2{font-size:1.15em; color:var(--accent); border-bottom:1px solid var(--line); padding-bottom:.2em}
h3{font-size:1em; color:var(--mut); text-transform:none}
p{margin:.55em 0}
blockquote{margin:.8em 0; padding:.5em .9em; background:var(--accent-bg); border-left:3px solid var(--accent);
  border-radius:0 8px 8px 0; color:var(--mut); font-size:.92em}
blockquote p{margin:.25em 0}
hr{border:0; border-top:1px solid var(--line); margin:1.6em 0}
code{background:var(--accent-bg); padding:.05em .35em; border-radius:5px; font-size:.88em}
pre{background:var(--card); border:1px solid var(--line); border-radius:10px; padding:12px 14px; overflow-x:auto}
pre code{background:none; padding:0}
strong{color:var(--fg)}
em{color:var(--mut)}
a{color:var(--accent)}

/* câu hỏi + đáp án nằm sát dòng (nl2br) */
main p{ }
.blk{color:var(--blk); font-weight:700; letter-spacing:1px}
.fill{display:inline-block; min-width:70px; border-bottom:1.5px solid var(--mut); margin:0 2px}

table{border-collapse:collapse; width:100%; margin:.9em 0; font-size:.9em; display:block; overflow-x:auto}
th,td{border:1px solid var(--line); padding:5px 9px; text-align:left}
th{background:var(--accent-bg); color:var(--accent)}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--card) 55%, var(--bg))}

/* gate đáp án */
.gate{text-align:center; padding:38px 16px}
.gate button{background:var(--accent); color:#fff; border:0; border-radius:10px; padding:12px 22px;
  font-size:1em; cursor:pointer}
.gate p{color:var(--mut); font-size:.9em; margin-top:14px}
.keybody{display:none}
.keybody.show{display:block}

#toTop{position:fixed; right:14px; bottom:16px; z-index:30; width:42px; height:42px; border-radius:50%;
  border:1px solid var(--line); background:var(--card); color:var(--fg); font-size:1.1em; cursor:pointer;
  opacity:0; pointer-events:none; transition:opacity .2s}
#toTop.show{opacity:.92; pointer-events:auto}

/* index */
.idx .wrap{max-width:860px; margin:0 auto; padding:22px 16px 80px}
.lead{color:var(--mut); font-size:.92em}
.grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); gap:12px; margin-top:18px}
.card{display:flex; flex-direction:column; gap:3px; padding:14px 15px; background:var(--card);
  border:1px solid var(--line); border-radius:12px; text-decoration:none; color:var(--fg)}
.card:hover{border-color:var(--accent)}
.cn{font-weight:700; letter-spacing:.5px; color:var(--accent)}
.ct{font-size:.95em}
.cm{font-size:.75em; color:var(--mut)}
.foot{margin-top:26px; color:var(--mut); font-size:.8em}

@media print{
  /* ép về nền sáng bất kể prefers-color-scheme của trình in */
  :root, :root.dark, :root:not(.light){
    --bg:#ffffff; --fg:#1a1a1a; --mut:#3d444c; --line:#d9d4c8; --card:#ffffff;
    --accent:#7a4a1f; --accent-bg:#f5efe4; --blk:#b5641f; --sel:#fff2d9;
  }
  body{background:#fff; color:#1a1a1a}
  .top,#toTop{display:none}
  .panel{display:block !important; opacity:1 !important; animation:none !important}
  .keybody{display:block !important}
  .gate{display:none}
  main{max-width:none; padding:0}
  h2,h3{break-after:avoid}
  p,tr,blockquote,pre{break-inside:avoid}
}
"""

JS = r"""
(function(){
  var root=document.documentElement, LS=window.localStorage;
  try{
    var t=LS.getItem('toeic-theme');
    if(t==='dark') root.classList.add('dark');
    if(t==='light') root.classList.add('light');
    var f=parseInt(LS.getItem('toeic-fs')||'0',10);
    if(f) root.style.setProperty('--fs',(17+f)+'px');
  }catch(e){}
  function bind(id,fn){var el=document.getElementById(id); if(el) el.addEventListener('click',fn);}
  bind('thm',function(){
    var d=root.classList.toggle('dark'); root.classList.remove('light');
    if(!d) root.classList.add('light');
    try{LS.setItem('toeic-theme', d?'dark':'light');}catch(e){}
  });
  var fs=parseInt((LS&&LS.getItem('toeic-fs'))||'0',10)||0;
  function setfs(){root.style.setProperty('--fs',(17+fs)+'px'); try{LS.setItem('toeic-fs',fs);}catch(e){}}
  bind('fup',function(){if(fs<8){fs++;setfs();}});
  bind('fdn',function(){if(fs>-4){fs--;setfs();}});

  // tabs
  var btns=document.querySelectorAll('.tabbtn'), pans=document.querySelectorAll('.panel');
  function show(name){
    btns.forEach(function(b){b.classList.toggle('on', b.dataset.tab===name);});
    pans.forEach(function(p){p.classList.toggle('on', p.dataset.tab===name);});
    try{LS.setItem('toeic-tab-'+document.body.dataset.set, name);}catch(e){}
    window.scrollTo(0,0);
  }
  btns.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.tab);});});
  if(btns.length){
    var saved=null; try{saved=LS.getItem('toeic-tab-'+document.body.dataset.set);}catch(e){}
    show(saved && document.querySelector('.tabbtn[data-tab="'+saved+'"]') ? saved : btns[0].dataset.tab);
  }

  // answer gate
  var g=document.getElementById('gatebtn');
  if(g) g.addEventListener('click',function(){
    document.querySelector('.keybody').classList.add('show');
    g.closest('.gate').style.display='none';
  });

  // to top
  var tt=document.getElementById('toTop');
  if(tt){
    tt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
    window.addEventListener('scroll',function(){tt.classList.toggle('show', window.scrollY>600);});
  }
})();
"""


def build_set(num: str) -> None:
    sd = os.path.join(BASE, f"Set_{num}")
    tabbtns, panels = [], []
    first = True
    for fname, key, label in TABS:
        fp = os.path.join(sd, fname)
        if not os.path.exists(fp):
            continue
        with open(fp, encoding="utf-8") as fh:
            body = md_to_html(fh.read())
        on = " on" if first else ""
        tabbtns.append(f'<button class="tabbtn{on}" data-tab="{key}">{label}</button>')
        if key == "key":
            panel_inner = (
                '<div class="gate"><button id="gatebtn">🗝️ Bấm để hiện đáp án</button>'
                '<p>Chỉ mở sau khi đã làm xong cả Listening và Reading.</p></div>'
                f'<div class="keybody">{body}</div>'
            )
        else:
            panel_inner = body
        panels.append(f'<section class="panel{on}" data-tab="{key}">{panel_inner}</section>')
        first = False

    page = PAGE.format(
        title=f"SET_{num} — {THEMES[num]}",
        num=num,
        theme=html.escape(THEMES[num]),
        tabbtns="\n    ".join(tabbtns),
        panels="\n  ".join(panels),
        css=CSS,
        js=JS,
    )
    with open(os.path.join(OUT, f"Set_{num}.html"), "w", encoding="utf-8") as fh:
        fh.write(page)


def build_index() -> None:
    cards = "\n    ".join(
        CARD.format(num=n, theme=html.escape(THEMES[n])) for n in sorted(THEMES)
    )
    page = INDEX.format(
        css=CSS, js=JS, cards=cards,
        stamp=datetime.date.today().isoformat(),
    )
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    for n in sorted(THEMES):
        if os.path.isdir(os.path.join(BASE, f"Set_{n}")):
            build_set(n)
            print(f"  Set_{n}.html")
    build_index()
    print(f"  index.html\nXong -> {OUT}")


if __name__ == "__main__":
    main()
