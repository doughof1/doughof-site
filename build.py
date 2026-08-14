from pathlib import Path
import html, shutil, re
from datetime import datetime

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
PUBLIC = ROOT / 'public'
BRAND_LOGO = ROOT / 'brand' / 'doug-hof-logo.png'

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
            ('Solution', "To successfully launch this control, I engaged in weekly meetings with legal partners to ensure compliance and defensibility while simultaneously collaborating with Instagram teams to integrate the control using the appropriate internal components, architecture, and placement. Additionally, I worked closely with engineering teams through dogfooding sessions and one-on-one meetings to conduct quality control and ensure an optimal user experience."),
        ],
        'ideation':[
            {
                'title':'Flow 1','image':'/images/social/flow-1.png',
                'pros':['These surfaces give space to explain how this works','It solves the problem of scalability'],
                'cons':['Adds an unnecessary surface','The user will have to go back and forth to see the status of each account'],
            },
            {
                'title':'Flow 2','image':'/images/social/flow-2.png',
                'pros':['Contains the experience to a single page flow','Quick profile access view bottom sheet'],
                'cons':['Unclear as to what I need to do','Very text heavy and confusing'],
            },
            {
                'title':'Flow 3','image':'/images/social/flow-3.png',
                'pros':['Less copy and less intimidating','Each profile now has a status making it clearer'],
                'cons':['Adds back the unnecessary surface','Redundant and excessive'],
            },
            {
                'title':'Final Flow','image':'/images/social/final-flow.png',
                'pros':['The user journey is now more clear','Leveraging the bottom sheet gives the user a strong sense of place'],
                'cons':['Still an overwhelming amount of copy','It solves the problem of scalability but by scrolling'],
            },
        ],
        'gallery':[('/images/social/social-context.webp','Social interaction shown in an ad experience')],
        'metrics':[('+0.41%','Proxy ads score, reducing cost for advertisers'),('+0.52%','A&A ad score improving ad quality for users'),('-33KW','Reduction of server usage marking a major capacity optimization')]
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
  <meta name="theme-color" content="#ED1C24" />
  <meta property="og:title" content="{esc(full_title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="{SITE['domain']}{og_image}" />
  <link rel="canonical" href="{SITE['domain']}{current}" />
  <link rel="icon" href="/assets/doug-hof-logo.png" type="image/png" />
  <link rel="stylesheet" href="/assets/site.css?v=brand-8" />
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <a href="/" class="brand" aria-label="Doug Hof home"><img class="brand-mark" src="/assets/doug-hof-logo.png" alt="" /><span class="brand-name">Doug Hof</span></a>
    <button class="menu-button" data-menu-button aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span class="menu-icon" aria-hidden="true"><span></span><span></span><span></span></span><span class="sr-only">Open menu</span></button>
    <nav id="site-nav" class="site-nav" data-nav>{nav(current)}<a class="nav-link nav-cta" href="mailto:{SITE['email']}">Let’s talk ↗</a></nav>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div><a href="/" class="footer-brand" aria-label="Doug Hof home"><img src="/assets/doug-hof-logo.png" alt="" /><span>Doug Hof</span></a><p class="kicker">Have a project or role in mind?</p><a class="footer-email" href="mailto:{SITE['email']}">{SITE['email']} ↗</a></div>
    <div class="footer-meta"><span>Product design · Design leadership</span><span>Madison, Wisconsin</span><span>© {datetime.now().year} Doug Hof</span></div>
  </footer>
  <script src="/assets/site.js?v=nav-2" defer></script>
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
    if p['slug'] == 'buy-with-prime-consent-optimization':
        pager = f'''<nav class="project-pager shell"><a href="/portfolio/{projects[idx-1]['slug']}/"><span>← Previous</span><strong>{esc(projects[idx-1]['title'])}</strong></a><a class="next" href="/portfolio/{projects[idx+1]['slug']}/"><span>Next →</span><strong>{esc(projects[idx+1]['title'])}</strong></a></nav>'''
        body = f'''<article class="case case-buy-with-prime-consent-optimization accent-page-blue">
          <header class="case-hero shell"><p class="kicker">Growth · Consent · Commerce</p><h1>Buy with Prime Consent Optimization</h1><p class="case-summary">Optimizing the consent moment—where users decide whether to share third-party data—was crucial to reducing drop-offs, improving conversion rates, and enabling personalized ad experiences for Buy with Prime, a partnership between Meta and Amazon.</p>{meta}</header>
          <figure class="case-hero-image shell-wide"><img src="/images/bwp/bwp-hero.webp" alt="Buy with Prime Consent Optimization project hero" /></figure>
          <section class="bwp-copy shell reveal"><h2>Overview</h2><p>Following Apple’s App Tracking Transparency (ATT) update in 2021, which limited social media companies’ ability to target users, Meta sought new opportunities to encourage data sharing and drive ad revenue. In late 2023, Meta and Amazon partnered to launch Buy with Prime, enabling Amazon shoppers to purchase products directly from Facebook and Instagram without leaving the apps. By linking their Facebook and Instagram accounts to Amazon, users can seamlessly buy products through in-feed promotions. However, this partnership requires a three-way agreement between the user, Meta, and Amazon, necessitating explicit consent for data sharing.</p></section>
          <section class="bwp-copy shell reveal"><h2>Problem</h2><p>Generally, the more data a platform has about a user, the better it can tailor ad experiences to their preferences. While Meta collects basic information when an account is created, users who choose not to share their full third-party data limit the system’s ability to deliver personalized ads and unlock features like Buy with Prime. This is where the consent moment becomes critical—often perceived as a dense wall of text that users either skim through and accept or abandon entirely. While many quickly tap “accept” and move on, a substantial cohort hesitates at this step, leading to significant drop-offs. Optimizing this key moment was essential to improving conversion rates and ensuring a seamless user experience.</p></section>
          <section class="bwp-split shell reveal"><div><h2>Challenge</h2><p>Design a transparent and user-friendly consent screen that avoids dark UI patterns, complies with Meta’s strict privacy standards, and effectively drives positive consent growth for both opted-in and opted-out users across Facebook and Instagram.</p></div><div><h2>Solution</h2><p>Through user research and prototype testing against our public-facing experience, we identified the most effective headline and CTA combination and the optimal placement for the consent moment.</p></div></section>
          <section class="bwp-flow-panel shell-wide reveal">
            <article><h3>User Flow 1</h3><img src="/images/bwp/flow-1.webp" alt="Buy with Prime user flow 1" loading="lazy" /></article>
            <article><h3>User Flow 2</h3><img src="/images/bwp/flow-2.webp" alt="Buy with Prime user flow 2" loading="lazy" /></article>
            <article><h3>User Flow 3</h3><img src="/images/bwp/flow-3.webp" alt="Buy with Prime user flow 3" loading="lazy" /></article>
            <article><h3>CTA Alts</h3><img src="/images/bwp/ctas.webp" alt="CTA language alternatives" loading="lazy" /></article>
          </section>
          <section class="bwp-copy shell reveal"><h2>Solution</h2><p>The team designed these three distinct consent placements and developed prototypes for each, bringing them through qualitative research sessions to uncover key insights and recommendations for both current and future ad partners. These optimizations enabled the team to meet its goal of linking millions of accounts by year-end while reducing the number of clicks per linked account by nearly 12%. This enhancement not only generated millions in ad revenue for Meta but also exceeded Amazon’s ad spend targets.</p></section>
          <figure class="bwp-solution-image shell-wide reveal"><img src="/images/bwp/solution-annotated.png" alt="Annotated final Buy with Prime consent design" loading="lazy" /></figure>
          <section class="bwp-results"><div class="shell"><p class="kicker">Post-launch results</p><div class="metrics-grid"><div><strong>6M</strong><span>Linked accounts with Meta, exceeding target goal</span></div><div><strong>$3.5M</strong><span>Additional revenue generated for the company</span></div><div><strong>+3 More</strong><span>Additional regions and ad partners planned following strong performance</span></div></div><div class="bwp-problems"><h2>Problems Solved</h2><p>Using clear and consistent language helps simplify the flow and reduce cognitive load. The original consent flow used “Allow/Don’t Allow” as its primary CTA, but testing a revised CTA with “Link/Don’t link,” paired with a corresponding heading, led to a 0.5% increase in opt-ins. Simplifying the language to a more intuitive label proved effective in driving higher engagement. Additionally, we observed a further increase in consent rates by reordering value propositions. Previous research revealed that users prioritized “checking out quickly” over “getting up-to-date pricing,” leading to improved opt-in performance.</p></div></div></section>
          {pager}
        </article>'''
        return base(p['title'], body, f'/portfolio/{p["slug"]}/', p['summary'], p['image'])
    if p['slug'] == 'skins':
        pager = f'''<nav class="project-pager shell"><a href="/portfolio/{projects[idx-1]['slug']}/"><span>← Previous</span><strong>{esc(projects[idx-1]['title'])}</strong></a><a class="next" href="/portfolio/{projects[idx+1]['slug']}/"><span>Next →</span><strong>{esc(projects[idx+1]['title'])}</strong></a></nav>'''
        body = f'''<article class="case case-skins accent-page-green">
          <header class="case-hero shell"><p class="kicker">Mobile · Gaming · Sports</p><h1>Skins</h1><p class="case-summary">Gamify the game of golf. A golf app that offers popular betting games, guided gameplay, seamless wagering with friends, and automated scorekeeping.</p>{meta}</header>
          <figure class="case-hero-image shell-wide"><img src="/images/skins/skins-hero.webp" alt="Skins golf app project hero" /></figure>
          <section class="skins-copy shell reveal"><h2>Overview</h2><p>Skins was a freelance project I joined through a network of former colleagues to lead design efforts. This moonlight project focused on the lucrative golf industry, specifically the side games that naturally occur during a traditional round. Skins aimed to provide players with a library of popular golf betting games, guided gameplay, seamless wagering with friends, and automated scorekeeping.</p><p>Over three years, the app evolved to include enhanced features, an expanded game library, and integration with GHIN (Golf Handicap &amp; Information Network). Throughout this process, I led all design efforts, including brand identity, marketing campaigns, email outreach, and product design.</p></section>
          <section class="skins-copy shell reveal"><h2>Problem</h2><p>Many golf apps help track scores, provide swing instruction, offer GPS tracking, and suggest clubs. However, none focused solely on side games played during a traditional round—games that add excitement through friendly wagers. The challenge is that most players don’t fully understand the rules, some games are more complex than others, and calculating payouts often defaults to trusting the player who knows the rules best.</p><p>The Skins App set out to eliminate this complexity, allowing players to focus on their game while handling all the math in the background and only requesting input when necessary. Adding to the challenge, not all games are the same—some require different player counts, while others allow multiple games to be layered.</p><p>Game discovery and education also needed a solution beyond a wall of confusing instructions. To uphold our core pillars of low friction and lightweight design, we needed to create a streamlined onboarding process that quickly gets players into the game with minimal effort.</p></section>
          <section class="skins-panel skins-panel--light shell-wide reveal"><div class="shell"><h2>Initial Design Thinking</h2><p>The initial approach to the “Start a Match” surface relied on search and filters to navigate the game library. However, the team quickly realized that each game needed a distinct identity, branded to align with the Skins look and feel.</p><p>The “User Profile” surface served a dual purpose—tracking user activity while also acting as a hub for adding friends, managing groups, and selecting courses.</p><p>At the heart of the app was the “Gameplay” surface, designed to highlight player rankings and earnings. Each hole provided users with two key CTAs: place a side bet or view the scorecard.</p><p>This first version of the app was designed as a utility to enhance gameplay, not distract from it. It needed to provide a quick snapshot of player rankings, ensuring users could stay focused on their round while easily tracking their standing.</p><figure class="skins-phone-art"><img src="/images/skins/initial-design.png" alt="Three early Skins mobile app screens" loading="lazy" /></figure></div></section>
          <section class="skins-copy shell reveal"><h2>UI Evolution</h2><p>After gathering feedback from stakeholders and early adopters, we refined the design to align with a newly established design system, ensuring consistency in icons, padding, and typography.</p><p>The Gameplay surface underwent a major redesign, introducing a unique rounded arch-scroll, allowing players to seamlessly navigate both holes and player standings simultaneously.</p><p>Game setup was streamlined into a single scrollable screen, accessible anytime via the flag icon. Additionally, the Round Payouts screen was designed to clearly display match results with a CTA to settle payments based on player standings.</p><figure class="skins-phone-art"><img src="/images/skins/skins-current.webp" alt="Four evolved Skins mobile app screens" loading="lazy" /></figure></section>
          <section class="skins-panel skins-panel--dark shell-wide reveal"><div class="shell"><h2>Game Icon Library</h2><p>When a new game was added to the app, I developed a library of assets, including a unique game icon and a custom animation for each.</p><img class="skins-panel-image" src="/images/skins/game-icons.png" alt="Skins game icon library" loading="lazy" /></div></section>
          <section class="skins-panel skins-panel--light shell-wide reveal"><div class="shell"><h2>Video and Animation</h2><p>A key part of each game was creating a how-to video that featured its animated game icon. I also repurposed these assets for the App Store preview video, ensuring a cohesive visual experience.</p><img class="skins-panel-image" src="/images/skins/video-animation.png" alt="Skins game animation and App Store video examples" loading="lazy" /></div></section>
          <section class="skins-copy shell reveal"><h2>Future Thinking</h2><p>Thinking long-term for the app and building on what we’ve learned from market feedback, there’s a clear demand for offline content, deeper personalization, and a space for golf influencers to connect with their communities. We envision a dynamic content feed where Skins users can consume short-form golf videos, react to scores, and even place bets on games they’re not actively playing. The future of Skins is bright, with strong potential for growth and innovation in the golf tech space.</p><figure class="skins-phone-art"><img src="/images/skins/future-thinking.png" alt="Four future Skins mobile app concepts" loading="lazy" /></figure></section>
          <section class="skins-results"><div class="shell"><p class="kicker">Post-launch results</p><div class="metrics-grid"><div><strong>50+</strong><span>Unique games added to the library</span></div><div><strong>+10K</strong><span>Active users in the community</span></div><div><strong>+30K</strong><span>Rounds of golf played using Skins</span></div></div></div></section>
          {pager}
        </article>'''
        return base(p['title'], body, f'/portfolio/{p["slug"]}/', p['summary'], p['image'])
    if p['slug'] == 'pinnacle-series':
        pager = f'''<nav class="project-pager shell"><a href="/portfolio/{projects[idx-1]['slug']}/"><span>← Previous</span><strong>{esc(projects[idx-1]['title'])}</strong></a><a class="next" href="/portfolio/{projects[idx+1]['slug']}/"><span>Next →</span><strong>{esc(projects[idx+1]['title'])}</strong></a></nav>'''
        body = f'''<article class="case case-pinnacle-series accent-page-purple">
          <header class="case-hero shell"><p class="kicker">B2B · SaaS · Design Systems</p><h1>Pinnacle Series Redesign</h1><p class="case-summary">Eagle Point Software’s Pinnacle Series platform needed to be brought into the modern age. This project involved a multi-phase redesign of their flagship learning management system, reimagining it from the ground up.</p>{meta}</header>
          <figure class="case-hero-image shell-wide"><img src="/images/pinnacle/pinnacle-hero.webp" alt="Pinnacle Series learning platform redesign" /></figure>
          <section class="pinnacle-copy shell reveal"><h2>Overview</h2><p>Eagle Point Software is a leader in comprehensive learning management systems. Companies that employ architects, engineers, manufacturers, or construction workers often need to meet safety and compliance requirements. Pinnacle Series software enables organizations to ensure employee compliance, share knowledge and resources, and enhance skills.</p></section>
          <section class="pinnacle-copy shell reveal"><h2>Problem</h2><p>Pinnacle Series had achieved product-market fit well before my arrival. The company was notably profitable and experiencing growth, despite its software being somewhat antiquated. The challenge they faced was scaling: as they continued to rely on traditional install methods, they lacked a web-based version of their platform.</p></section>
          <section class="pinnacle-panel pinnacle-panel--light shell-wide reveal"><div class="shell"><h2>Out with the Old</h2><p>Their software was limited by its reliance on outdated installation methods that primarily operated on Windows-based machines. This presented significant barriers to scalability and usability, particularly for users operating in the field. The user experience was superb, resembling a folder structure that depended heavily on file naming conventions and document types.</p><img src="/images/pinnacle/old-1.webp" alt="Previous Windows-based Pinnacle management experience" loading="lazy" /></div></section>
          <section class="pinnacle-copy shell reveal"><h2>Dynamic Solutions</h2><p>Collaborating with leadership, engineering, and customer experience revealed the necessity for our design to accommodate admins, managers, and employees, each having distinct access to various features and controls.</p><p>To address this issue, I developed a unified side navigation layout that displayed access options based on user profiles. This approach not only streamlined the design but also ensured that only relevant features were presented to each user, simplifying the design and solving for scale.</p><figure class="pinnacle-art"><img src="/images/pinnacle/users.webp" alt="Redesigned Pinnacle user management" loading="lazy" /></figure></section>
          <section class="pinnacle-panel pinnacle-panel--dark shell-wide reveal"><div class="shell"><h2>Expansive Libraries</h2><p>The previous version of the software relied heavily on file naming conventions and document types, which hindered users’ ability to search and discover content organically. To address this, I developed a new set of document icons and paired them with auto-generated screenshots of each document. This provided each file with a unique visual identifier that did not solely depend on its title. Content creator admins were also given the ability to create their own file assets if they chose to do so.</p><img src="/images/pinnacle/library.webp" alt="Redesigned visual Pinnacle content library" loading="lazy" /></div></section>
          <section class="pinnacle-copy shell reveal"><h2>Scalable Solutions</h2><p>Each industry and company has different content types, including videos, Word documents, learning paths, Excel sheets, and PDFs. To address this, we developed a scalable framework capable of accommodating these various content types along with their associated metadata.</p><p>My solution involved creating a template that included a content area alongside a sidebar navigation to effectively organize and present the diverse metadata.</p><figure class="pinnacle-art"><img src="/images/pinnacle/scalable-solutions.png" alt="Scalable Pinnacle content template" loading="lazy" /></figure></section>
          <section class="pinnacle-copy pinnacle-home-copy shell reveal"><h2>A New Home</h2><p>To provide admins with a foundation that was missing in the previous version, I implemented a home screen framework. This new feature serves to educate first-time users, announce new content and partnerships, and offer a smooth transition when they begin using the app.</p><figure class="pinnacle-art"><img src="/images/pinnacle/home.webp" alt="Pinnacle Series Admin Home experience" loading="lazy" /></figure></section>
          <section class="pinnacle-learnings shell-wide"><div class="shell"><h2>Post-Launch Learnings</h2><p>My experience with Eagle Point focused on establishing the foundational elements necessary for scaling their product. After my departure, Pinnacle Series successfully relaunched as a web-based platform and introduced a later version of the app, catering to market segments with smaller-scale requirements. Additionally, my design contributions facilitated a brand relaunch that aligned with the modern aesthetic I developed.</p></div></section>
          {pager}
        </article>'''
        return base(p['title'], body, f'/portfolio/{p["slug"]}/', p['summary'], p['image'])
    sections=[]
    gallery_iter=iter(p['gallery'])
    for i,(title,text) in enumerate(p['sections']):
        sections.append(f'<section class="case-section shell reveal"><div class="case-section__index">{i+1:02}</div><div><h2>{esc(title)}</h2><p>{esc(text)}</p></div></section>')
        if p['gallery'] and i in (0,2,3):
            try:
                path,cap=next(gallery_iter)
                sections.append(f'<figure class="case-image shell-wide reveal"><img src="{path}" alt="{esc(cap)}" loading="lazy"/><figcaption>{esc(cap)}</figcaption></figure>')
            except StopIteration: pass
        if title == 'Alignment' and p.get('ideation'):
            flow_cards=[]
            for flow in p['ideation']:
                pros=''.join(f'<li>{esc(item)}</li>' for item in flow['pros'])
                cons=''.join(f'<li>{esc(item)}</li>' for item in flow['cons'])
                flow_cards.append(f'''<article class="flow-card reveal">
                  <h3>{esc(flow['title'])}</h3>
                  <figure class="flow-art"><img src="{flow['image']}" alt="Three mobile screens showing {esc(flow['title'])}" loading="lazy" /></figure>
                  <div class="tradeoffs"><div><h4>Pros</h4><ul>{pros}</ul></div><div><h4>Cons</h4><ul>{cons}</ul></div></div>
                </article>''')
            sections.append(f'''<section class="ideation shell-wide">
              <header class="ideation-heading shell"><p class="kicker">Exploration</p><h2>Ideation</h2><p>Rapid ideation enabled us to map out four different flows, pinpointing pain points and reducing cognitive load.</p></header>
              <div class="flow-list">{''.join(flow_cards)}</div>
            </section>''')
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
    body=f'''<article class="case case-{p['slug']} accent-page-{p['accent']}"><header class="case-hero shell"><p class="kicker">{esc(p['eyebrow'])}</p><h1>{esc(p['title'])}</h1><p class="case-summary">{esc(p['summary'])}</p>{meta}</header><figure class="case-hero-image shell-wide"><img src="{p['image']}" alt="{esc(p['title'])} project hero" /></figure>{''.join(sections)}{metrics}{pager}</article>'''
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
    shutil.copy(BRAND_LOGO, DIST/'assets'/'doug-hof-logo.png')
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
