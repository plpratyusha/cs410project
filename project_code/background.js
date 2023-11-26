// background.js

// Dummy sentiment analysis results
const dummyResults = {
  scraped_data: ["Comment 1", "Comment 2"],
  actual_ratings: [1, 0],
  predicted_sentiment: [1, 0],
  accuracy: 0.85
};

// Execute the function when the extension icon is clicked
chrome.browserAction.onClicked.addListener(() => {
  // Send the dummy results to the content script
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {
      action: "updateSentimentAnalysis",
      data: dummyResults
    });
  });
});
