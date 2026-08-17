// 1. VAT
function vat(amount, rate = 0.15) {
    return amount + amount * rate;
}

const vatArrow = (amount, rate = 0.15) => amount + amount * rate;

console.log("1.", vat(1000));
console.log("1 Arrow:", vatArrow(1000));


// 2. Counter closure
function makeCounter() {
    let count = 0;

    return function () {
        count++;
        return count;
    };
}

const counter = makeCounter();

console.log("2.", counter());
console.log("2.", counter());
console.log("2.", counter());

// count stays private because it is inside makeCounter.


// 3. Discount factory
function discountBy(rate) {
    return function (price) {
        return price - price * rate;
    };
}

const memberPrice = discountBy(0.10);
const salePrice = discountBy(0.30);

console.log("3. Member:", memberPrice(1000), "ETB");
console.log("3. Sale:", salePrice(1000), "ETB");


// 4. Higher-order function
function applyToAll(list, fn) {
    return list.map(fn);
}

const prices = [100, 200, 500];

const pricesWithVAT = applyToAll(prices, price => vat(price));

console.log("4.", pricesWithVAT);


// 5. forEach
const cities = ["Addis Ababa", "Hawassa", "Bahir Dar", "Dire Dawa"];

cities.forEach(function(city, index) {
    console.log((index + 1) + ". " + city);
});