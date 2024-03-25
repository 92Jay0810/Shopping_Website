console.log("this is working");
let btns = document.querySelectorAll(".addCart");
btns.forEach((btn) => {
  btn.addEventListener("click", addToCart);
});
let debtns = document.querySelectorAll(".minCart");
debtns.forEach((btn) => {
  btn.addEventListener("click", decreaseCart);
});
let deletebtns = document.querySelectorAll(".delete_btn");
deletebtns.forEach((btn) => {
  btn.addEventListener("click", delete_Cart);
});

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
      window.location.reload();
    })
    .catch((error) => {
      console.log(error);
    });
}
function decreaseCart(e) {
  let product_id = e.target.value;
  console.log(product_id);
  let url = "/decreaseCart/";
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
      window.location.reload();
    })
    .catch((error) => {
      console.log(error);
    });
}
function delete_Cart(e) {
  let product_id = e.target.value;
  console.log(product_id);
  let url = "/deleteCartitem/";
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
      window.location.reload();
    })
    .catch((error) => {
      console.log(error);
    });
}
