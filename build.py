from pathlib import Path
import html, shutil, re
from datetime import datetime

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
PUBLIC = ROOT / 'public'

SITE = {
    'title': 'Doug Hof — Product Design & Design Leadership',
    'description': 'Product design leader focused on consumer experiences, design systems, growth, privacy, commerce, and zero-to-one products.',
    'email': 'doughof@gmail.com',
    'phone': '(319) 331-8611',
    'domain': 'https://doughof.com',
}

NAV = [('/', 'Home'), ('/projects/', 'Projects'), ('/process/', 'Process'), ('/about/', 'About')]

projects = [
    {
        'slug':'social-interactions-control','title':'Social Interactions Control','year':'2024','company':'Meta','role':'UI/UX Design Lead','type':'Product Design',
        'eyebrow':'Privacy · Ads · Platform','accent':'blue','image':'/images/social/social-hero.webp',
        'summary':"A globally launched ad control extending Facebook's social-interaction transparency to Instagram and Accounts Center.",
        'sections':[
            ('Overview', "When a user likes a brand page that is running an ad, Facebook may surface that social interaction to friends. At the time, users could manage the control on Facebook but not Instagram. The work expanded the control to Instagram and integrated it into Accounts Center so people could manage settings across Meta products from one place."),
            ('Problem', "The experience needed to give people a clear, defensible privacy control while scaling across Facebook and Instagram—and potentially future platforms—without introducing unnecessary screens or cognitive load."),
            ('Challenge', "Use existing platform components, satisfy privacy and policy requirements, support users inside and outside Accounts Center, and create a structure that could scale as more profiles and products were added."),
            ('Alignment', "The work required close collaboration across Facebook and Instagram design, privacy, legal, product and engineering. Multiple flow directions were explored before converging on a compact profile-based pattern with clear status and a bottom-sheet interaction."),
            ('Solution', "The final experience kept the user grounded in a single setting, made account-level status visible, and reused established architecture rather than creating a bespoke control. I partnered with legal on compliance and defensibility and worked directly with engineering through dogfooding and quality-control sessions."),
        ],
        'gallery':[('/images/social/social-context.webp','Social interaction shown in an ad experience')],
        'metrics':[('+0.41%','Proxy ads score'),('+0.52%','A&A ads score'),('-33KW','Server capacity reduction')]
    },
    {
        'slug':'buy-with-prime-consent-optimization','title':'Buy with Prime Consent Optimization','year':'2024','company':'Meta','role':'UI/UX Design Lead','type':'Product Design',
        'eyebrow':'Growth · Consent · Commerce','accent':'blue','image':'/images/bwp/bwp-hero.webp',
        'summary':'Optimizing the consent moment for Buy with Prime to reduce drop-off, improve conversion, and unlock personalized commerce experiences.',
        'sections':[
            ('Overview', "Meta and Amazon partnered on Buy with Prime, allowing shoppers to purchase promoted products without leaving Facebook or Instagram. Linking accounts required an explicit consent relationship between the user, Meta and Amazon."),
            ('Problem', "Consent screens are easy to turn into dense walls of text. The challenge was to improve comprehension and conversion without using dark patterns, while meeting strict privacy and policy requirements across Facebook and Instagram."),
            ('Research & Testing', "The team prototyped multiple placements in the purchase journey and tested language, value-proposition order and CTA labels. Research showed that people responded more strongly to the immediate benefit of checking out quickly than to secondary pricing benefits."),
            ('Solution', "We identified the strongest consent placement and simplified the language around the decision. Changing the primary action from generic permission language to the more concrete 'Link / Don’t link' framing produced a measurable lift while keeping the decision explicit."),
            ('Problems Solved', "The optimized flow reduced clicks per linked account by nearly 12%, improved opt-in performance, and created a reusable consent pattern for future commerce partners."),
        ],
        'gallery':[
            ('/images/bwp/flow-1.webp','Consent placement concept 1'),('/images/bwp/flow-2.webp','Consent placement concept 2'),('/images/bwp/flow-3.webp','Consent placement concept 3'),('/images/bwp/ctas.webp','CTA language alternatives')
        ],
        'metrics':[('6M','Linked accounts'),('$3.5M','Additional revenue'),('+3','Additional partner / region expansion')]
    },
    {
        'slug':'skins','title':'Skins','year':'2020–2023','company':'Skins','role':'Product Design Lead','type':'Freelance Product Design',
        'eyebrow':'0→1 · Mobile · Sports','accent':'green','image':'/images/skins/skins-hero.webp',
        'summary':'A golf app that turns side games, wagers and scorekeeping into a guided, lightweight experience.',
        'sections':[
            ('Overview', "Skins began as a freelance product-design engagement and evolved over several years. I led product design as the app expanded its betting-game library, introduced GHIN integration, and developed a more complete social layer around rounds and groups."),
            ('Problem', "Golfers play dozens of side games, but the rules vary, payouts get complicated, and one person usually becomes the scorekeeper. The product needed to manage that complexity without becoming a distraction during a round."),
            ('Initial Design Thinking', "The first approach centered on game discovery, a lightweight setup flow, a player profile that doubled as a social hub, and a gameplay surface that surfaced only the information needed on the current hole."),
            ('UI Evolution', "As the design system matured, gameplay was rebuilt around a distinctive curved navigation treatment, while game setup was consolidated into a scrollable surface. Payouts were redesigned to clearly show match outcomes and who owed whom."),
            ('Future Thinking', "The longer-term opportunity extended beyond scorekeeping into offline content, personalization, short-form golf media and community features that allow people to follow rounds even when they are not actively playing."),
        ],
        'gallery':[('/images/skins/skins-current.webp','Evolved Skins product UI')],
        'metrics':[('50+','Games in the library'),('10K+','Active users'),('30K+','Rounds played')]
    },
    {
        'slug':'pinnacle-series','title':'Pinnacle Series Redesign','year':'2021','company':'Eagle Point Software','role':'Product Design Lead','type':'Product Design',
        'eyebrow':'B2B · SaaS · Design Systems','accent':'purple','image':'/images/pinnacle/pinnacle-hero.webp',
        'summary':'A multi-phase redesign that moved a mature desktop learning platform toward a modern, scalable web experience.',
        'sections':[
            ('Overview', "Pinnacle Series helps architecture, engineering, manufacturing and construction organizations manage training, compliance and knowledge. The product had strong market fit, but its installed desktop experience created usability and scaling constraints."),
            ('Out with the Old', "The existing experience relied heavily on folders, file names and desktop installation patterns. That made discovery difficult and limited access for people working outside traditional Windows environments."),
            ('Dynamic Solutions', "I developed a unified navigation model that adapted to admin, manager and employee permissions, simplifying the experience while keeping the system flexible across customer types."),
            ('Expansive Libraries', "Library content was redesigned with visual document identities, metadata and filtering so users could recognize and discover content without relying entirely on file names."),
            ('A New Home', "A new home framework gave administrators onboarding guidance, product education and a place for announcements, while establishing a reusable shell for future modules."),
        ],
        'gallery':[('/images/pinnacle/old-1.webp','Previous Windows-based management experience'),('/images/pinnacle/users.webp','Redesigned user management'),('/images/pinnacle/library.webp','Redesigned content library'),('/images/pinnacle/home.webp','New admin home')],
        'metrics':[]
    },
    {
        'slug':'spin','title':'Spin Live Shopping','year':'2020','company':'Spin','role':'Creative Director, Product Design Lead','type':'Product Design',
        'eyebrow':'Startup · Commerce · Live Video','accent':'orange','image':'/images/spin/spin-hero.webp',
        'summary':'A live-shopping startup built around product discovery, creators and short-form commerce content.',
        'sections':[
            ('Overview', "Spin was a significant pivot from Gravy Live. We narrowed the product toward health and beauty, moved to a softer visual language, and built a creator-led discovery experience for a predominantly female audience."),
            ('Why Pivot?', "Beauty offered more SKUs, lower shipping costs and healthier margins than the higher-ticket tech products we had focused on previously. That gave the product team more room to improve content quality, creator engagement and shopping frequency."),
            ('Design Thinking', "The product borrowed the immediacy of vertical short-form video. Instead of relying on a conventional tab bar, the experience used gestures to move between products, details, creator profiles and social interactions while keeping commerce actions one tap away."),
            ('Learnings', "Live-streaming products need both compelling content and repeatable distribution. Synchronous moments can create excitement, but asynchronous content gives users more control over when and how they engage."),
        ],
        'gallery':[('/images/spin/screens-1.webp','Spin mobile shopping surfaces')],
        'metrics':[]
    },
    {
        'slug':'spin-for-web','title':'Spin for Web','year':'2020','company':'Spin','role':'Creative Direction, UI/UX Design','type':'Web + B2B Product',
        'eyebrow':'Web · Merchant Tools · Creator Tools','accent':'orange','image':'/images/spin/spin-web.webp',
        'summary':'Web experiences for consumers, merchants and influencers plus a merchant / creator operations hub.',
        'sections':[
            ('The Challenge', "The public website had to serve three distinct audiences: consumers discovering the app, merchants providing products and offers, and influencers creating content. Each needed a clear path and a tailored call to action."),
            ('Merchant & Influencer Hub', "Behind the marketing site, we designed tools for merchants to upload products, create offers and build streams, plus a sister workflow for influencers to discover offers and assemble content."),
            ('Solution', "Inspired in part by Etsy’s Shop Manager, the workflow broke complex data entry into smaller steps, pre-populated fields where possible, and used contextual help and suggested values to reduce friction."),
        ],
        'gallery':[('/images/spin/create-offer.webp','Merchant offer creation workflow')],
        'metrics':[]
    },
    {
        'slug':'gravy-live','title':'Gravy Live','year':'2017–2020','company':'Gravy Live','role':'Creative Director, Product Design Lead','type':'Product Design',
        'eyebrow':'Founder · 0→1 · Live Commerce','accent':'pink','image':'/images/gravy/gravy-hero.webp',
        'summary':'A synchronous reverse-auction shopping app where prices dropped from full price toward free until inventory sold out.',
        'sections':[
            ('Overview', "Every night a host revealed a hidden product and dropped its price in real time. Users could buy whenever the deal felt right, but they did not know how much inventory remained or who else was buying."),
            ('Design Thinking', "The visual system leaned into a game-show atmosphere: bright color, dark studio backgrounds and frequent motion. Lightweight Lottie animation let the product feel playful without adding heavy native assets."),
            ('My Solution', "After an early desktop concept failed to find traction, the product was simplified around the core dropping-price mechanic. The redesign focused attention on the product, host, live price and trust signals while using scheduled notifications to support the synchronous model."),
            ('Results & Learnings', "The company went through several pivots and taught us a lot about synchronous behavior, category economics and influencer acquisition. The strongest lesson was that users need control over when they engage, even when the core experience is live."),
        ],
        'gallery':[],
        'metrics':[]
    },
    {
        'slug':'branding','title':'Brand Identity','year':'Selected work','company':'Freelance + Startups','role':'Creative Direction','type':'Brand Design',
        'eyebrow':'Identity · Illustration · Systems','accent':'tan','image':'/images/about/wisconsin-barrel.webp',
        'summary':'Selected identity work across startups, local businesses and freelance clients.',
        'sections':[
            ('Wisconsin Barrel Company', "A rustic but legible identity built around a top-down barrel form and a vintage typographic voice."),
            ('Freefox', "A print-on-demand concept built around negative space, simple geometry and an intentionally vintage Midwest feel."),
            ('Back Pocket', "A gentler rebrand for a youth mental-health support program, using a pocket-and-heart metaphor designed to flex across educational materials."),
            ('Spin', "A clean, playful mark designed to coexist with many merchant brands while still suggesting movement and live energy."),
            ('Freestyle Concrete Design', "A system of heavy geometric lines and earthy color designed to reference walkways and concrete without becoming literal."),
        ],
        'gallery':[], 'metrics':[]
    },
    {
        'slug':'video-and-animation','title':'Video and Animation','year':'Selected work','company':'Gravy + Spin','role':'Motion + Creative Direction','type':'Motion Design',
        'eyebrow':'After Effects · Lottie · Motion','accent':'pink','image':'/images/gravy/gravy-hero.webp',
        'summary':'Motion, app-store previews and animated product moments created to explain, market and energize live-shopping products.',
        'sections':[
            ('Motion as Product Design', "I used After Effects, Audition, Bodymovin and Lottie to build lightweight motion that could move from marketing into the product experience."),
            ('App Store Preview', "The preview had to demonstrate a live-shopping format without relying on a long voiceover, balancing real footage with feature explanation and product UI."),
            ('Surprise & Delight', "Animated characters and celebratory moments made wins, referrals and transitions feel more rewarding while keeping implementation lightweight for iOS and Android."),
        ],
        'gallery':[], 'metrics':[]
    },
    {
        'slug':'just-for-fun','title':'Just for fun.','year':'Ongoing','company':'Personal','role':'Designer / Maker','type':'Creative Work',
        'eyebrow':'Because why not?','accent':'tan','image':'/images/about/fun-wedding.webp',
        'summary':'Experiments, illustrations and creative work made simply because design is hard to turn off.',
        'sections':[('Always making', "When design is in your DNA, you’re always creating something. This page is a home for the projects that do not need a product roadmap, KPI or launch plan to justify existing.")],
        'gallery':[], 'metrics':[]
    },
]

PROJECT_BY_SLUG = {p['slug']: p for p in projects}


def esc(s): return html.escape(str(s), quote=True)

def nav(current='/'):
    links=[]
    for href,label in NAV:
        active = current == href or (href != '/' and current.startswith(href))
        links.append(f'<a class="nav-link {"active" if active else ""}" href="{href}">{label}</a>')
    return ''.join(links)

def base(title, body, current='/', description=None, og_image='/images/social/social-hero.webp'):
    full_title = title if title == SITE['title'] else f"{title} — Doug Hof"
    desc = description or SITE['description']
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{esc(full_title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <meta name="theme-color" content="#f4f1ec" />
  <meta property="og:title" content="{esc(full_title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="{SITE['domain']}{og_image}" />
  <link rel="canonical" href="{SITE['domain']}{current}" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/assets/site.css" />
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <a href="/" class="brand" aria-label="Doug Hof home"><span class="brand-mark">DH</span><span class="brand-name">Doug Hof</span></a>
    <button class="menu-button" data-menu-button aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="site-nav" data-nav>{nav(current)}<a class="nav-link nav-cta" href="mailto:{SITE['email']}">Let’s talk ↗</a></nav>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div><p class="kicker">Have a project or role in mind?</p><a class="footer-email" href="mailto:{SITE['email']}">{SITE['email']} ↗</a></div>
    <div class="footer-meta"><span>Product design · Design leadership</span><span>Madison, Wisconsin</span><span>© {datetime.now().year} Doug Hof</span></div>
  </footer>
  <script src="/assets/site.js" defer></script>
</body>
</html>'''

def project_card(p, index=0, featured=False):
    return f'''<a class="project-card {"project-card--featured" if featured else ""} reveal" href="/portfolio/{p['slug']}/" style="--delay:{index*45}ms">
      <div class="project-card__media accent-{p['accent']}"><img src="{p['image']}" alt="{esc(p['title'])} project preview" loading="lazy" /></div>
      <div class="project-card__body">
        <div class="project-card__meta"><span>{esc(p['year'])}</span><span>{esc(p['eyebrow'])}</span></div>
        <h3>{esc(p['title'])}</h3><p>{esc(p['summary'])}</p><span class="text-link">View case study <b>↗</b></span>
      </div>
    </a>'''

def home_page():
    featured = [PROJECT_BY_SLUG[x] for x in ['social-interactions-control','buy-with-prime-consent-optimization','skins']]
    body = f'''
<section class="hero shell">
  <div class="hero-copy reveal">
    <p class="kicker"><span class="status-dot"></span> Product design leader · Madison, WI</p>
    <h1>I design products people understand <em>and</em> businesses can grow.</h1>
    <p class="hero-lede">I’m Doug Hof, a product design director with 15+ years across startups and global products—leading teams, shaping product vision, building systems, and turning complicated experiences into clear ones.</p>
    <div class="hero-actions"><a class="button button--dark" href="/projects/">Explore the work <span>↗</span></a><a class="button button--ghost" href="/about/">More about me</a></div>
  </div>
  <div class="hero-portrait reveal"><div class="portrait-bg"></div><img src="/images/home/doug.webp" alt="Portrait of Doug Hof" /><div class="hero-note"><span>Currently</span><strong>Director of Product Design</strong><small>RetailMeNot</small></div></div>
</section>
<section class="selected shell">
  <div class="section-heading"><div><p class="kicker">Selected work</p><h2>Complex problems.<br/>Clear outcomes.</h2></div><p>Privacy, commerce, growth, SaaS, live shopping and zero-to-one product work across enterprise and startup environments.</p></div>
  <div class="featured-grid">{''.join(project_card(p,i,True) for i,p in enumerate(featured))}</div>
</section>
<section class="leadership-strip">
  <div class="shell leadership-grid"><div><p class="kicker">How I work</p><h2>Design is a team sport.</h2></div><div class="principles"><p><strong>01</strong> Start with the actual problem, not the requested screen.</p><p><strong>02</strong> Make the system understandable before making it beautiful.</p><p><strong>03</strong> Use craft, data and narrative to create alignment.</p><p><strong>04</strong> Build reusable decisions—not one-off deliverables.</p></div></div>
</section>
<section class="cta-panel shell reveal"><p class="kicker">Let’s build something useful</p><h2>Need someone who can move between product strategy, team leadership and pixel-level craft?</h2><a href="mailto:{SITE['email']}" class="button button--light">Start a conversation ↗</a></section>
'''
    return base(SITE['title'], body, '/', SITE['description'], '/images/social/social-hero.webp')

def projects_page():
    cards=''.join(project_card(p,i) for i,p in enumerate(projects))
    body=f'''<section class="page-hero shell"><p class="kicker">Portfolio / {len(projects):02}</p><h1>Selected projects<br/>from the last decade.</h1><p class="page-intro">A mix of product strategy, UX, visual design, systems, growth work and creative direction.</p></section><section class="shell"><div class="project-list">{cards}</div></section>'''
    return base('Projects', body, '/projects/')

def about_page():
    body=f'''<section class="page-hero shell about-hero"><div><p class="kicker">About</p><h1>People first.<br/>Designer second.</h1><p class="page-intro">I’m a product design leader, builder, dad, coach, furniture maker, coffee nerd and film obsessive based in Madison, Wisconsin.</p></div><div class="about-photo"><img src="/images/home/doug.webp" alt="Doug Hof" /></div></section>
<section class="shell prose-grid"><aside><p class="kicker">Who I am</p></aside><div class="prose"><p>We’re all people before we’re employees. I believe knowing where someone comes from, what motivates them and what they care about outside work makes collaboration stronger.</p><p>I’m a proud Midwesterner and a dad to three active kids. Outside the office you’ll usually find me coaching, building furniture in my workshop, obsessing over coffee, snowboarding, running, traveling with my family or analyzing the cinematography of a movie nobody else asked me to analyze.</p></div></section>
<section class="shell prose-grid"><aside><p class="kicker">At work</p></aside><div class="prose"><p>I’ve spent more than 15 years designing consumer and enterprise products across startups and large organizations. My experience spans zero-to-one products, design systems, privacy, ads, commerce, growth, live shopping and B2B tools.</p><p>I spent more than three years at Meta working on Responsibility & Privacy for Facebook and Instagram, launching global controls and commerce experiences. Today I lead product design at RetailMeNot, helping shape the next generation of savings and shopping experiences.</p><div class="contact-grid"><a href="mailto:{SITE['email']}"><span>Email</span><strong>{SITE['email']} ↗</strong></a><a href="tel:+13193318611"><span>Phone</span><strong>{SITE['phone']}</strong></a></div></div></section>
<section class="shell personal-card reveal"><div><p class="kicker">Not everything needs a KPI</p><h2>I still make things just because I want to.</h2><a href="/portfolio/just-for-fun/" class="text-link">See the fun stuff ↗</a></div><img src="/images/about/fun-wedding.webp" alt="Personal creative artwork" loading="lazy" /></section>'''
    return base('About', body, '/about/')

def process_page():
    steps=[
      ('01','Problem',"It starts with the problem. I write it down, challenge assumptions and keep asking what we are actually solving and why."),
      ('02','Research & discovery',"I look at user behavior, adjacent products, competitors and visual references. Inspiration is useful, but only after the problem is clear."),
      ('03','Wireframe',"I get ideas out quickly—often in a sketchbook first, then in Figma with enough fidelity to expose interaction and information-architecture issues."),
      ('04','Prototype',"Prototypes make decisions tangible. I use them to test flows, tell the story, pressure-test edge cases and build alignment before engineering cost increases."),
      ('05','Feedback, iterate, polish',"The last 10% is where details, QA, system consistency and cross-functional feedback turn a concept into something that feels finished."),
    ]
    rows=''.join(f'<article class="process-row reveal"><span>{n}</span><h2>{t}</h2><p>{d}</p></article>' for n,t,d in steps)
    body=f'''<section class="page-hero shell"><p class="kicker">Process</p><h1>Logic first.<br/>Craft all the way through.</h1><p class="page-intro">My process flexes to the team and problem, but the fundamentals stay consistent: understand, reduce, test, align and refine.</p></section><section class="shell process-images"><img src="/images/process/sketchbook3.webp" alt="Sketchbook notes and wireframes"/><img src="/images/process/sketchbook.webp" alt="Sketchbook product-flow notes"/></section><section class="shell process-list">{rows}</section>'''
    return base('Process', body, '/process/')

def project_page(p, idx):
    prevp = projects[idx-1] if idx>0 else None
    nextp = projects[idx+1] if idx<len(projects)-1 else None
    meta = f'''<div class="project-meta"><div><span>Project type</span><strong>{esc(p['type'])}</strong></div><div><span>Contribution</span><strong>{esc(p['role'])}</strong></div><div><span>Year</span><strong>{esc(p['year'])}</strong></div><div><span>Company</span><strong>{esc(p['company'])}</strong></div></div>'''
    sections=[]
    gallery_iter=iter(p['gallery'])
    for i,(title,text) in enumerate(p['sections']):
        sections.append(f'<section class="case-section shell reveal"><div class="case-section__index">{i+1:02}</div><div><h2>{esc(title)}</h2><p>{esc(text)}</p></div></section>')
        if p['gallery'] and i in (0,2,3):
            try:
                path,cap=next(gallery_iter)
                sections.append(f'<figure class="case-image shell-wide reveal"><img src="{path}" alt="{esc(cap)}" loading="lazy"/><figcaption>{esc(cap)}</figcaption></figure>')
            except StopIteration: pass
    # any remaining gallery
    rem=list(gallery_iter)
    if rem:
        sections.append('<section class="gallery shell-wide">'+''.join(f'<figure class="reveal"><img src="{a}" alt="{esc(c)}" loading="lazy"/><figcaption>{esc(c)}</figcaption></figure>' for a,c in rem)+'</section>')
    metrics=''
    if p['metrics']:
        metrics='<section class="metrics"><div class="shell"><p class="kicker">Post-launch results</p><div class="metrics-grid">'+''.join(f'<div><strong>{esc(v)}</strong><span>{esc(l)}</span></div>' for v,l in p['metrics'])+'</div></div></section>'
    pager='<nav class="project-pager shell">'
    pager += f'<a href="/portfolio/{prevp["slug"]}/"><span>← Previous</span><strong>{esc(prevp["title"])}</strong></a>' if prevp else '<span></span>'
    pager += f'<a class="next" href="/portfolio/{nextp["slug"]}/"><span>Next →</span><strong>{esc(nextp["title"])}</strong></a>' if nextp else '<a class="next" href="/projects/"><span>All work →</span><strong>Projects</strong></a>'
    pager+='</nav>'
    body=f'''<article class="case accent-page-{p['accent']}"><header class="case-hero shell"><p class="kicker">{esc(p['eyebrow'])}</p><h1>{esc(p['title'])}</h1><p class="case-summary">{esc(p['summary'])}</p>{meta}</header><figure class="case-hero-image shell-wide"><img src="{p['image']}" alt="{esc(p['title'])} project hero" /></figure>{''.join(sections)}{metrics}{pager}</article>'''
    return base(p['title'],body,f'/portfolio/{p["slug"]}/',p['summary'],p['image'])

def write(path, content):
    fp=DIST/path
    fp.parent.mkdir(parents=True,exist_ok=True)
    fp.write_text(content,encoding='utf-8')

def build():
    if DIST.exists(): shutil.rmtree(DIST)
    DIST.mkdir()
    # copy images
    shutil.copytree(PUBLIC/'images', DIST/'images')
    shutil.copytree(PUBLIC/'assets', DIST/'assets')
    shutil.copy(PUBLIC/'favicon.svg', DIST/'favicon.svg')
    write(Path('index.html'),home_page())
    write(Path('projects/index.html'),projects_page())
    write(Path('about/index.html'),about_page())
    write(Path('process/index.html'),process_page())
    for i,p in enumerate(projects): write(Path(f'portfolio/{p["slug"]}/index.html'),project_page(p,i))
    write(Path('404.html'),base('Not found','<section class="page-hero shell"><p class="kicker">404</p><h1>That page wandered off.</h1><p class="page-intro">The work is still here.</p><a class="button button--dark" href="/projects/">View projects ↗</a></section>','/404.html'))
    write(Path('robots.txt'),f'User-agent: *\nAllow: /\nSitemap: {SITE["domain"]}/sitemap.xml\n')
    urls=['/','/projects/','/process/','/about/']+[f'/portfolio/{p["slug"]}/' for p in projects]
    sitemap='''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''+''.join(f'  <url><loc>{SITE["domain"]}{u}</loc></url>\n' for u in urls)+'</urlset>\n'
    write(Path('sitemap.xml'),sitemap)
    print(f'Built {len(urls)} pages into {DIST}')

if __name__=='__main__': build()
