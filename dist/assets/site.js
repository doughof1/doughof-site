const button=document.querySelector('[data-menu-button]');
const nav=document.querySelector('[data-nav]');
if(button&&nav){button.addEventListener('click',()=>{const open=nav.classList.toggle('open');const label=open?'Close menu':'Open menu';button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',label);const text=button.querySelector('.sr-only');if(text)text.textContent=label;});}
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
