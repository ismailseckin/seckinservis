/* ============================================================
   SEÇKIN SERVİS - JavaScript
   ============================================================ */

// ── NAVBAR SCROLL ──────────────────────────────────────────
const navbar = document.getElementById('navbar');
const onScroll = () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// ── HAMBURGER / MOBILE NAV ──────────────────────────────────
const hamburger  = document.getElementById('hamburger');
const mobileNav  = document.getElementById('mobileNav');
const mobileClose = document.getElementById('mobileClose');
const mobileLinks = document.querySelectorAll('.mobile-link');

const openNav  = () => { mobileNav.classList.add('open');  hamburger.classList.add('active');    document.body.style.overflow = 'hidden'; };
const closeNav = () => { mobileNav.classList.remove('open'); hamburger.classList.remove('active'); document.body.style.overflow = ''; };

hamburger.addEventListener('click', () => mobileNav.classList.contains('open') ? closeNav() : openNav());
mobileClose.addEventListener('click', closeNav);
mobileLinks.forEach(l => l.addEventListener('click', closeNav));

// ── SMOOTH SCROLL ───────────────────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const offset = 72;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ── INTERSECTION OBSERVER – Fade-Up ───────────────────────
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// ── CONTACT FORM ────────────────────────────────────────────
const form    = document.getElementById('contactForm');
const success = document.getElementById('formSuccess');
const submitBtn = document.getElementById('form-submit');

form.addEventListener('submit', e => {
  e.preventDefault();

  // Simple validation
  const name    = document.getElementById('name').value.trim();
  const phone   = document.getElementById('phone').value.trim();
  const service = document.getElementById('service').value;

  if (!name || !phone || !service) {
    shakeForm();
    return;
  }

  // Simulate sending (replace with actual backend/email service)
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<span>⏳</span> Gönderiliyor...';

  setTimeout(() => {
    form.style.opacity = '0';
    form.style.transform = 'translateY(-10px)';
    form.style.transition = 'opacity 0.4s, transform 0.4s';
    setTimeout(() => {
      form.style.display = 'none';
      success.style.display = 'block';
      success.style.animation = 'fadeIn 0.5s ease forwards';
    }, 400);
  }, 1400);
});

function shakeForm() {
  const wrap = document.querySelector('.contact-form-wrap');
  wrap.style.animation = 'shake 0.4s ease';
  setTimeout(() => wrap.style.animation = '', 400);
}

// ── COUNTER ANIMATION ───────────────────────────────────────
function animateCounter(el, target, suffix = '') {
  let start = 0;
  const duration = 1800;
  const step = (timestamp) => {
    if (!start) start = timestamp;
    const progress = Math.min((timestamp - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    el.textContent = Math.floor(eased * target) + suffix;
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

const statNums = document.querySelectorAll('.hero-stat-num');
let statsAnimated = false;

const statsObserver = new IntersectionObserver(entries => {
  if (entries[0].isIntersecting && !statsAnimated) {
    statsAnimated = true;
    const data = [
      { el: statNums[0], target: 500, suffix: '+' },
      { el: statNums[1], target: 100, suffix: '+' },
    ];
    // 7/24 is static text, no animation needed
    data.forEach(d => animateCounter(d.el, d.target, d.suffix));
  }
}, { threshold: 0.5 });

if (statNums[0]) statsObserver.observe(statNums[0].closest('.hero-stats'));

// ── ACTIVE NAV LINK ─────────────────────────────────────────
const sections = document.querySelectorAll('section[id], div[id]');
const navLinks  = document.querySelectorAll('.nav-links a');

const activeLinkObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute('id');
      navLinks.forEach(link => {
        link.classList.remove('active-link');
        if (link.getAttribute('href') === `#${id}`) {
          link.classList.add('active-link');
        }
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => activeLinkObserver.observe(s));

// CSS injection for dynamic styles
const dynamicCSS = document.createElement('style');
dynamicCSS.textContent = `
  @keyframes shake {
    0%,100% { transform: translateX(0); }
    20%,60%  { transform: translateX(-8px); }
    40%,80%  { transform: translateX(8px); }
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .nav-links a.active-link { color: #ffffff !important; }
  .nav-links a.active-link::after { width: 100% !important; }
`;
document.head.appendChild(dynamicCSS);
