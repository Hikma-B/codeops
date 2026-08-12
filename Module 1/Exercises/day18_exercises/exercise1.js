const prices = [500, 800, 1200, 300, 950];

// Add 15% VAT
const pricesWithVat = prices.map(price => price * 1.15);

// Keep prices under 1000
const under1000 = pricesWithVat.filter(price => price < 1000);

// Calculate grand total
const grandTotal = under1000.reduce((total, price) => total + price, 0);

console.log("Prices with VAT:", pricesWithVat);
console.log("Prices under 1000:", under1000);
console.log("Grand Total:", grandTotal);