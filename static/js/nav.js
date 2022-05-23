let nav = document.querySelector('nav');
let bgColor = document.getElementsByClassName('dropdown-menu')


window.addEventListener('scroll', function () {
  if (window.pageYOffset > 350) {
    nav.classList.add('bg-dark', 'shadow');
    for (let i = 0; i < bgColor.length; i++) {
      bgColor[i].style.backgroundColor = '#212529';
    }
  } else {
    nav.classList.remove('bg-dark', 'shadow');
    for (let i = 0; i < bgColor.length; i++) {
      bgColor[i].style.backgroundColor = '#21252900';
    }
  }
});
