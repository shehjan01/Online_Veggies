// document.addEventListener('DOMContentLoaded', () => {
//     const loginForm = document.getElementById('loginForm');
//     if (loginForm) {
//         loginForm.addEventListener('submit', (e) => {
//             e.preventDefault();
//             const username = document.getElementById('username').value;
//             const password = document.getElementById('password').value;
//             console.log('Username:', username);
//             console.log('Password:', password);
//         });
//     }
// });
// function redirect(action) {
//     if (!isLoggedIn()) {
//         window.location.href = 'login.html';
//     } else {
//         if (action === 'cart') {
//             window.location.href = 'cart.html';
//         } else if (action === 'buy') {
//             window.location.href = 'buy.html';
//         }
//     }
// }

// function isLoggedIn() {
//     // Check if user is logged in
//     // This is a placeholder function, you need to implement the actual login check
//     return false; // change this to actual login status
// }


function viewProduct(name, price, description, image) {
    const url = `product.html?name=${encodeURIComponent(name)}&price=${encodeURIComponent(price)}&description=${encodeURIComponent(description)}&image=${encodeURIComponent(image)}`;
    window.location.href = url;
}
function viewProduct2(name, price, description, image) {
    const url = `product2.html?name=${encodeURIComponent(name)}&price=${encodeURIComponent(price)}&description=${encodeURIComponent(description)}&image=${encodeURIComponent(image)}`;
    window.location.href = url;
}

