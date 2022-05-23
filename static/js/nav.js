let nav = document.querySelector('nav');
let bgColor = document.getElementsByClassName('dropdown-menu')

window.addEventListener('resize', function() {
  if (screen.width < 1200) {
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
