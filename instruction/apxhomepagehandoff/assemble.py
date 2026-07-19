import base64, pathlib
work = pathlib.Path(__file__).parent; site = work/'site'
body = (work/'apx-root-v9-body.html').read_text()
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()
repl = {
  '{{APX_LOGO}}': b64(site/'assets/images/logos/APX_LOGO.png','image/png'),
  '{{APX_LOGO_WHITE}}': b64(work/'styleguide/apx-design-system/assets/logos/apx-revops-wordmark-white.png','image/png'),
  '{{CL_ZECH}}': b64(work/'logos_norm/zech.png','image/png'),
  '{{CL_EIGENHERD}}': b64(work/'logos_norm/eigenherd.png','image/png'),
  '{{CL_LIQID}}': b64(work/'logos_norm/liqid.png','image/png'),
  '{{CL_EVENTINC}}': b64(work/'logos_norm/eventinc_log.png','image/png'),
  '{{CL_IU}}': b64(work/'logos_norm/iu.png','image/png'),
  '{{CL_HAUSER}}': b64(work/'logos_norm/hauser.png','image/png'),
  '{{PHOTO_ALEX}}': b64(site/'assets/images/people/alex-knoll.webp','image/webp'),
  '{{PH_LEONARD}}': b64(site/'assets/images/people/leonard-falk.webp','image/webp'),
  '{{PH_DORIAN}}': b64(site/'assets/images/people/dorian-mihu.webp','image/webp'),
  '{{PH_ALEXL}}': b64(site/'assets/images/people/alex-lyad.webp','image/webp'),
  '{{PH_SAMUEL}}': b64(site/'assets/images/people/samuel-plesa.webp','image/webp'),
  '{{PH_VIKTOR}}': b64(site/'assets/images/people/viktor-kur.webp','image/webp'),
  '{{PH_SOPHIE}}': b64(site/'assets/images/people/sophie-schwarz.webp','image/webp'),
}
for k,v in repl.items(): body = body.replace(k, v)
tailwind = (site/'assets/css/tailwind.css').read_text()
font_b64 = base64.b64encode((site/'assets/fonts/plus-jakarta-sans.woff2').read_bytes()).decode()
lucide = (site/'assets/js/lucide.min.js').read_text()
supplement = """
.bg-rose-50{background-color:#fff1f2}.text-rose-600{color:#e11d48}
.border-slate-200\\/70{border-color:rgb(226 232 240 / .7)}
.h-44{height:11rem}.w-44{width:11rem}.h-20{height:5rem}.w-20{width:5rem}.h-12{height:3rem}.w-12{width:3rem}
.hover\\:gap-2:hover{gap:.5rem}
.hover\\:text-purple-300:hover{color:#d8b4fe}
.mb-5{margin-bottom:1.25rem}.mb-14{margin-bottom:3.5rem}.pl-5{padding-left:1.25rem}.mt-5{margin-top:1.25rem}.mr-1{margin-right:.25rem}
.pt-28{padding-top:7rem}.py-10{padding-top:2.5rem;padding-bottom:2.5rem}
.text-\\[11px\\]{font-size:11px}
.text-white\\/80{color:rgb(255 255 255 / .8)}
.text-rose-400{color:#fb7185}
.bg-emerald-500\\/15{background-color:rgb(16 185 129 / .15)}
.bg-rose-500\\/15{background-color:rgb(244 63 94 / .15)}
.bg-purple-500\\/15{background-color:rgb(168 85 247 / .15)}
.-ml-3{margin-left:-.75rem}
.first\\:ml-0:first-child{margin-left:0}
.max-w-\\[220px\\]{max-width:220px}
.space-y-5>*+*{margin-top:1.25rem}
.decoration-white\\/40{text-decoration-color:rgb(255 255 255 / .4)}
.hover\\:decoration-white:hover{text-decoration-color:#fff}
.hero-cap{padding-right:0}
@media (min-width:768px){.hero-cap{padding-right:190px}}

@media (min-width:640px){.sm\\:pt-32{padding-top:8rem}.sm\\:p-10{padding:2.5rem}.sm\\:p-14{padding:3.5rem}.sm\\:text-2xl{font-size:1.5rem;line-height:2rem}.sm\\:text-left{text-align:left}}
@media (min-width:768px){.md\\:pt-36{padding-top:9rem}.md\\:p-12{padding:3rem}.md\\:gap-14{gap:3.5rem}.md\\:grid-cols-\\[auto_1fr\\]{grid-template-columns:auto 1fr}.md\\:grid-cols-\\[1\\.2fr_0\\.8fr\\]{grid-template-columns:1.2fr .8fr}.md\\:text-left{text-align:left}}
@media (min-width:1024px){.lg\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}}
"""

supplement += """
.border-b-2{border-bottom-width:2px}
.grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}
.col-span-10{grid-column:span 10/span 10}.col-span-12{grid-column:span 12/span 12}.col-start-3{grid-column-start:3}
.divide-x>*+*{border-left-width:1px;border-right-width:0}
.divide-slate-200>*+*{border-color:#e5e7eb;border-color:rgb(226 232 240)}
.divide-white\/20>*+*{border-color:rgb(255 255 255 / .2)}
.first\:border-t-0:first-child{border-top-width:0}
.gap-14{gap:3.5rem}.gap-x-3{column-gap:.75rem}.gap-y-2{row-gap:.5rem}
.group:hover .group-hover\:bg-purple-500\/30{background-color:rgb(168 85 247 / .3)}
.h-\[28\%\]{height:28%}.h-\[52\%\]{height:52%}.h-\[78\%\]{height:78%}
.leading-\[1\.06\]{line-height:1.06}.leading-\[1\.15\]{line-height:1.15}
.p-7{padding:1.75rem}.pb-10{padding-bottom:2.5rem}.pb-16{padding-bottom:4rem}
.py-14{padding-top:3.5rem;padding-bottom:3.5rem}.py-20{padding-top:5rem;padding-bottom:5rem}
.py-3\.5{padding-top:.875rem;padding-bottom:.875rem}.py-6{padding-top:1.5rem;padding-bottom:1.5rem}
.space-y-7>*+*{margin-top:1.75rem}.w-40{width:10rem}
@media (min-width:640px){
.sm\:flex{display:flex}
.sm\:inline{display:inline}
.sm\:grid{display:grid}
.col-span-1{grid-column:span 1/span 1}
.col-span-2{grid-column:span 2/span 2}
.col-span-3{grid-column:span 3/span 3}
.col-span-6{grid-column:span 6/span 6}
.pb-3{padding-bottom:.75rem}
.sm\:col-span-1{grid-column:span 1/span 1}.sm\:col-span-2{grid-column:span 2/span 2}.sm\:col-span-3{grid-column:span 3/span 3}
.sm\:col-span-6{grid-column:span 6/span 6}.sm\:col-span-7{grid-column:span 7/span 7}.sm\:col-start-auto{grid-column-start:auto}
.sm\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.sm\:p-7{padding:1.75rem}.sm\:text-right{text-align:right}
}
@media (min-width:768px){
.md\:border-t-0{border-top-width:0}.md\:divide-x>*+*{border-left-width:1px;border-right-width:0}
.md\:divide-slate-200>*+*{border-color:rgb(226 232 240)}
.md\:gap-20{gap:5rem}.md\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}
.md\:justify-between{justify-content:space-between}.md\:max-w-md{max-width:28rem}.md\:max-w-sm{max-width:24rem}
.md\:mt-0{margin-top:0}.md\:pb-0{padding-bottom:0}.md\:pb-24{padding-bottom:6rem}
.md\:pl-10{padding-left:2.5rem}.md\:pr-10{padding-right:2.5rem}.md\:pt-0{padding-top:0}
.md\:px-10{padding-left:2.5rem;padding-right:2.5rem}.md\:py-0{padding-top:0;padding-bottom:0}
.md\:py-24{padding-top:6rem;padding-bottom:6rem}.md\:py-28{padding-top:7rem;padding-bottom:7rem}.md\:py-32{padding-top:8rem;padding-bottom:8rem}
}
@media (min-width:1024px){
.lg\:col-span-2{grid-column:span 2/span 2}.lg\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.lg\:row-span-1{grid-row:span 1/span 1}
}
"""

supplement += """
.h-9{height:2.25rem}.h-96{height:24rem}
.justify-start{justify-content:flex-start}
.pt-5{padding-top:1.25rem}
.space-y-1\.5>*+*{margin-top:.375rem}
.sm\:text-lg{font-size:1.125rem;line-height:1.75rem}
@media (min-width:640px){.sm\:p-6{padding:1.5rem}}
@media (min-width:768px){.md\:grid-cols-\[1fr_340px\]{grid-template-columns:1fr 340px}.md\:pb-16{padding-bottom:4rem}.md\:pt-8{padding-top:2rem}}
"""
supplement += """\n.bg-slate-900\\/85{background-color:rgb(15 23 42 / .85)}\n.inset-x-0{left:0;right:0}\n.py-2\\.5{padding-top:.625rem;padding-bottom:.625rem}\n.rounded-b-2xl{border-bottom-left-radius:1rem;border-bottom-right-radius:1rem}\n"""

supplement += """
/* polish pass */
.js .rv{opacity:0;transform:translateY(14px);transition:opacity .6s cubic-bezier(.22,.6,.3,1),transform .6s cubic-bezier(.22,.6,.3,1)}
.js .rv.on{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){.js .rv{opacity:1;transform:none;transition:none}}
.skip-link{position:absolute;left:-9999px;top:0;z-index:100;background:#4A00E0;color:#fff;padding:.6rem 1rem;border-radius:0 0 .5rem 0;font-weight:700}
.skip-link:focus{left:0}
:focus-visible{outline:2px solid #4A00E0;outline-offset:2px;border-radius:2px}
section[id]{scroll-margin-top:88px}
h1,h2{text-wrap:balance}
.text-\\[64px\\]{font-size:64px}
.leading-\\[1\\.05\\]{line-height:1.05}.leading-\\[1\\.08\\]{line-height:1.08}
.border-white\\/15{border-color:rgb(255 255 255 / .15)}
.border-white\\/10{border-color:rgb(255 255 255 / .1)}
.text-white\\/60{color:rgb(255 255 255 / .6)}
.bg-purple-50\\/60{background-color:rgb(250 245 255 / .6)}
.w-0\\.5{width:.125rem}
.h-5{height:1.25rem}
.-mr-2{margin-right:-.5rem}
.-mt-2{margin-top:-.5rem}
.pt-14{padding-top:3.5rem}.pb-8{padding-bottom:2rem}
.opacity-70{opacity:.7}
.tracking-wider{letter-spacing:.05em}
.duration-300{transition-duration:300ms}
.border-sky-200{border-color:#bae6fd}.bg-sky-50{background-color:#f0f9ff}.text-sky-700{color:#0369a1}
.border-amber-200{border-color:#fde68a}.bg-amber-50{background-color:#fffbeb}.text-amber-700{color:#b45309}
.border-purple-200{border-color:#e9d5ff}.text-purple-700{color:#7e22ce}
.border-rose-200{border-color:#fecdd3}.text-rose-700{color:#be123c}
.bg-rose-400{background-color:#fb7185}
.text-slate-100{color:#f1f5f9}
.hover\\:-translate-y-1:hover{transform:translateY(-.25rem)}
.hover\\:shadow-xl:hover{box-shadow:0 20px 25px -5px rgb(0 0 0 / .1),0 8px 10px -6px rgb(0 0 0 / .1)}
.hover\\:shadow-slate-200\\/70:hover{box-shadow:0 20px 25px -5px rgb(226 232 240 / .7),0 8px 10px -6px rgb(226 232 240 / .5)}
.hover\\:border-slate-300:hover{border-color:#cbd5e1}
.hover\\:opacity-90:hover{opacity:.9}
.transition-opacity{transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:150ms}
.py-3\\.5{padding-top:.875rem;padding-bottom:.875rem}
.gap-y-2{row-gap:.5rem}
@media (min-width:640px){.sm\\:hidden{display:none}.sm\\:block{display:block}.sm\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.sm\\:gap-16{gap:4rem}.sm\\:items-baseline{align-items:baseline}.sm\\:justify-between{justify-content:space-between}.sm\\:flex-row{flex-direction:row}}
@media (min-width:768px){.md\\:hidden{display:none}.md\\:block{display:block}.md\\:items-start{align-items:flex-start}.md\\:mt-2{margin-top:.5rem}.md\\:py-28{padding-top:7rem;padding-bottom:7rem}}
@media (min-width:768px){.md\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}}
.-right-8{right:-2rem}
.pt-12{padding-top:3rem}
@media (min-width:768px){.md\\:inline{display:inline}}
.top-\\[60px\\]{top:60px}
.divide-y>*+*{border-top-width:1px;border-bottom-width:0}
.divide-slate-200>:not(:last-child){border-color:rgb(226 232 240)}
.divide-y>:not(:last-child){border-bottom-width:0}
.gap-1\\.5{gap:.375rem}
.overflow-auto{overflow:auto}
@media (min-width:640px){.sm\\:justify-items-end{justify-items:end}.sm\\:p-8{padding:2rem}}
.border-purple-300{border-color:#d8b4fe}
.pt-3{padding-top:.75rem}
.py-8{padding-top:2rem;padding-bottom:2rem}
@media (min-width:640px){.sm\\:mt-0{margin-top:0}}
@media (min-width:1024px){.lg\\:text-\\[64px\\]{font-size:64px}}
"""
font_face = f"@font-face {{font-family:'Plus Jakarta Sans';font-style:normal;font-weight:400 800;font-display:swap;src:url(data:font/woff2;base64,{font_b64}) format('woff2');}}"
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>APX. RevOps Technology Agency – Engineering Revenue Systems</title>
<meta name="description" content="APX. is a RevOps technology agency. We architect, integrate and run the systems your revenue engine depends on. From first touch to renewal, on the stack you already run.">
<meta name="theme-color" content="#8E2DE2">
<style>{font_face}</style>
<style>{tailwind}</style>
<style>{supplement}</style>
</head>
<body class="min-h-screen bg-white text-slate-900 selection:bg-purple-100">
{body}
<script>{lucide}</script>
<script>document.documentElement.classList.add('js');</script>
<script>
document.addEventListener('DOMContentLoaded', () => {{
  if (typeof lucide !== 'undefined') lucide.createIcons();
  const btn = document.getElementById('mnav-btn'), panel = document.getElementById('mnav');
  if (btn && panel) {{
    const setOpen = (open) => {{
      panel.classList.toggle('hidden', !open);
      btn.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      btn.querySelectorAll('svg.mnav-open-icon, i.mnav-open-icon').forEach(el => el.classList.toggle('hidden', open));
      btn.querySelectorAll('svg.mnav-close-icon, i.mnav-close-icon').forEach(el => el.classList.toggle('hidden', !open));
    }};
    btn.addEventListener('click', () => setOpen(panel.classList.contains('hidden')));
    panel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', e => {{ if (e.key === 'Escape' && !panel.classList.contains('hidden')) {{ setOpen(false); btn.focus(); }} }});
    window.matchMedia('(min-width: 768px)').addEventListener('change', e => {{ if (e.matches) setOpen(false); }});
  }}
  const els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {{
    const io = new IntersectionObserver(entries => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{
          const sibs = Array.from(e.target.parentElement.querySelectorAll(':scope > .rv'));
          e.target.style.transitionDelay = (sibs.indexOf(e.target) % 8) * 70 + 'ms';
          e.target.classList.add('on');
          io.unobserve(e.target);
        }}
      }});
    }}, {{threshold: 0.15}});
    els.forEach(el => io.observe(el));
  }} else {{ els.forEach(el => el.classList.add('on')); }}
}});
const navbar = document.getElementById('navbar');
if (navbar) window.addEventListener('scroll', () => {{
  if (window.scrollY > 20) {{
    navbar.classList.add('border-b','border-slate-100','shadow-sm','py-3');
    navbar.classList.remove('py-4');
  }} else {{
    navbar.classList.remove('border-b','border-slate-100','shadow-sm','py-3');
    navbar.classList.add('py-4');
  }}
}});
</script>
</body>
</html>"""
(work/'apx-root-landingpage.html').write_text(html)
print("assembled:", round(len(html)/1024), "KB")
