const ship_data = {
  Standard: {
    fullname: "Standard Shipping",
    fee: 5.99,
    estimate_shipping_day: 5,
  },
  Air: { fullname: "Air Freight", fee: 29.99, estimate_shipping_day: 2 },
  Sea: { fullname: "Sea Freight", fee: 19.99, estimate_shipping_day: 14 },
  Express: {
    fullname: "Express Shipping",
    fee: 99.99,
    estimate_shipping_day: 1,
  },
  Truck: {
    fullname: "Truck Delivery",
    fee: 49.99,
    estimate_shipping_day: 3,
  },
  Mail: { fullname: "Mail Delivery", fee: 3.99, estimate_shipping_day: 7 },
  Local: {
    fullname: "Local Delivery",
    fee: 0.99,
    estimate_shipping_day: 2,
  },
};

// fetch("http://localhost:8001/shipment/method/all/", {
//   mode: "cors",
// })
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error("Network response was not ok");
//     }
//     return response.json(); // Parse the JSON response
//   })
//   .then((data) => {
//     console.log(ship_data);
//     ship_data = data;
//   })
//   .catch((error) => {
//     console.error("There was a problem with the fetch operation:", error);
//   });

const shippingMethodSelect = document.getElementById("shipping-method");

function updateShippingFee() {
  const selectedMethod = shippingMethodSelect.value;
  const shippingFee = ship_data[selectedMethod].fee;
  document.getElementById("shipping-fee").textContent = `$${shippingFee.toFixed(
    2
  )}`;

  // Retrieve the shipping fee value from the span with id "shipping-fee"
  const shippingFeeText = document.getElementById("shipping-fee").textContent;
  const shippingFeeFloat = parseFloat(shippingFeeText.replace("$", ""));

  // Retrieve the total price value
  const totalPriceText =
    document.querySelector(".total-price-label").textContent;
  const totalPrice = parseFloat(totalPriceText.replace("Total Price: $", ""));

  // Calculate the total amount by adding the shipping fee and total price
  const totalAmount = shippingFeeFloat + totalPrice;

  // Update the content of the span with id "total-amount" to display the total amount
  document.getElementById("total-amount").textContent = `$${totalAmount.toFixed(
    2
  )}`;
}

updateShippingFee();
shippingMethodSelect.addEventListener("change", function () {
  updateShippingFee();
});

/////

const paymentMethodSelect = document.getElementById("payment-method");

function updateCreditCardFieldsVisibility() {
  const selectedMethod = paymentMethodSelect.value;
  const creditCardFieldsDiv = document.getElementById("credit-card-fields");

  if (selectedMethod === "Cash on Delivery") {
    creditCardFieldsDiv.style.display = "none";
  } else {
    creditCardFieldsDiv.style.display = "block";
  }
}

updateCreditCardFieldsVisibility();

paymentMethodSelect.addEventListener("change", function () {
  updateCreditCardFieldsVisibility();
});
