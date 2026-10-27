(() => {
  'use strict';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const header = document.querySelector('.site-header');
  const progress = document.querySelector('.progress-line');
  const sticky = document.querySelector('.mobile-sticky');
  const stickyBlockers = new Set();
  let scrollPending = false;
  const scrollUpdate = () => {
    header.classList.toggle('scrolled', scrollY > 15);
    const height = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = `scaleX(${height > 0 ? Math.min(1, scrollY / height) : 0})`;
    const showSticky = innerWidth <= 700 && innerHeight > 500 && scrollY > 520
      && location.pathname.replace(/\/$/,'') !== '/contact'
      && !document.body.classList.contains('menu-open') && !stickyBlockers.size
      && !document.activeElement?.matches('input,textarea,select');
    sticky.classList.toggle('visible', showSticky);
    sticky.inert = !showSticky;
    sticky.setAttribute('aria-hidden', String(!showSticky));
    scrollPending = false;
  };
  addEventListener('scroll', () => {if(!scrollPending){scrollPending = true;requestAnimationFrame(scrollUpdate);}}, {passive: true});
  scrollUpdate();
  addEventListener('resize', scrollUpdate, {passive: true});
  document.addEventListener('focusin', scrollUpdate);
  document.addEventListener('focusout', () => queueMicrotask(scrollUpdate));
  if ('IntersectionObserver' in window) {
    const stickyObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => entry.isIntersecting ? stickyBlockers.add(entry.target) : stickyBlockers.delete(entry.target));
      scrollUpdate();
    }, {threshold: 0});
    document.querySelectorAll('.site-footer, main .cta-panel, [data-contact-section]').forEach(el => stickyObserver.observe(el));
  }
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    toggle.textContent = open ? '×' : '☰';
    nav.classList.toggle('open',open);
    document.body.classList.toggle('menu-open',open);
    document.querySelectorAll('main,.site-footer,.mobile-sticky').forEach(el => {el.inert=open;});
    scrollUpdate();
  }
  toggle.addEventListener('click',()=>setMenu(toggle.getAttribute('aria-expanded')!=='true'));
  document.addEventListener('keydown',e=>{
    if(e.key==='Escape' && nav.classList.contains('open')){setMenu(false);toggle.focus();}
    if(e.key==='Tab' && nav.classList.contains('open')){
      const links=[...nav.querySelectorAll('a')];
      if(e.shiftKey && document.activeElement===links[0]){e.preventDefault();toggle.focus();}
      else if(!e.shiftKey && document.activeElement===toggle){e.preventDefault();links[0].focus();}
    }
  });
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
  addEventListener('resize',()=>{if(innerWidth>700)setMenu(false);},{passive:true});
  document.querySelector('.back-top').addEventListener('click',()=>scrollTo({top:0,behavior:reduced.matches?'instant':'smooth'}));
  if('IntersectionObserver' in window && !reduced.matches){
    document.body.classList.add('motion-ready');
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target);}}),{threshold:.08});
    document.querySelectorAll('.reveal').forEach(e=>observer.observe(e));
  }
  const stage=document.querySelector('.hero-stage');
  if(stage && matchMedia('(pointer:fine)').matches){
    const model=stage.querySelector('.stage-model');
    stage.addEventListener('pointermove',e=>{
      if(reduced.matches)return;
      const r=stage.getBoundingClientRect();
      model.style.setProperty('--ry',`${-10+(e.clientX-r.left-r.width/2)/r.width*13}deg`);
      model.style.setProperty('--rx',`${6-(e.clientY-r.top-r.height/2)/r.height*9}deg`);
    });
    stage.addEventListener('pointerleave',()=>{model.style.setProperty('--ry','-10deg');model.style.setProperty('--rx','6deg');});
  }
  const demos={
    ecrire:{title:'Passez des notes brutes au compte rendu utile.',desc:'L’IA prépare une synthèse structurée à partir de vos notes. Vous vérifiez les faits, précisez les décisions et partagez un document clair.',paper:'La réunion est finie. La suite est claire.',rows:['Les décisions sont regroupées.','Les actions sont identifiées.','L’équipe valide la synthèse.']},
    organiser:{title:'Transformez vos informations en un plan lisible.',desc:'À partir de documents préparés et de vos priorités, l’IA vous aide à classer les informations et à organiser les prochaines étapes. Vous choisissez ce qui compte.',paper:'Des informations. Un cap partagé.',rows:['Les sujets sont regroupés.','Les priorités sont proposées.','Vous décidez du plan d’action.']},
    automatiser:{title:'Reliez les étapes qui se répètent chaque jour.',desc:'Une demande arrive, les informations sont classées et un brouillon est préparé. L’automatisation fait circuler le travail. Votre équipe garde la validation.',paper:'Une demande reçue. La suite préparée.',rows:['Les informations sont structurées.','Un brouillon est préparé.','Votre équipe décide de l’envoi.']}
  };
  const tabs=[...document.querySelectorAll('[data-demo]')];
  function selectTab(tab,focus=false){
    const data=demos[tab.dataset.demo];
    tabs.forEach(t=>{t.setAttribute('aria-selected',String(t===tab));t.tabIndex=t===tab?0:-1;});
    document.getElementById('tool-panel').setAttribute('aria-labelledby',tab.id);
    document.getElementById('tool-title').textContent=data.title;
    document.getElementById('tool-description').textContent=data.desc;
    document.getElementById('demo-title').textContent=data.paper;
    document.getElementById('demo-rows').replaceChildren(...data.rows.map(text=>{const row=document.createElement('div');row.className='demo-row';const check=document.createElement('span');check.textContent='✓';row.append(check,document.createTextNode(text));return row;}));
    if(focus)tab.focus();
  }
  tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>selectTab(tab));tab.addEventListener('keydown',e=>{let next;if(e.key==='ArrowRight')next=(i+1)%tabs.length;if(e.key==='ArrowLeft')next=(i+tabs.length-1)%tabs.length;if(e.key==='Home')next=0;if(e.key==='End')next=tabs.length-1;if(next!==undefined){e.preventDefault();selectTab(tabs[next],true);}});});
  const form=document.getElementById('contact-form');
  if(form){
    const fields = Object.fromEntries(['name','company','email','need','message'].map(key => [key, form.elements.namedItem(key)]));

    const params=new URLSearchParams(location.search),need=params.get('besoin');
    if([...fields.need.options].some(o=>o.value===need))fields.need.value=need;
    const programs={responsable:'IA responsable',metier:'IA métier',communication:'IA communication','vibe-coding':'Vibe coding',performance:'Vibe coding'};
    if(programs[params.get('programme')])fields.message.value=`Bonjour Florian, je souhaite échanger au sujet de la formation ${programs[params.get('programme')]}.`;
    let message='';
    form.addEventListener('submit',e=>{
      e.preventDefault();if(!form.reportValidity())return;
      const name=fields.name.value.trim(),company=fields.company.value.trim(),email=fields.email.value.trim();
      message=`Bonjour Florian,\n\n${fields.message.value.trim()}\n\nMon besoin : ${fields.need.selectedOptions[0].textContent}\n\n${name}${company?'\n'+company:''}\n${email}`;
      const href=`mailto:escale.digitale.solutions@gmail.com?subject=${encodeURIComponent('Échange EDS — '+fields.need.selectedOptions[0].textContent)}&body=${encodeURIComponent(message)}`;
      const link=document.getElementById('email-link');link.href=href;
      const feedback=document.getElementById('form-feedback');feedback.hidden=false;link.click();
    });
    form.querySelector('button[type="submit"]').disabled=false;
    document.getElementById('copy-message').addEventListener('click',async e=>{
      try{await navigator.clipboard.writeText(message);e.target.textContent='Message copié ✓';}
      catch{const area=document.createElement('textarea');area.value=message;area.setAttribute('aria-label','Message à copier');document.getElementById('form-feedback').append(area);area.focus();area.select();e.target.textContent='Sélectionnez puis copiez le texte';}
    });
  }
})();
