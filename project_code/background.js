// background.js

// Execute the function when the extension icon is clicked
chrome.browserAction.onClicked.addListener(() => {
  // console.log("Icon clicked");

  // Read the JSON file with sentiment analysis results
  const fetchPromise = fetch(chrome.runtime.getURL('/sentiment_results.json'));
  // console.log("Fetch Promise:", fetchPromise);

  fetchPromise
    .then(response => {
      console.log("Response:", response);
      return response.json();
    })
    .then(data => {
      console.log("Data:", data);

      // Send the data to the content script
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        console.log("Sending data to content script");
        chrome.tabs.sendMessage(tabs[0].id, {
          action: "updateSentimentAnalysis",
          data: data
        });
      });
    })
    .catch(error => console.error('Error reading sentiment_results.json:', error));
});
