async function loadQuote() {
  const quoteText = document.getElementById("quote-text");
  const quoteAuthor = document.getElementById("quote-author");
  const btn = document.getElementById("refresh-quote");

  quoteText.classList.add("loading");
  btn.disabled = true;

  try {
    const data = await api.quotes.random();
    quoteText.style.opacity = 0;
    quoteAuthor.style.opacity = 0;

    setTimeout(() => {
      quoteText.textContent = `"${data.quote}"`;
      quoteAuthor.textContent = `— ${data.author}`;
      quoteText.style.opacity = 1;
      quoteAuthor.style.opacity = 1;
    }, 200);
  } catch (e) {
    quoteText.textContent = '"Keep going. Everything you need will come to you."';
    quoteAuthor.textContent = "— Focus Track";
  } finally {
    quoteText.classList.remove("loading");
    btn.disabled = false;
  }
}
