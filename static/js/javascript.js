const main = document.getElementsByClassName('main')[0];
main.addEventListener('click', navbar_hide2)


function navbar_hide() {
  const navContent = document.getElementById('navbarContent');
  navContent.setAttribute("class", "navbar-collapse collapse");
}

function navbar_hide2() {
  const navContent = document.getElementById('navbarContent');
  const bsCollapse = new bootstrap.Collapse(navContent, {toggle:false})
  bsCollapse.hide()
}
