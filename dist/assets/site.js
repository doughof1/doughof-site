const button=document.querySelector('[data-menu-button]');
const nav=document.querySelector('[data-nav]');
if(button&&nav){button.addEventListener('click',()=>{const open=nav.classList.toggle('open');const label=open?'Close menu':'Open menu';button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',label);const text=button.querySelector('.sr-only');if(text)text.textContent=label;});}
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

const lightbox=document.querySelector('[data-image-lightbox]');
const lightboxTriggers=Array.from(document.querySelectorAll('.process-gallery img'));
if(lightbox&&lightboxTriggers.length){
  const lightboxImage=lightbox.querySelector('[data-lightbox-image]');
  const lightboxCaption=lightbox.querySelector('[data-lightbox-caption]');
  const lightboxCounter=lightbox.querySelector('[data-lightbox-counter]');
  const previousButton=lightbox.querySelector('[data-lightbox-previous]');
  const nextButton=lightbox.querySelector('[data-lightbox-next]');
  const closeButton=lightbox.querySelector('[data-lightbox-close]');
  let activeIndex=0;
  let returnTarget=null;

  const showImage=index=>{
    activeIndex=(index+lightboxTriggers.length)%lightboxTriggers.length;
    const source=lightboxTriggers[activeIndex];
    lightboxImage.src=source.currentSrc||source.src;
    lightboxImage.alt=source.alt;
    lightboxCaption.textContent=source.alt;
    lightboxCounter.textContent=`${activeIndex+1} / ${lightboxTriggers.length}`;
  };
  const openLightbox=index=>{
    returnTarget=lightboxTriggers[index].closest('figure');
    showImage(index);
    document.body.classList.add('lightbox-open');
    lightbox.showModal();
    closeButton.focus();
  };
  const closeLightbox=()=>lightbox.close();

  lightboxTriggers.forEach((image,index)=>{
    const trigger=image.closest('figure');
    if(!trigger)return;
    trigger.dataset.lightboxTrigger='';
    trigger.tabIndex=0;
    trigger.setAttribute('role','button');
    trigger.setAttribute('aria-label',`View larger: ${image.alt}`);
    trigger.addEventListener('click',()=>openLightbox(index));
    trigger.addEventListener('keydown',event=>{
      if(event.key==='Enter'||event.key===' '){event.preventDefault();openLightbox(index);}
    });
  });
  previousButton.addEventListener('click',()=>showImage(activeIndex-1));
  nextButton.addEventListener('click',()=>showImage(activeIndex+1));
  closeButton.addEventListener('click',closeLightbox);
  lightbox.addEventListener('click',event=>{if(event.target===lightbox)closeLightbox();});
  lightbox.addEventListener('keydown',event=>{
    if(event.key==='ArrowLeft'){event.preventDefault();showImage(activeIndex-1);}
    if(event.key==='ArrowRight'){event.preventDefault();showImage(activeIndex+1);}
    if(event.key==='Escape'){event.preventDefault();closeLightbox();}
  });
  lightbox.addEventListener('close',()=>{
    document.body.classList.remove('lightbox-open');
    lightboxImage.removeAttribute('src');
    returnTarget?.focus();
  });
}
