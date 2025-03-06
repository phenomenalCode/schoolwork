// Key and values
const obj = {
    "china-btn": "china",
    "italy-btn": "italy",
    "usa-btn": "usa",
    "all-btn": "all",
    "vegetarian-btn": "vegetarian"
  };
 
  // Get all cards using card class
  const recipeCards = document.querySelectorAll(".card");
  
  // Add event listeners to filter buttons
  Object.keys(obj).forEach(buttonId => {
    const button = document.getElementById(buttonId);
  
    button.addEventListener("click", () => {
      const targetElementId = obj[buttonId];
  
      recipeCards.forEach(card => {
        // Show all recipe cards if "all-btn" is clicked
        if (targetElementId === "all") {
          card.style.display = "block"; // Show all cards
        } 
        // Vegetarian-specific logic
        else if (targetElementId === "vegetarian" && card.id === "italy") {
          card.style.display = "block";
           // Show vegetarian-specific card (e.g., Italy)
        } 
        // Match based on ID
        else if (card.id === targetElementId) {
          card.style.display = "block";
           // Show matching cards based on ID
        } 
        // Hide non-matching cards
        else {
          card.style.display = "none";
        }
      });
    });
  });
  