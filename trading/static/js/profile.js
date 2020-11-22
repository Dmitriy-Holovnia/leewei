const allLinks = document.querySelectorAll('.profile__link');

allLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    allLinks.forEach(e => {
      e.classList.remove('profile__nav_active');
    })
    e.target.classList.add('profile__nav_active')
  })
})
