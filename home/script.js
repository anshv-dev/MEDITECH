const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link'); // Fix the selector

const btnpopup = document.querySelector('.btnLogin-popup');
const iconclose=document.querySelector('.icon-closed');
registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btnpopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});
iconclose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});
