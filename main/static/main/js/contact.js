window.onload = function() {
  var popup = document.getElementById('popup-message');
  if (popup) {
    popup.style.display = 'block';
    // Прокрутить к форме контакта, чтобы фокус был там, а не наверху
    document.getElementById('contact').scrollIntoView({behavior: 'smooth'});
    setTimeout(function() {
      popup.style.display = 'none';
    }, 3000);
  }
}
