// Находим кнопку
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Показывать кнопку, если страница прокручена вниз
window.onscroll = function() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
};

// При клике прокручиваем страницу наверх
scrollToTopBtn.addEventListener("click", function() {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
