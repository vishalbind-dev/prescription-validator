document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("prescriptionForm");

    form.addEventListener("submit", function () {

        const button = form.querySelector("button");

        button.innerText = "Validating...";

        button.disabled = true;

    });

});
