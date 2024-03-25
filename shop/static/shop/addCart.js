console.log("this is working");
let btns = document.querySelectorAll(".addCart");
let log_check = document.querySelector(".log_check");
let CartButton = document.querySelector(".CartButton");
if (log_check.dataset.value === "1") {
  btns.forEach((btn) => {
    btn.addEventListener("click", addToCart);
  });
} else {
  btns.forEach((btn) => {
    btn.addEventListener("click", alertLogin);
  });
  CartButton.addEventListener("click", alertLogin);
}

function addToCart(e) {
  let product_id = e.target.value;
  console.log(product_id);
  let url = "/addToCart/";
  let data = { id: product_id };
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("number_of_item").innerHTML = data;
      console.log(data);
    })
    .catch((error) => {
      console.log(error);
    });
}

function alertLogin(e) {
  alert("please login");
}
