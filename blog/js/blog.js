/**
 * Blog Components Loader
 * Kinetic Energy - Modular Blog System
 */

// Load HTML components
async function loadComponent(elementId, componentPath) {
  const element = document.getElementById(elementId);
  if (!element) return;

  try {
    const response = await fetch(componentPath);
    if (response.ok) {
      element.innerHTML = await response.text();
    }
  } catch (error) {
    console.error(`Error loading component ${componentPath}:`, error);
  }
}

// Initialize all components
async function initComponents() {
  await Promise.all([
    loadComponent('nav-component', 'components/nav.html'),
    loadComponent('footer-component', 'components/footer.html'),
    loadComponent('floating-buttons-component', 'components/floating-buttons.html')
  ]);

  // Initialize functionality after components are loaded
  initNavigation();
  initScrollTop();
}

// Mobile navigation functionality
function initNavigation() {
  const hamburgerBtn = document.getElementById('hamburger-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (!hamburgerBtn || !mobileMenu) return;

  const hamburgerIcon = hamburgerBtn.querySelector('.hamburger-icon');

  hamburgerBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    hamburgerIcon.classList.toggle('rotate');
    hamburgerIcon.textContent = mobileMenu.classList.contains('open') ? 'close' : 'menu';
  });

  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      hamburgerIcon.classList.remove('rotate');
      hamburgerIcon.textContent = 'menu';
    });
  });
}

// Scroll to top functionality
function initScrollTop() {
  const scrollTopBtn = document.getElementById('scroll-top-btn');

  if (!scrollTopBtn) return;

  window.addEventListener('scroll', () => {
    scrollTopBtn.classList.toggle('visible', window.scrollY > 500);
  });

  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initComponents);
