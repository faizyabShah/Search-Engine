document.getElementById('submitbtn').addEventListener('click', e => {
    e.preventDefault(); // prevent the form from being submitted
    


    let containers = document.getElementsByClassName("card-container");
// Loop through the elements and remove them from the DOM
    while (containers.length > 0) {
    containers[0].parentNode.removeChild(containers[0]);
    }
    // Make the fetch request
    fetch('/search?q=' + document.getElementById('query').value)
      .then(response => response.json())
      .then(data => {

        for (let i = 0; i < data.length; i++) {
            console.log(data[i])
            let card = document.createElement("div");
            card.classList.add("card");
          
            let cardContainer = document.createElement("div");
            cardContainer.classList.add("card-container");
          
            cardContainer.innerHTML = `<h3>${data[i].title}</h3><p>${data[i].url}<p>${data[i].content}</p>`;
          
            card.appendChild(cardContainer);
          
            document.body.appendChild(card);
          }
        // Process the data here
    //     document.getElementById("results").innerHTML = data.map(res => (`
    //         ${res.title}
    //     `)).join("</br>")
      });
  });
  