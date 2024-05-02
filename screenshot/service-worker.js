chrome.action.onClicked.addListener(async function () {
  const screenshotUrl = await chrome.tabs.captureVisibleTab();

  chrome.downloads.download({
    url: screenshotUrl,
    filename: "screenshot.png",
    conflictAction: "uniquify",
    saveAs: true
  });
});
