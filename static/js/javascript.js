document.getElementsByClassName("main")[0].addEventListener("click", navbar_hide);


function navbar_hide() {
  const menuToggle = document.getElementById('navbarContent');
  menuToggle.setAttribute("class", "navbar-collapse collapse");
}
