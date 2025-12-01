document.addEventListener('DOMContentLoaded', () => {
  const toggle1 = document.querySelector('.userf');
  const toggle2 = document.querySelector('.nouserf');
  const menu = document.querySelector('.dropdown-menu');

  toggle1.addEventListener('click', (e) => {
    e.preventDefault();
    menu.classList.toggle('show');
  });

  toggle2.addEventListener('click', (e) => {
    e.preventDefault();
    menu.classList.toggle('show');
  });

  document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown')) {
      menu.classList.remove('show');
    }
  });
});