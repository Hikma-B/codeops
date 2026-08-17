import { transactions } from "./transactions.js";
import { totalByType, receipts } from "./report.js";

const debits = totalByType(transactions, "debit");
const credits = totalByType(transactions, "credit");

console.log("TeleBirr Transaction Report");
console.log("----------------------------");
console.log('Debits: ${debits} ETB');

console.log('Credits: ${credits} ETB');
console.log("Receipts:");
console.log(receipts(transactions));

// Spread: create an updated copy without changing the original
const updatedTransaction = {
    ...transactions[0],
    amount: 300
};

console.log("Original:", transactions[0]);
console.log("Updated:", updatedTransaction);