const acknowledgementKey = "foodbooking-notice-dismissed";

export function initializePrivacyNotice() {
  const notice = document.querySelector("#privacy-notice");
  if (hasAcknowledgedNotice()) notice.hidden = true;
  const button = document.querySelector("#dismiss-privacy-notice");
  button.hidden = false;
  button.addEventListener("click", dismissPrivacyNotice);
  new ResizeObserver(reserveNoticeSpace).observe(notice);
  reserveNoticeSpace();
}

function hasAcknowledgedNotice() {
  try {
    return sessionStorage.getItem(acknowledgementKey) === "true";
  } catch {
    return false;
  }
}

function dismissPrivacyNotice() {
  document.querySelector("#privacy-notice").hidden = true;
  reserveNoticeSpace();
  try {
    sessionStorage.setItem(acknowledgementKey, "true");
  } catch {
    // Dismissing still works when browser storage is unavailable.
  }
}

function reserveNoticeSpace() {
  const notice = document.querySelector("#privacy-notice");
  const height = notice.hidden ? 0 : notice.offsetHeight + 32;
  document.body.style.setProperty("--privacy-notice-height", `${height}px`);
}
