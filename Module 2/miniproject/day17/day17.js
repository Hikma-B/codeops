
// MINI PROJECT — Loyalty Points Module

function createLoyalty(earnRule) {
    let points = 0;

    function earn(amount) {
        points += earnRule(amount);
    }

    function redeem(amount) {
        points = Math.max(0, points - amount);
    }

    function balance() {
        return points;
    }

    return { earn, redeem, balance };
}


// Normal rule: 1 point per 10 ETB
const normalRule = amount => Math.floor(amount / 10);

const loyalty = createLoyalty(normalRule);

loyalty.earn(100);
console.log("Mini Project balance:", loyalty.balance());

loyalty.redeem(3);
console.log("After redeem:", loyalty.balance());


// Holiday rule: double points
const holidayRule = amount => Math.floor(amount / 10) * 2;

const holidayLoyalty = createLoyalty(holidayRule);

holidayLoyalty.earn(100);
console.log("Holiday balance:", holidayLoyalty.balance());