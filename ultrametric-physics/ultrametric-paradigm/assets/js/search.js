/* ═══════════════════════════════════════════════════════════════
   ULTRAMETRIC PARADIGM — Search Engine
   Precomputed search-data.json → in-memory index → results UI
   ═══════════════════════════════════════════════════════════════ */
(function(){
  'use strict';
  var $=function(s){return document.querySelector(s);};
  var $$=function(s){return document.querySelectorAll(s);};

  var searchIdx=[], searchLoaded=false, searchVis=false;
  var searchEl, inputEl, listEl;
  var DEBOUNCE_MS=300;

  function createUI(){
    searchEl=document.createElement('div');
    searchEl.className='search-results';
    searchEl.setAttribute('aria-live','polite');
    searchEl.setAttribute('aria-label','Search results');
    searchEl.innerHTML='<div class="search-results-header">Results</div><div class="search-results-list"></div>';
    document.body.appendChild(searchEl);
    listEl=searchEl.querySelector('.search-results-list');
    inputEl=$('#search-input');
    if(!inputEl)inputEl=$('.sidebar-search input');
  }

  function loadIndex(){
    if(searchLoaded)return;
    fetch('/ultrametric-paradigm/assets/search/search-data.json')
      .then(function(r){return r.json();})
      .then(function(data){
        searchIdx=data;
        searchLoaded=true;
        if(inputEl)inputEl.disabled=false;
        if(inputEl)inputEl.placeholder='Search… (Ctrl+K)';
      })
      .catch(function(){
        console.warn('Search index failed to load; using DOM fallback');
        buildFallbackIndex();
      });
  }

  function buildFallbackIndex(){
    var headings=$$('#main-content h2,#main-content h3');
    searchIdx=[];
    headings.forEach(function(h,i){
      if(!h.id){h.id='sect-'+i+'-'+h.tagName.toLowerCase();}
      var next=h.nextElementSibling;
      var content='';
      while(next&&next.tagName!=='H2'&&content.length<200){
        content+=(next.textContent||'')+' ';
        next=next.nextElementSibling;
      }
      searchIdx.push({
        id:h.id,
        title:h.textContent.trim(),
        content:content.trim().substring(0,200),
        url:'/ultrametric-paradigm/#'+h.id,
        level:h.tagName.toLowerCase()
      });
    });
    searchLoaded=true;
  }

  function tokenize(s){
    return s.toLowerCase().replace(/[^\w\s]/g,' ').split(/\s+/).filter(Boolean);
  }

  function search(q){
    var tokens=tokenize(q);
    var scored=searchIdx.map(function(item){
      var titleLower=item.title.toLowerCase();
      var contentLower=item.content.toLowerCase();
      var score=0;
      tokens.forEach(function(t){
        if(titleLower.indexOf(t)!==-1)score+=10;
        if(contentLower.indexOf(t)!==-1)score+=1;
      });
      return {item:item,score:score};
    }).filter(function(r){return r.score>0;})
      .sort(function(a,b){return b.score-a.score;})
      .slice(0,20);
    return scored;
  }

  function highlight(t,q){
    var tokens=tokenize(q);
    var result=t;
    tokens.forEach(function(tok){
      var re=new RegExp('('+tok.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi');
      result=result.replace(re,'<strong>$1</strong>');
    });
    return result;
  }

  function showResults(query){
    var results=search(query);
    listEl.innerHTML='';
    if(!results.length){
      listEl.innerHTML='<div class="search-result-item" style="color:var(--text3);justify-content:center">No matching sections</div>';
    }else{
      results.forEach(function(r,i){
        var relevance=Math.round((1-(i/results.length))*5);
        var bars='';
        for(var j=0;j<5;j++)bars+='<span style="opacity:'+(j<relevance?1:.2)+';height:'+(8+j*3)+'px"></span>';
        var a=document.createElement('a');
        a.className='search-result-item';
        a.href='#'+r.item.id;
        a.innerHTML='<span class="result-title">'+highlight(r.item.title,query)+'</span><span class="result-relevance">'+bars+'</span>';
        a.addEventListener('click',function(){
          hideResults();
          if(inputEl)inputEl.value='';
        });
        listEl.appendChild(a);
      });
    }
    searchEl.classList.add('visible');
    searchVis=true;
  }

  function hideResults(){
    searchEl.classList.remove('visible');
    searchVis=false;
  }

  var debounceTimer;
  function debounce(fn,ms){
    return function(){
      var args=arguments,ctx=this;
      clearTimeout(debounceTimer);
      debounceTimer=setTimeout(function(){fn.apply(ctx,args);},ms);
    };
  }

  function init(){
    createUI();
    loadIndex();

    if(inputEl){
      inputEl.disabled=true;
      inputEl.placeholder='Loading search index…';
      inputEl.addEventListener('input',debounce(function(e){
        var q=e.target.value.trim();
        if(q.length<2){hideResults();return;}
        if(!searchLoaded){loadIndex();return;}
        showResults(q);
      },DEBOUNCE_MS));
    }

    document.addEventListener('keydown',function(e){
      if((e.ctrlKey||e.metaKey)&&e.key==='k'){
        e.preventDefault();
        if(inputEl)inputEl.focus();
      }
      if(e.key==='Escape'&&searchVis){
        hideResults();
        if(inputEl)inputEl.blur();
      }
      if(searchVis){
        var items=$$('.search-result-item');
        var active=searchEl.querySelector('.search-result-item.active');
        if(e.key==='ArrowDown'){
          e.preventDefault();
          if(!active){items[0]&&items[0].classList.add('active');}
          else{active.classList.remove('active');var next=active.nextElementSibling;if(next)next.classList.add('active');}
        }
        if(e.key==='ArrowUp'){
          e.preventDefault();
          if(!active){items[items.length-1]&&items[items.length-1].classList.add('active');}
          else{active.classList.remove('active');var prev=active.previousElementSibling;if(prev)prev.classList.add('active');}
        }
        if(e.key==='Enter'&&active){
          e.preventDefault();
          active.click();
        }
      }
    });

    document.addEventListener('click',function(e){
      if(searchVis&&!searchEl.contains(e.target)&&!e.target.closest('.sidebar-search')){
        hideResults();
      }
    });
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
