document.getElementById('submitbtn').addEventListener('click', e => {
    e.preventDefault(); // prevent the form from being submitted
    


    let containers = document.getElementsByClassName("card");
// Loop through the elements and remove them from the DOM
    while (containers.length > 0) {
    containers[0].parentNode.removeChild(containers[0]);
    }
    // Make the fetch request
    fetch('/search?q=' + document.getElementById('query').value)
      .then(response => response.json())
      .then(data => {
      //   for (let i=0; i<50; i++) {
      //     let card = document.createElement("div");
      //     card.classList.add("card-container");
        
      //     document.getElementById("results").appendChild(card);
      //   }    
        
        // if (data.length >= 20) {
        //   let comment = document.createElement("div");
        //   comment.classList.add("comment");
        //   comment.innerHTML = `<p>Here are 20 of the most relevant search results</p>`;
        //   document.body.appendChild(comment);
        // } else 
        if (data.length == 0) {
          let comment = document.createElement("div");
          comment.classList.add("comment");
          comment.innerHTML = `<p>Oops, no results found.</p>`;
          document.body.appendChild(comment);
        }
        
        for (let i = 0; i < data.length; i++) {
            let card = document.createElement("div");
            card.classList.add("card");
          
            let cardContainer = document.createElement("div");
            cardContainer.classList.add("card-container");
          
            cardContainer.innerHTML = `<h3>${data[i].title}</h3><a>${data[i].url}</a><p>${data[i].content}</p>`;
          
            card.appendChild(cardContainer);
          
            document.body.appendChild(card);
          }
        // Process the data here
    //     document.getElementById("results").innerHTML = data.map(res => (`
    //         ${res.title}
    //     `)).join("</br>")
      });
  });
  