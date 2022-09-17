var cartButton = document.getElementById('cartButton');

let data = {
    count: 1,
    productVersion: {
        title: "Default",
        color: 'yellow',
        size: "M",
        quantity: 1,
        old_price: '120',
    }
}

const addToCart = (data) => {
    fetch('127.0.0.1:8000/en-us/cart/', {
        method: "POST",
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(data),
    })
}
console.log('isWorking')
cartButton.addEventListener('click', (data) => {
    console.log("success")
    addToCart(data);
})