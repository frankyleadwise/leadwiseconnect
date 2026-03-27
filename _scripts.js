// Nav scroll
const nav = document.getElementById('main-nav');
if(nav) window.addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>40),{passive:true});

// Hamburger
const hb = document.getElementById('hamburger');
const mm = document.getElementById('mobile-menu');
if(hb) hb.addEventListener('click',()=>{const o=mm.classList.toggle('open');hb.classList.toggle('open',o);document.body.style.overflow=o?'hidden':''});
function closeMenu(){mm.classList.remove('open');hb.classList.remove('open');document.body.style.overflow=''}

// Industries dropdown — click based so it doesn't glitch
const dropdownWrap = document.querySelector('.nav-dropdown-wrap');
const dropdownBtn = document.querySelector('.nav-dropdown-btn');
if(dropdownBtn) {
  dropdownBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    dropdownWrap.classList.toggle('open');
  });
  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if(!dropdownWrap.contains(e.target)) {
      dropdownWrap.classList.remove('open');
    }
  });
  // Close when clicking a link inside dropdown
  document.querySelectorAll('.nav-dropdown a').forEach(link => {
    link.addEventListener('click', () => dropdownWrap.classList.remove('open'));
  });
}

// Reveal
document.querySelectorAll('.reveal').forEach(el=>{
  new IntersectionObserver(([e])=>{if(e.isIntersecting){el.classList.add('visible');e.target._obs&&e.target._obs.disconnect()}},{threshold:.1}).observe(el);
});

// Form
const form = document.getElementById('audit-form');
if(form) form.addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=form.querySelector('button[type="submit"]');
  btn.textContent='Sending...';btn.disabled=true;
  try{
    const res=await fetch(form.action,{method:'POST',body:new FormData(form),headers:{'Accept':'application/json'}});
    if(res.ok){document.getElementById('form-card').innerHTML='<div style="text-align:center;padding:3rem 1rem"><div style="width:3.5rem;height:3.5rem;border-radius:50%;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.3);display:flex;align-items:center;justify-content:center;margin:0 auto 1.5rem;font-size:1.4rem;color:#E8A020">✓</div><h3 style="font-size:1.5rem;font-weight:700;color:#F5F5F0;margin-bottom:.75rem">You\'re on the list.</h3><p style="color:#9A9890;line-height:1.7">We\'ll review your site and reach out within 24 hours with your free audit.</p></div>'}
    else{btn.textContent='Get My Free Audit';btn.disabled=false}
  }catch{btn.textContent='Get My Free Audit';btn.disabled=false}
});
