const customer = {
    name: "Hikma",
    city: "Addis Ababa",
    balance: 2500
};

// Destructure name and city
const { name, city } = customer;

console.log("Name:", name);
console.log("City:", city);

// Parameter destructuring
function greet({ name }) {
    console.log("Hello, ${name}!");
}

greet(customer);