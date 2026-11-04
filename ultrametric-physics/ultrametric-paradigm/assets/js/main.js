/* ═══════════════════════════════════════════════════════════════
   ULTRAMETRIC PARADIGM — Content-Driven Interactive Engine
   v0.9.2 — FAB, precomputed sidebar.json, separate search.js
   ═══════════════════════════════════════════════════════════════ */
(function(){
  'use strict';
  var $=function(s){return document.querySelector(s);};
  var $$=function(s){return document.querySelectorAll(s);};
  var NAV=$('#sidebar-nav'),MAIN=$('#main-content'),SIDEBAR=$('#sidebar');
  var OVERLAY=$('.sidebar-overlay'),PROGRESS=$('#progress-bar'),FAB=$('#fab');
  var SCROLL_OFFSET=80;
  var tocs=[];

  /* ── Theme ──────────────────────────────────────── */
  function setThemeUI(theme){
    document.documentElement.setAttribute('data-theme',theme);
    $$('.theme-toggle,.theme-toggle-mobile,#fab').forEach(function(b){
      if(b===FAB){b.setAttribute('data-theme-icon',theme==='dark'?'☀️':'🌙');return;}
      b.textContent=theme==='dark'?'☀️':'🌙';
    });
  }

  function toggleTheme(){
    var next=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
    localStorage.setItem('theme',next);
    setThemeUI(next);
  }

  /* ── Sidebar Nav Builder (JSON-first, DOM-fallback) ─ */
  function buildSidebarFromJSON(data){
    var frag=document.createDocumentFragment();
    data.forEach(function(item){
      var link=document.createElement('a');
      link.href='#'+item.id;
      link.textContent=item.title.length>80?item.title.substring(0,77)+'…':item.title;
      link.setAttribute('data-id',item.id);
      if(item.level==='h1')link.className='nav-h1';
      if(item.level==='h2')link.className='nav-h2';
      if(item.level==='h3'){link.className='nav-h3';link.style.paddingLeft='3rem';link.style.fontSize='.75rem';link.style.opacity='.8';}
      frag.appendChild(link);
      tocs.push({id:item.id,text:item.title,tag:item.level});
    });
    NAV.innerHTML='';
    NAV.appendChild(frag);
    finishSidebarInit();
  }

  function buildSidebarFromDOM(){
    var headings=$$('#main-content h1,#main-content h2,#main-content h3');
    var frag=document.createDocumentFragment();
    headings.forEach(function(h,i){
      if(!h.id){h.id='sect-'+i+'-'+h.tagName.toLowerCase();}
      var tag=h.tagName.toLowerCase();
      var link=document.createElement('a');
      link.href='#'+h.id;
      link.textContent=h.textContent.trim().substring(0,80);
      link.setAttribute('data-id',h.id);
      if(tag==='h1')link.className='nav-h1';
      if(tag==='h2')link.className='nav-h2';
      if(tag==='h3'){link.className='nav-h3';link.style.paddingLeft='3rem';link.style.fontSize='.75rem';link.style.opacity='.8';}
      frag.appendChild(link);
      tocs.push({id:h.id,text:h.textContent.trim(),tag:tag});
    });
    NAV.innerHTML='';
    NAV.appendChild(frag);
    finishSidebarInit();
  }

  function finishSidebarInit(){
    window.__toc=tocs;
    var skeleton=NAV.querySelector('.skeleton-nav');
    if(skeleton)skeleton.style.display='none';
    var read=new Set(JSON.parse(localStorage.getItem('read-sections')||'[]'));
    read.forEach(function(id){
      var link=NAV.querySelector('a[data-id="'+id+'"]');
      if(link)link.classList.add('read');
    });
  }

  function buildSidebar(){
    fetch('/ultrametric-paradigm/assets/js/nav/sidebar.json')
      .then(function(r){return r.json();})
      .then(function(data){
        if(data&&data.length)buildSidebarFromJSON(data);
        else buildSidebarFromDOM();
      })
      .catch(function(){
        console.warn('sidebar.json not found, building from DOM');
        buildSidebarFromDOM();
      });
  }

  /* ── Active Heading (IntersectionObserver) ──────── */
  function initActiveObserver(){
    if(!('IntersectionObserver' in window))return;
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          var id=e.target.id;
          $$('#sidebar-nav a').forEach(function(a){
            a.classList.toggle('active',a.getAttribute('data-id')===id);
          });
        }
      });
    },{rootMargin:'-'+SCROLL_OFFSET+'px 0px -60% 0px'});

    $$('#main-content h2').forEach(function(h){
      if(!h.id){h.id='sect-'+Math.random().toString(36).substr(2,8)+'-h2';}
      observer.observe(h);
    });
  }

  /* ── Progress Bar ───────────────────────────────── */
  function updateProgress(){
    if(!PROGRESS)return;
    var pct=Math.min((window.scrollY/(document.documentElement.scrollHeight-window.innerHeight))*100,100);
    PROGRESS.style.width=pct+'%';
  }

  /* ── Mobile ─────────────────────────────────────── */
  function initMobile(){
    var menuToggle=$('.menu-toggle');
    if(menuToggle){
      menuToggle.addEventListener('click',function(){
        SIDEBAR.classList.toggle('open');
        if(OVERLAY)OVERLAY.classList.toggle('visible');
      });
    }
    if(OVERLAY){
      OVERLAY.addEventListener('click',function(){
        SIDEBAR.classList.remove('open');
        OVERLAY.classList.remove('visible');
      });
    }
    $$('#sidebar-nav a').forEach(function(a){
      a.addEventListener('click',function(){
        if(window.innerWidth<=1024){
          SIDEBAR.classList.remove('open');
          if(OVERLAY)OVERLAY.classList.remove('visible');
        }
      });
    });
  }

  /* ── Collapsible Sections ───────────────────────── */
  function initCollapse(){
    $$('#main-content h2').forEach(function(h2){
      if(/CONTENTS|HOW TO READ|READING PATHWAYS|CONCEPT MAP|NOTATION|HISTORICAL|PROLOGUE|ABSTRACT|QUICK REFERENCE|CHAPTER TRANSITION|INDEX|FURTHER READING|GLOSSARY|VERSION HISTORY/i.test(h2.textContent))return;
      h2.style.cursor='pointer';
      h2.setAttribute('data-collapsed','false');
      h2.setAttribute('aria-expanded','true');
      var icon=document.createElement('span');
      icon.style.cssText='font-size:.7em;color:var(--accent);margin-left:.3em';
      icon.textContent='▾';
      h2.appendChild(icon);
      h2.addEventListener('click',function(){
        var c=h2.getAttribute('data-collapsed')==='true';
        h2.setAttribute('data-collapsed',String(!c));
        h2.setAttribute('aria-expanded',String(c));
        var n=h2.nextElementSibling;
        while(n&&n.tagName!=='H2'){
          n.style.display=c?'':'none';
          n=n.nextElementSibling;
        }
        icon.textContent=c?'▾':'▸';
      });
    });
  }

  /* ── Floating Action Button (scroll-to-top + theme) ─ */
  function initFAB(){
    if(!FAB)return;
    var pressTimer,longPress=false;
    var updateVis=function(){FAB.classList.toggle('visible',window.scrollY>600);};
    addEventListener('scroll',updateVis);

    FAB.addEventListener('click',function(e){
      if(longPress){longPress=false;return;}
      window.scrollTo({top:0,behavior:'smooth'});
    });

    FAB.addEventListener('mousedown',function(){
      longPress=false;
      pressTimer=setTimeout(function(){longPress=true;toggleTheme();},500);
    });
    FAB.addEventListener('mouseup',function(){clearTimeout(pressTimer);});
    FAB.addEventListener('mouseleave',function(){clearTimeout(pressTimer);});
    FAB.addEventListener('touchstart',function(e){
      longPress=false;
      pressTimer=setTimeout(function(){longPress=true;toggleTheme();},500);
    });
    FAB.addEventListener('touchend',function(){clearTimeout(pressTimer);});
    FAB.addEventListener('touchmove',function(){clearTimeout(pressTimer);});

    updateVis();
  }

  /* ── Smooth Scroll ──────────────────────────────── */
  function initSmoothScroll(){
    document.addEventListener('click',function(e){
      var link=e.target.closest('a[href^="#"]');
      if(!link||link.classList.contains('search-result-item'))return;
      var id=link.getAttribute('href').substring(1);
      var el=document.getElementById(id);
      if(el){
        e.preventDefault();
        window.scrollTo({top:el.getBoundingClientRect().top+window.scrollY-SCROLL_OFFSET,behavior:'smooth'});
        history.pushState(null,null,'#'+id);
      }
    });
  }

  /* ── Section Anchors ────────────────────────────── */
  function initSectionAnchors(){
    $$('#main-content h2,#main-content h3,#main-content h4').forEach(function(h){
      var a=document.createElement('a');
      a.className='section-anchor';
      a.href='#'+h.id;
      a.textContent='#';
      a.title='Copy link to this section';
      a.setAttribute('aria-label','Copy link to this section');
      a.addEventListener('click',function(e){
        e.preventDefault();
        navigator.clipboard.writeText(window.location.href.split('#')[0]+'#'+h.id).then(function(){
          a.textContent='✓';
          a.classList.add('copied');
          setTimeout(function(){a.textContent='#';a.classList.remove('copied');},1500);
        }).catch(function(){});
      });
      h.appendChild(a);
    });
  }

  /* ── Reading Time ───────────────────────────────── */
  function initReadingTime(){
    var text=document.getElementById('main-content');
    if(!text)return;
    var words=text.textContent.split(/\s+/).length;
    var mins=Math.max(1,Math.round(words/200));
    $$('.reading-time').forEach(function(el){el.textContent='~'+mins+' min read';});
    document.querySelectorAll('.proof-toggle span').forEach(function(span){
      var wc=0,n=span.closest('.proof-block');
      if(!n)return;
      var body=n.querySelector('.proof-body');
      if(body)wc=body.textContent.split(/\s+/).length;
      var t=Math.max(1,Math.round(wc/200));
      span.textContent='~'+t+' min read';
    });
  }

  /* ═══════════════════════════════════════════════════
     CONTENT-AWARE ENHANCEMENTS
     Read the DOM, identify content types, enhance.
     ═══════════════════════════════════════════════════ */

  /* ── Glossary Tooltips ──────────────────────────── */
  var glossary={};
  function buildGlossaryIndex(){
    var terms=['Adele ring','Archimedean metric','Bruhat–Tits tree','Container','Monna projection',
      'Projection artifact','Shift metric','Stabilizer code','Threshold principle','Tree automorphism',
      'Ultrametric','Basin-crossing','Holographic principle','Product formula','Scrambling',
      'Born rule','Decoherence','Riemann Hypothesis','Langlands program','Automorphic form',
      'Measurement problem','Ball-inclusion tree','Lorentz symmetry','Adelic space','Coarse-graining'];
    var text=document.getElementById('main-content');
    if(!text)return;
    text=text.textContent;
    var defs={};
    terms.forEach(function(term){
      var defStart=text.indexOf(term);
      if(defStart===-1)return;
      var defEnd=text.indexOf('.',defStart+term.length);
      if(defEnd===-1)defEnd=defStart+term.length+200;
      var snippet=text.substring(defStart,Math.min(defEnd+1,defStart+300)).trim();
      glossary[term.toLowerCase()]=snippet;
    });
  }

  function applyGlossaryTooltips(){
    buildGlossaryIndex();
    Object.keys(glossary).forEach(function(term){
      var lower=term.toLowerCase();
      document.querySelectorAll('#main-content p,#main-content li,#main-content td').forEach(function(el){
        if(el.querySelector('.glossary-term, mjx-container'))return;
        var html=el.innerHTML;
        var idx=html.toLowerCase().indexOf(lower);
        if(idx!==-1&&!html.substring(Math.max(0,idx-1),idx).match(/[a-z]/i)){
          var before=html.substring(0,idx);
          var match=html.substring(idx,idx+term.length);
          var after=html.substring(idx+term.length);
          el.innerHTML=before+'<span class="glossary-term" data-term="'+term+'">'+match+'</span>'+after;
        }
      });
    });
    document.querySelectorAll('.glossary-term').forEach(function(el){
      el.addEventListener('mouseenter',function(){
        var tip=document.createElement('div');
        tip.className='glossary-tooltip visible';
        tip.textContent=(glossary[el.getAttribute('data-term').toLowerCase()]||'Defined term — see Glossary').substring(0,250)+'…';
        el.appendChild(tip);
        el.addEventListener('mouseleave',function(){if(tip.parentNode)tip.parentNode.removeChild(tip);},{once:true});
      });
    });
  }

  /* ── Proof Collapsibility ───────────────────────── */
  function applyProofCollapse(){
    $$('#main-content p,#main-content div').forEach(function(el){
      if(el.classList.contains('proof-block'))return;
      var text=el.textContent||'';
      if(text.trim().match(/^Proof\.\s/)&&!el.closest('.proof-block')){
        var proofDiv=document.createElement('div');
        proofDiv.className='proof-block';
        var btn=document.createElement('button');
        btn.className='proof-toggle';
        btn.setAttribute('aria-expanded','false');
        var wc=0,n=el;
        while(n&&!n.textContent.match(/□/)){wc+=n.textContent.length;n=n.nextElementSibling;}
        var readTime=Math.max(1,Math.round(wc/200));
        btn.innerHTML='Proof <span style="font-size:.75em;color:var(--text3);margin-left:.5em">~'+readTime+' min read</span>';
        var body=document.createElement('div');
        body.className='proof-body';
        btn.addEventListener('click',function(){
          var open=body.classList.toggle('open');
          btn.classList.toggle('open',open);
          btn.setAttribute('aria-expanded',String(open));
          if(open&&window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([body]);
        });
        proofDiv.appendChild(btn);
        proofDiv.appendChild(body);
        el.parentNode.insertBefore(proofDiv,el);
        body.appendChild(el);
        var next=el.nextElementSibling;
        while(next&&(next.textContent||'').indexOf('□')===-1&&!next.matches('h1,h2,h3,h4')){
          var n2=next.nextElementSibling;
          body.appendChild(next);
          next=n2;
        }
        if(next&&(next.textContent||'').indexOf('□')!==-1)body.appendChild(next);
      }
    });
  }

  /* ── Diagram Zoom ───────────────────────────────── */
  function applyDiagramZoom(){
    $$('pre.diagram,pre:has(code)').forEach(function(pre){
      var code=pre.querySelector('code');
      if(!code)return;
      var text=code.textContent||'';
      if(/[┌┐└┘├┤┬┴┼│─═╔╗╚╝║╠╣╦╩╬▶▼▲◀◆◇○●□■☆★↑↓→←↗↘↙↖]/.test(text)&&text.split('\n').length>3){
        pre.classList.add('diagram');
        pre.addEventListener('click',function(e){
          if(e.target.closest('a'))return;
          pre.classList.toggle('zoomed');
        });
      }
    });
  }

  /* ── Equation Modal ─────────────────────────────── */
  function applyEquationModals(){
    var modal=document.createElement('div');
    modal.className='equation-modal';
    modal.setAttribute('role','dialog');
    modal.setAttribute('aria-label','Equation viewer');
    modal.innerHTML='<div class="equation-modal-content"></div><button class="equation-modal-close" aria-label="Close">×</button>';
    document.body.appendChild(modal);
    modal.querySelector('.equation-modal-close').addEventListener('click',function(){modal.classList.remove('visible');});
    modal.addEventListener('click',function(e){if(e.target===modal)modal.classList.remove('visible');});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')modal.classList.remove('visible');});

    /* Wait for MathJax to process, then attach click handlers */
    var attempts=0;
    var attach=function(){
      var eqs=document.querySelectorAll('.MathJax_Display, mjx-container[mjx-display="true"]');
      if(eqs.length>0||attempts>20){
        eqs.forEach(function(eq){
          eq.style.cursor='pointer';
          eq.addEventListener('click',function(){
            var clone=eq.cloneNode(true);
            clone.style.fontSize='1.3em';
            modal.querySelector('.equation-modal-content').innerHTML='';
            modal.querySelector('.equation-modal-content').appendChild(clone);
            modal.classList.add('visible');
            if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([modal]);
          });
        });
        return;
      }
      attempts++;
      setTimeout(attach,500);
    };
    setTimeout(attach,2000);
  }

  /* ── Image Lightbox ─────────────────────────────── */
  function initImageLightbox(){
    var box=document.createElement('div');
    box.className='lightbox';
    box.setAttribute('role','dialog');
    box.setAttribute('aria-label','Image viewer');
    box.innerHTML='<img class="lightbox-content" alt=""><button class="lightbox-close" aria-label="Close">×</button>';
    document.body.appendChild(box);
    box.querySelector('.lightbox-close').addEventListener('click',function(){box.classList.remove('visible');});
    box.addEventListener('click',function(e){if(e.target===box)box.classList.remove('visible');});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')box.classList.remove('visible');});
    document.addEventListener('click',function(e){
      var img=e.target.closest('.main-content img');
      if(!img||img.closest('.lightbox')||img.closest('.equation-modal'))return;
      var src=img.getAttribute('src')||img.getAttribute('data-src');
      if(!src)return;
      e.preventDefault();
      box.querySelector('.lightbox-content').setAttribute('src',src);
      box.classList.add('visible');
    });
  }

  /* ── Section Read Tracking ──────────────────────── */
  function applyReadTracking(){
    var read=new Set(JSON.parse(localStorage.getItem('read-sections')||'[]'));
    if(!('IntersectionObserver' in window))return;
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          var h=e.target.closest('h2');
          if(h&&h.id){
            read.add(h.id);
            localStorage.setItem('read-sections',JSON.stringify([...read]));
            var link=NAV.querySelector('a[data-id="'+h.id+'"]');
            if(link)link.classList.add('read');
          }
        }
      });
    },{threshold:0.5});
    $$('#main-content h2').forEach(function(h){observer.observe(h);});
    read.forEach(function(id){
      var link=NAV.querySelector('a[data-id="'+id+'"]');
      if(link)link.classList.add('read');
    });
  }

  /* ── Fragment Highlight ─────────────────────────── */
  function initFragmentHighlight(){
    var hash=window.location.hash;
    if(!hash)return;
    setTimeout(function(){
      var el=document.querySelector(hash);
      if(el){el.scrollIntoView();window.scrollBy(0,-SCROLL_OFFSET);}
    },300);
    addEventListener('hashchange',function(){
      var h=window.location.hash;
      if(h){var el=document.querySelector(h);if(el){el.scrollIntoView();window.scrollBy(0,-SCROLL_OFFSET);}}
    });
  }

  /* ── Page TOC Builder ──────────────────────────── */
  function buildPageTOC(){
    var tocList=$('#toc-list');
    if(!tocList)return;
    $$('#main-content h2').forEach(function(h,i){
      if(!h.id){h.id='toc-'+i;}
      var li=document.createElement('li');
      var a=document.createElement('a');
      a.href='#'+h.id;
      a.textContent=h.textContent.trim().substring(0,80);
      li.appendChild(a);
      tocList.appendChild(li);
    });
    /* Track active TOC item */
    if('IntersectionObserver' in window){
      var tocObserver=new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          var link=tocList.querySelector('a[href="#'+e.target.id+'"]');
          if(link)link.classList.toggle('active',e.isIntersecting);
        });
      },{rootMargin:'-80px 0px -60% 0px'});
      $$('#main-content h2').forEach(function(h){tocObserver.observe(h);});
    }
  }

  /* ── Boot ───────────────────────────────────────── */
  function init(){
    buildSidebar();
    initMobile();
    initCollapse();
    initFAB();
    initSmoothScroll();
    initSectionAnchors();
    initFragmentHighlight();
    initImageLightbox();
    initActiveObserver();
    initReadingTime();
    buildPageTOC();

    /* Scroll loop */
    var ticking=false;
    addEventListener('scroll',function(){
      if(!ticking){
        requestAnimationFrame(function(){updateProgress();ticking=false;});
        ticking=true;
      }
    });

    /* Theme buttons (legacy + mobile) */
    $$('.theme-toggle,.theme-toggle-mobile').forEach(function(b){
      b.addEventListener('click',toggleTheme);
    });

    /* Content-aware enhancements (deferred for performance) */
    setTimeout(function(){
      applyProofCollapse();
      applyDiagramZoom();
      applyReadTracking();
    },500);
    setTimeout(function(){
      applyGlossaryTooltips();
    },1000);
    setTimeout(function(){
      applyEquationModals();
    },2000);

    /* Initial state */
    updateProgress();
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
