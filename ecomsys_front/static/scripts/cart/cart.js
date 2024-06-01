document.addEventListener("DOMContentLoaded", function () {
  var table = document.querySelector("table");
  var orderButton = document.querySelector(".order-button");

  if (table.rows.length <= 1) {
    // Check if the table has only the header row
    orderButton.style.display = "none";
  }
});
