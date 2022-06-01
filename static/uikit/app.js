let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
    alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}


const dropdownMenu = document.querySelector(".dropdown-menu1");
const dropdownButton = document.querySelector(".dropdown-button1");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show1");
  });
}


const conversationThread = document.querySelector(".thread__details1");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;