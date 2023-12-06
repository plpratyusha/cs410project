// background.js

// Execute the function when the extension icon is clicked
chrome.browserAction.onClicked.addListener(() => {

  // Read the JSON file with sentiment analysis results
  fetch(chrome.runtime.getURL('/sentiment_results.json'))
    .then(response => response.json())
    .then(data => {
      
      // Send the data to the content script
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {
          action: "updateSentimentAnalysis",
          data: data
        });
      });
    })
    .catch(error => console.error('Error reading sentiment_results.json:', error));
});
