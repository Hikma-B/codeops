// 1. Change h1 text and toggle a CSS class
const title = document.querySelector("#title");

title.textContent = "Day 19 DOM Practice";
title.classList.toggle("highlight");


// 2. Create li elements from Ethiopian city names
const cities = ["Addis Ababa", "Hawassa", "Bahir Dar"];
const cityList = document.querySelector("#cityList");

cities.forEach(function(city) {
    const li = document.createElement("li");
    li.textContent = city;
    cityList.appendChild(li);
});


// 3. Event bubbling
const button = document.querySelector("#myButton");
const container = document.querySelector("#buttonContainer");

button.addEventListener("click", function(event) {
    console.log("Button target:", event.target);
});

container.addEventListener("click", function(event) {
    console.log("Container clicked");
});


// 4. Event delegation for delete buttons
const itemList = document.querySelector("#itemList");

itemList.addEventListener("click", function(event) {
    if (event.target.classList.contains("delete-btn")) {
        event.target.parentElement.remove();
    }
});


// 5. Form submit
const form = document.querySelector("#itemForm");
const input = document.querySelector("#itemInput");
const newItemsList = document.querySelector("#newItemsList");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const value = input.value;

    if (value.trim() !== "") {
        const li = document.createElement("li");
        li.textContent = value;

        newItemsList.appendChild(li);

        input.value = "";
    }
});