// content.js

// Listen for a message from the background script
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.action === "updateSentimentAnalysis") {
      displayPopup(request.data);
    }
  }
);

// Function to display sentiment analysis results in a popup dialog
function displayPopup(data) {
  
  // Extract predicted ratings
  const predictedRatings = data.predicted_ratings;

  // Calculate the average predicted rating
  const averageRating = predictedRatings.reduce((sum, rating) => sum + rating, 0) / predictedRatings.length;

  // Determine sentiment message based on the average rating
  let sentimentMessage = "";
  if (averageRating > 3.5) {
    sentimentMessage = "Wow, this recipe has a lot of positive ratings!";
  } else if (averageRating < 2.5) {
    sentimentMessage = "Hmm, this recipe does not have many positive ratings.";
  } else {
    sentimentMessage = "This recipe has pretty neutral ratings.";
  }

  // Create a popup dialog
  const popupContainer = document.createElement('div');
  popupContainer.style.cssText = 'position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #fff; padding: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); z-index: 9999;';

  // Display the average predicted rating and sentiment message in the popup
  popupContainer.innerHTML = `
    <h3>Predicted Overall Comment Rating</h3>
    <p><strong>Average Comment Rating:</strong> ${averageRating.toFixed(2)}</p>
    <p>${sentimentMessage}</p>
    <button id="closePopupBtn">Close</button>
  `;

  // Append the popup to the body
  document.body.appendChild(popupContainer);

  // Close the popup when the close button is clicked
  document.getElementById('closePopupBtn').addEventListener('click', function() {
    document.body.removeChild(popupContainer);
  });
}
