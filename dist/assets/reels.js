/* Continuous, touch-friendly rails. Originals remain available without JavaScript. */
(() => {
  'use strict';
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  let keyboardInput = true;
  document.addEventListener('keydown', () => { keyboardInput = true; }, {capture:true});
  document.addEventListener('pointerdown', () => { keyboardInput = false; }, {capture:true, passive:true});
  document.addEventListener('touchstart', () => { keyboardInput = false; }, {capture:true, passive:true});
  const RESUME_DELAY = 2400;
  const mod = (value, length) => ((value % length) + length) % length;

  document.querySelectorAll('[data-reel]').forEach(reel => {
    const viewport = reel.querySelector('.reel-window');
    const track = reel.querySelector('.reel-track');
    const original = reel.querySelector('.reel-group:not([data-reel-copy])');
    if (!viewport || !track || !original) return;

    const speed = Math.max(1, Number(reel.dataset.speed) || 28);
    // Increasing scrollLeft moves the artwork left; the second row travels right.
    const direction = reel.dataset.direction === 'right' ? -1 : 1;
    let cycle = 0, base = 0, position = 0, frame = 0, last = 0;
    let measureFrame = 0, resumeTimer = 0, manualUntil = 0;
    let visible = !('IntersectionObserver' in window);
    let hovered = false, keyboardFocused = false, pointerActive = false, touchActive = false;
    let dragging = false, activePointer = null, pointerStart = 0, scrollStart = 0;

    function shouldRun() {
      return cycle > 0 && visible && !motion.matches && !document.hidden &&
        !hovered && !keyboardFocused && !pointerActive && !touchActive &&
        performance.now() >= manualUntil;
    }

    function writePosition(value) {
      position = value;
      viewport.scrollLeft = value;
    }

    function centered(value) {
      return base + mod(value - base, cycle);
    }

    function tick(now) {
      frame = 0;
      if (!shouldRun()) { last = 0; return; }
      if (last) {
        const delta = speed * Math.min(now - last, 40) / 1000 * direction;
        writePosition(centered(position + delta));
      }
      last = now;
      frame = requestAnimationFrame(tick);
    }

    function update() {
      if (shouldRun()) {
        if (!frame) {
          // Return to the middle copy, preserving exactly the visible logo position.
          writePosition(centered(viewport.scrollLeft));
          last = 0;
          frame = requestAnimationFrame(tick);
        }
      } else if (frame) {
        cancelAnimationFrame(frame);
        frame = 0;
        last = 0;
      }
    }

    function allowManualScroll() {
      manualUntil = performance.now() + RESUME_DELAY;
      clearTimeout(resumeTimer);
      resumeTimer = setTimeout(() => {
        resumeTimer = 0;
        update();
      }, RESUME_DELAY + 20);
      update();
    }

    function cloneGroup() {
      const copy = original.cloneNode(true);
      copy.dataset.reelCopy = '';
      copy.setAttribute('aria-hidden', 'true');
      copy.setAttribute('inert', '');
      copy.removeAttribute('role');
      copy.removeAttribute('id');
      copy.querySelectorAll('[id]').forEach(el => el.removeAttribute('id'));
      copy.querySelectorAll('a,button,input,select,textarea,[tabindex]').forEach(el => el.setAttribute('tabindex', '-1'));
      copy.querySelectorAll('img').forEach(img => { img.draggable = false; });
      return copy;
    }

    function measure() {
      const phase = cycle > 0 ? mod(viewport.scrollLeft - base, cycle) / cycle : 0;
      track.querySelectorAll('[data-reel-copy]').forEach(copy => copy.remove());
      cycle = original.getBoundingClientRect().width;
      base = 0;
      if (!motion.matches && cycle > 0) {
        // Copies on both sides leave room for a swipe in either direction.
        const copies = Math.min(12, Math.max(2, Math.ceil(viewport.clientWidth / cycle) + 1));
        const before = document.createDocumentFragment();
        const after = document.createDocumentFragment();
        for (let i = 0; i < copies; i++) {
          before.appendChild(cloneGroup());
          after.appendChild(cloneGroup());
        }
        track.insertBefore(before, original);
        track.appendChild(after);
        base = copies * cycle;
      }
      writePosition(base + phase * cycle);
      update();
    }

    function scheduleMeasure() {
      if (measureFrame) return;
      measureFrame = requestAnimationFrame(() => { measureFrame = 0; measure(); });
    }

    function manualStep(sign) {
      allowManualScroll();
      const first = original.firstElementChild;
      const gap = parseFloat(getComputedStyle(original).columnGap || getComputedStyle(original).gap) || 24;
      const step = first ? first.getBoundingClientRect().width + gap : viewport.clientWidth * .8;
      if (!motion.matches && cycle > 0) writePosition(centered(viewport.scrollLeft));
      viewport.scrollTo({left: viewport.scrollLeft + sign * step, behavior: motion.matches ? 'instant' : 'smooth'});
    }

    viewport.addEventListener('mouseenter', () => { hovered = finePointer.matches; update(); });
    viewport.addEventListener('mouseleave', () => { hovered = false; update(); });
    viewport.addEventListener('focusin', () => {
      // Touch/click focus must not permanently stop a rail after the finger leaves.
      keyboardFocused = keyboardInput && (viewport.matches(':focus-visible') || !!viewport.querySelector(':focus-visible'));
      update();
    });
    viewport.addEventListener('focusout', () => {
      queueMicrotask(() => {
        if (!viewport.contains(document.activeElement)) keyboardFocused = false;
        update();
      });
    });
    viewport.addEventListener('keydown', event => {
      keyboardFocused = true;
      update();
      if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
        event.preventDefault();
        manualStep(event.key === 'ArrowRight' ? 1 : -1);
      }
    });

    viewport.addEventListener('pointerdown', event => {
      if (event.pointerType === 'mouse' && event.button !== 0) return;
      pointerActive = true;
      keyboardFocused = false;
      activePointer = event.pointerId;
      allowManualScroll();
      if (event.pointerType === 'mouse' && !event.target.closest('a,button,input,select,textarea')) {
        event.preventDefault();
        dragging = true;
        pointerStart = event.clientX;
        scrollStart = viewport.scrollLeft;
        viewport.setPointerCapture?.(event.pointerId);
        reel.classList.add('is-dragging');
      }
    });
    viewport.addEventListener('pointermove', event => {
      if (!dragging || event.pointerId !== activePointer) return;
      event.preventDefault();
      writePosition(scrollStart + pointerStart - event.clientX);
    });
    function endPointer(event) {
      if (activePointer === null || (event.pointerId !== undefined && event.pointerId !== activePointer)) return;
      pointerActive = false;
      dragging = false;
      activePointer = null;
      reel.classList.remove('is-dragging');
      allowManualScroll();
    }
    window.addEventListener('pointerup', endPointer);
    viewport.addEventListener('pointercancel', endPointer);
    viewport.addEventListener('lostpointercapture', endPointer);

    // Native panning can cancel pointer events; touch lifecycle still tracks a held finger.
    viewport.addEventListener('touchstart', () => {
      touchActive = true;
      keyboardFocused = false;
      allowManualScroll();
    }, {passive:true});
    function endTouch(event) {
      if (!touchActive || event.touches.length) return;
      touchActive = false;
      pointerActive = false;
      activePointer = null;
      allowManualScroll();
    }
    window.addEventListener('touchend', endTouch, {passive:true});
    window.addEventListener('touchcancel', endTouch, {passive:true});
    viewport.addEventListener('wheel', event => {
      if (Math.abs(event.deltaX) > Math.abs(event.deltaY) || event.shiftKey) allowManualScroll();
    }, {passive:true});
    viewport.addEventListener('scroll', () => {
      // Automatic writes match position. Only a user/browser scroll renews the idle delay.
      if (Math.abs(viewport.scrollLeft - position) > 2) {
        position = viewport.scrollLeft;
        allowManualScroll();
      }
    }, {passive:true});

    // Optional arrows remain supported for future content, but no pause UI is required.
    reel.querySelector('[data-reel-prev]')?.addEventListener('click', () => manualStep(-1));
    reel.querySelector('[data-reel-next]')?.addEventListener('click', () => manualStep(1));
    document.addEventListener('visibilitychange', update);
    const changeMotion = () => {
      clearTimeout(resumeTimer);
      manualUntil = 0;
      measure();
    };
    if (motion.addEventListener) motion.addEventListener('change', changeMotion);
    else motion.addListener(changeMotion);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(entries => {
        visible = entries[0].isIntersecting;
        reel.classList.toggle('is-offscreen', !visible);
        update();
      }, {threshold:.08}).observe(reel);
    }
    if ('ResizeObserver' in window) {
      let width = -1;
      new ResizeObserver(() => {
        if (Math.abs(viewport.clientWidth - width) > 1) {
          width = viewport.clientWidth;
          scheduleMeasure();
        }
      }).observe(viewport);
    } else window.addEventListener('resize', scheduleMeasure, {passive:true});
    original.querySelectorAll('img').forEach(img => {
      img.draggable = false;
      img.addEventListener('load', scheduleMeasure, {once:true});
    });
    document.fonts?.ready.then(scheduleMeasure);
    reel.classList.add('reel-ready');
    measure();
  });
})();
